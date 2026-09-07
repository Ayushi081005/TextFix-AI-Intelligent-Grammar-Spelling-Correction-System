import re

from flask import Flask, render_template, request

from services.spell_checker import spell_checker
from services.document_parser import DocumentParser


app = Flask(__name__)

# Maximum upload size: 2 MB
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024


# ============================================================
# TEXT STATISTICS
# ============================================================

def calculate_text_statistics(text):
    """
    Calculate basic statistics about the submitted text.
    """

    words = re.findall(r"\b[\w']+\b", text)
    word_count = len(words)

    sentences = re.findall(r"[.!?]+(?=\s|$)", text)
    sentence_count = len(sentences)

    # If text exists but no punctuation is detected,
    # consider the entire text as one sentence.
    if sentence_count == 0 and text.strip():
        sentence_count = 1

    character_count = len(text)

    characters_no_spaces = len(
        re.sub(r"\s", "", text)
    )

    if sentence_count > 0:
        avg_words_per_sentence = round(
            word_count / sentence_count,
            1
        )
    else:
        avg_words_per_sentence = 0

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "character_count": character_count,
        "characters_no_spaces": characters_no_spaces,
        "avg_words_per_sentence": avg_words_per_sentence
    }


# ============================================================
# WRITING QUALITY ANALYSIS
# ============================================================

def calculate_writing_quality(
    text,
    word_count,
    sentence_count,
    total_errors,
    spelling_errors,
    grammar_errors
):
    """
    Calculate different writing quality metrics.

    Metrics:
    - Readability
    - Spelling accuracy
    - Grammar accuracy
    - Sentence clarity
    - Overall writing quality
    """

    # --------------------------------------------------------
    # READABILITY SCORE
    # --------------------------------------------------------

    if word_count == 0 or sentence_count == 0:

        readability_score = 0

    else:

        # Extract alphabetic words for syllable estimation
        words = re.findall(
            r"\b[a-zA-Z]+\b",
            text.lower()
        )

        syllables = 0

        for word in words:

            # Find groups of vowels
            vowel_groups = re.findall(
                r"[aeiouy]+",
                word
            )

            count = len(vowel_groups)

            # Every word should have at least one syllable
            if count == 0:
                count = 1

            # Small adjustment for silent 'e'
            if word.endswith("e") and count > 1:
                count -= 1

            syllables += count

        if word_count > 0:

            readability_score = (
                206.835
                - (1.015 * (word_count / sentence_count))
                - (84.6 * (syllables / word_count))
            )

            # Keep score between 0 and 100
            readability_score = max(
                0,
                min(
                    100,
                    round(readability_score)
                )
            )

        else:

            readability_score = 0

    # --------------------------------------------------------
    # SPELLING ACCURACY
    # --------------------------------------------------------

    if word_count > 0:

        spelling_accuracy = (
            100
            - (spelling_errors / word_count * 100)
        )

    else:

        spelling_accuracy = 100

    spelling_accuracy = max(
        0,
        min(
            100,
            round(spelling_accuracy)
        )
    )

    # --------------------------------------------------------
    # GRAMMAR ACCURACY
    # --------------------------------------------------------

    if word_count > 0:

        grammar_accuracy = (
            100
            - (grammar_errors / word_count * 100)
        )

    else:

        grammar_accuracy = 100

    grammar_accuracy = max(
        0,
        min(
            100,
            round(grammar_accuracy)
        )
    )

    # --------------------------------------------------------
    # SENTENCE CLARITY
    # --------------------------------------------------------

    if sentence_count > 0:

        average_sentence_length = (
            word_count / sentence_count
        )

        if average_sentence_length <= 15:

            sentence_clarity = 100

        elif average_sentence_length <= 20:

            sentence_clarity = 90

        elif average_sentence_length <= 25:

            sentence_clarity = 80

        elif average_sentence_length <= 30:

            sentence_clarity = 65

        else:

            sentence_clarity = 50

    else:

        sentence_clarity = 0

    # --------------------------------------------------------
    # OVERALL WRITING SCORE
    # --------------------------------------------------------

    overall_score = round(
        (
            readability_score * 0.35
            + grammar_accuracy * 0.30
            + spelling_accuracy * 0.20
            + sentence_clarity * 0.15
        )
    )

    # --------------------------------------------------------
    # QUALITY LABEL
    # --------------------------------------------------------

    if overall_score >= 90:

        quality_label = "Excellent"

    elif overall_score >= 80:

        quality_label = "Very Good"

    elif overall_score >= 70:

        quality_label = "Good"

    elif overall_score >= 60:

        quality_label = "Needs Improvement"

    else:

        quality_label = "Poor"

    return {

        "readability_score": readability_score,

        "spelling_accuracy": spelling_accuracy,

        "grammar_accuracy": grammar_accuracy,

        "sentence_clarity": sentence_clarity,

        "overall_score": overall_score,

        "quality_label": quality_label
    }


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def index():

    return render_template(
        "index.html"
    )


