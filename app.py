import re
import math

from flask import Flask, render_template, request

from services.spell_checker import spell_checker
from services.document_parser import DocumentParser




app = Flask(__name__)

# Maximum upload size: 2 MB
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024


# =========================================
# TEXT STATISTICS
# =========================================

def calculate_text_statistics(text):
    """
    Calculate basic statistics for the submitted text.
    """

    # -------------------------
    # Words
    # -------------------------

    words = re.findall(
        r"\b[\w']+\b",
        text
    )

    word_count = len(words)


    # -------------------------
    # Sentences
    # -------------------------

    sentences = re.findall(
        r"[.!?]+(?=\s|$)",
        text
    )

    sentence_count = len(sentences)


    # If there is text but no punctuation,
    # consider it one sentence.

    if sentence_count == 0 and text.strip():
        sentence_count = 1


    # -------------------------
    # Characters
    # -------------------------

    character_count = len(text)


    # -------------------------
    # Characters excluding spaces
    # -------------------------

    characters_no_spaces = len(
        re.sub(
            r"\s",
            "",
            text
        )
    )


    # -------------------------
    # Average words per sentence
    # -------------------------

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

# =========================================
# WRITING QUALITY ANALYSIS
# =========================================

def calculate_writing_quality(
    text,
    word_count,
    sentence_count,
    total_errors,
    spelling_errors,
    grammar_errors
):
    """
    Calculate readability and writing quality scores.
    """

    # -----------------------------------------
    # READABILITY SCORE
    # -----------------------------------------

    if word_count == 0 or sentence_count == 0:

        readability_score = 0

    else:

        # Approximate syllable count
        words = re.findall(
            r"\b[a-zA-Z]+\b",
            text.lower()
        )

        syllables = 0

        for word in words:

            word = word.lower()

            vowel_groups = re.findall(
                r"[aeiouy]+",
                word
            )

            count = len(vowel_groups)

            # Every word has at least one syllable
            if count == 0:
                count = 1

            # Silent 'e'
            if (
                word.endswith("e")
                and count > 1
            ):
                count -= 1

            syllables += count


        # Flesch Reading Ease
        readability_score = (
            206.835
            - (
                1.015
                * (word_count / sentence_count)
            )
            - (
                84.6
                * (syllables / word_count)
            )
        )


        readability_score = max(
            0,
            min(
                100,
                round(readability_score)
            )
        )


    # -----------------------------------------
    # SPELLING ACCURACY
    # -----------------------------------------

    if word_count > 0:

        spelling_accuracy = (
            100
            - (
                spelling_errors
                / word_count
                * 100
            )
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


    # -----------------------------------------
    # GRAMMAR ACCURACY
    # -----------------------------------------

    if word_count > 0:

        grammar_accuracy = (
            100
            - (
                grammar_errors
                / word_count
                * 100
            )
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


    # -----------------------------------------
    # SENTENCE CLARITY
    # -----------------------------------------

    if sentence_count > 0:

        average_sentence_length = (
            word_count
            / sentence_count
        )

        # Short-to-medium sentences are
        # generally easier to read.

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


    # -----------------------------------------
    # OVERALL SCORE
    # -----------------------------------------

    overall_score = round(
        (
            readability_score * 0.35
            + grammar_accuracy * 0.30
            + spelling_accuracy * 0.20
            + sentence_clarity * 0.15
        )
    )


    # -----------------------------------------
    # QUALITY LABEL
    # -----------------------------------------

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

        "readability_score":
            readability_score,

        "spelling_accuracy":
            spelling_accuracy,

        "grammar_accuracy":
            grammar_accuracy,

        "sentence_clarity":
            sentence_clarity,

        "overall_score":
            overall_score,

        "quality_label":
            quality_label
    }

# =========================================
# HOME PAGE
# =========================================

@app.route("/")
def index():

    return render_template(
        "index.html"
    )


# =========================================
# TEXT ANALYSIS
# =========================================

@app.route(
    "/check",
    methods=["POST"]
)
def check():

    # -------------------------
    # Get manual text
    # -------------------------

    text = request.form.get(
        "text",
        ""
    ).strip()


    # -------------------------
    # Get uploaded file
    # -------------------------

    uploaded_file = request.files.get(
        "file"
    )


    try:

        # =================================
        # DETERMINE INPUT SOURCE
        # =================================

        if (
            uploaded_file
            and uploaded_file.filename
        ):

            print(
                f"Processing file: "
                f"{uploaded_file.filename}"
            )


            # Extract text from PDF/PPTX

            text = DocumentParser.extract_text(
                uploaded_file
            )


        # =================================
        # VALIDATE TEXT
        # =================================

        if not text:

            return render_template(
                "index.html",
                error=(
                    "Please enter text or "
                    "upload a valid PDF/PPTX file."
                )
            )


        # =================================
        # CALCULATE TEXT STATISTICS
        # =================================

        statistics = calculate_text_statistics(
            text
        )


        print(
            f"Words: "
            f"{statistics['word_count']}"
        )

        print(
            f"Sentences: "
            f"{statistics['sentence_count']}"
        )

        print(
            f"Characters: "
            f"{statistics['character_count']}"
        )


        # =================================
        # NLP ANALYSIS
        # =================================

        print(
            "Analyzing text..."
        )


        result = spell_checker.analyze(
            text
        )


        print(
            "Analysis complete."
        )


        # =================================
        # SHOW RESULTS
        # =================================

        return render_template(

            "result.html",

            # -------------------------
            # Existing analysis data
            # -------------------------

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


            # -------------------------
            # Text statistics
            # -------------------------

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


    # =================================
    # INVALID FILE / INPUT ERROR
    # =================================

    except ValueError as error:

        return render_template(

            "index.html",

            error=str(error)

        )


    # =================================
    # GENERAL ERROR
    # =================================

    except Exception as error:

        print(
            "Processing error:",
            error
        )

        return render_template(

            "index.html",

            error=(
                "Something went wrong "
                "while processing your document."
            )

        )


# =========================================
# RUN APPLICATION
# =========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )