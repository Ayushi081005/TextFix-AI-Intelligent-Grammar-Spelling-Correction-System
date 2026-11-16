
import re
import math
from collections import Counter


# Common English words that carry less information
STOP_WORDS = {
    "a", "an", "the", "is", "am", "are", "was", "were",
    "be", "been", "being", "to", "of", "and", "or", "in",
    "on", "at", "by", "for", "with", "about", "from", "as",
    "it", "its", "this", "that", "these", "those", "i",
    "you", "he", "she", "we", "they", "them", "my", "your",
    "his", "her", "our", "their", "me", "us", "do", "does",
    "did", "have", "has", "had", "can", "could", "will",
    "would", "should", "may", "might", "must", "not", "but",
    "if", "then", "than", "so", "because", "while", "when",
    "where", "who", "which", "what", "how", "there", "here",
    "also", "very", "just", "more", "most", "some", "any"
}


def split_sentences(text):
    """
    Split text into individual sentences.
    """

    text = text.strip()

    if not text:
        return []

    sentences = re.split(
        r'(?<=[.!?])\s+',
        text
    )

    return [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]


def tokenize(sentence):
    """
    Convert a sentence into lowercase words.
    """

    words = re.findall(
        r"\b[a-zA-Z]+\b",
        sentence.lower()
    )

    return [
        word for word in words
        if word not in STOP_WORDS
    ]


def summarize_text(text, length="medium"):
    """
    Generate an extractive summary using
    TF-IDF-based sentence ranking.

    length:
        short  = approximately 20% of sentences
        medium = approximately 35% of sentences
        long   = approximately 50% of sentences
    """

    if not text or not text.strip():
        raise ValueError("Please provide text to summarize.")

    sentences = split_sentences(text)

    if not sentences:
        raise ValueError("No meaningful sentences found.")

    # For very short documents, retain the original text.
    if len(sentences) <= 2:
        summary = text.strip()

        return {
            "summary": summary,
            "original_word_count": len(text.split()),
            "summary_word_count": len(summary.split()),
            "compression_percentage": 0,
            "original_sentence_count": len(sentences),
            "summary_sentence_count": len(sentences)
        }

    # Select summary ratio.
    ratios = {
        "short": 0.20,
        "medium": 0.35,
        "long": 0.50
    }

    if length not in ratios:
        length = "medium"

    ratio = ratios[length]

    # Tokenize every sentence.
    tokenized_sentences = [
        tokenize(sentence)
        for sentence in sentences
    ]

    # Calculate document frequency.
    document_frequency = Counter()

    for words in tokenized_sentences:
        unique_words = set(words)

        for word in unique_words:
            document_frequency[word] += 1

    total_sentences = len(sentences)

    # Calculate TF-IDF sentence scores.
    sentence_scores = []

    for index, words in enumerate(tokenized_sentences):

        if not words:
            sentence_scores.append(0)
            continue

        word_counts = Counter(words)
        total_words = len(words)

        score = 0

        for word, frequency in word_counts.items():

            tf = frequency / total_words

            idf = math.log(
                (total_sentences + 1)
                / (document_frequency[word] + 1)
            ) + 1

            score += tf * idf

        # Normalize for sentence length.
        score = score / math.sqrt(total_words)

        # Give a small preference to earlier sentences.
        position_bonus = 1 + (0.15 / (index + 1))

        score *= position_bonus

        sentence_scores.append(score)

    # Determine how many sentences to select.
    selected_count = max(
        1,
        math.ceil(total_sentences * ratio)
    )

    selected_count = min(
        selected_count,
        total_sentences
    )

    # Rank sentences by score.
    ranked_indices = sorted(
        range(total_sentences),
        key=lambda i: sentence_scores[i],
        reverse=True
    )

    selected_indices = ranked_indices[:selected_count]

    # Restore original sentence order.
    selected_indices.sort()

    summary_sentences = [
        sentences[index]
        for index in selected_indices
    ]

    summary = " ".join(summary_sentences)

    # Calculate summary statistics.
    original_word_count = len(text.split())
    summary_word_count = len(summary.split())

    if original_word_count > 0:

        compression_percentage = round(
            (
                1 - summary_word_count / original_word_count
            ) * 100,
            2
        )

    else:
        compression_percentage = 0

    return {
        "summary": summary,
        "original_word_count": original_word_count,
        "summary_word_count": summary_word_count,
        "compression_percentage": max(
            0,
            compression_percentage
        ),
        "original_sentence_count": total_sentences,
        "summary_sentence_count": len(summary_sentences)
    }