# ============================================================
# TEXT ANALYSIS
# ============================================================

@app.route("/check", methods=["POST"])
def check():

    text = request.form.get(
        "text",
        ""
    ).strip()

    uploaded_file = request.files.get(
        "file"
    )

    try:

        # ----------------------------------------------------
        # HANDLE FILE UPLOAD
        # ----------------------------------------------------

        if uploaded_file and uploaded_file.filename:

            print(
                f"Processing file: {uploaded_file.filename}"
            )

            text = DocumentParser.extract_text(
                uploaded_file
            )

        # ----------------------------------------------------
        # VALIDATE TEXT
        # ----------------------------------------------------

        if not text:

            return render_template(
                "index.html",
                error=(
                    "Please enter text or upload "
                    "a valid PDF/PPTX file."
                )
            )

        # ----------------------------------------------------
        # CALCULATE TEXT STATISTICS
        # ----------------------------------------------------

        statistics = calculate_text_statistics(
            text
        )

        print(
            f"Words: {statistics['word_count']}"
        )

        print(
            f"Sentences: {statistics['sentence_count']}"
        )

        print(
            f"Characters: {statistics['character_count']}"
        )

        print(
            "Analyzing text..."
        )

        # ----------------------------------------------------
        # SPELLING + GRAMMAR ANALYSIS
        # ----------------------------------------------------

        result = spell_checker.analyze(
            text
        )

        # ----------------------------------------------------
        # WRITING QUALITY ANALYSIS
        # ----------------------------------------------------

        writing_quality = calculate_writing_quality(

            text=text,

            word_count=statistics[
                "word_count"
            ],

            sentence_count=statistics[
                "sentence_count"
            ],

            total_errors=result[
                "total_errors"
            ],

            spelling_errors=result[
                "spelling_errors"
            ],

            grammar_errors=result[
                "grammar_errors"
            ]
        )

        print(
            "Analysis complete."
        )

        # ----------------------------------------------------
        # SEND EVERYTHING TO RESULT PAGE
        # ----------------------------------------------------

        return render_template(

            "result.html",

            # -----------------------------------------------
            # WRITING QUALITY
            # -----------------------------------------------

            overall_score=writing_quality[
                "overall_score"
            ],

            quality_label=writing_quality[
                "quality_label"
            ],

            readability_score=writing_quality[
                "readability_score"
            ],

            spelling_accuracy=writing_quality[
                "spelling_accuracy"
            ],

            grammar_accuracy=writing_quality[
                "grammar_accuracy"
            ],

            sentence_clarity=writing_quality[
                "sentence_clarity"
            ],

            # -----------------------------------------------
            # EXISTING ANALYSIS DATA
            # -----------------------------------------------

            original_text=result[
                "original_text"
            ],

            corrected_text=result[
                "corrected_text"
            ],

            errors=result[
                "errors"
            ],

            total_errors=result[
                "total_errors"
            ],

            spelling_errors=result[
                "spelling_errors"
            ],

            grammar_errors=result[
                "grammar_errors"
            ],

            # -----------------------------------------------
            # TEXT STATISTICS
            # -----------------------------------------------

            word_count=statistics[
                "word_count"
            ],

            sentence_count=statistics[
                "sentence_count"
            ],

            character_count=statistics[
                "character_count"
            ],

            avg_words_per_sentence=statistics[
                "avg_words_per_sentence"
            ]
        )

    # ========================================================
    # INVALID FILE / USER INPUT ERROR
    # ========================================================

    except ValueError as error:

        return render_template(
            "index.html",
            error=str(error)
        )

    # ========================================================
    # GENERAL ERROR
    # ========================================================

    except Exception as error:

        print(
            "Processing error:",
            error
        )

        return render_template(

            "index.html",

            error=(
                "Something went wrong while "
                "processing your document."
            )
        )


# ============================================================
# RUN FLASK APPLICATION
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )