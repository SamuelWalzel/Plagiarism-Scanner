"""
Provides a function to calculate cosine similarity between tokenized texts.
"""

import math
from collections import Counter


def calc_cosine_sim(tokens1: list, tokens2: list) -> float:
    """
    Calculates the cosine similarity between two lists of tokens.

    Args:
        tokens1 (list): List of tokens from the first text.
        tokens2 (list): List of tokens from the second text.

    Returns:
        float: Cosine similarity in percentage.

    Raises:
        ValueError: If the token lists are empty.
    """
    if not tokens1 or not tokens2:
        raise ValueError("Token lists must not be empty.")

    freq1 = Counter(tokens1)
    freq2 = Counter(tokens2)

    unique_words = set(freq1.keys()).union(set(freq2.keys()))

    vec1 = [freq1.get(word, 0) for word in unique_words]
    vec2 = [freq2.get(word, 0) for word in unique_words]

    # Calculate dot product
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))

    # Calculate magnitude of the vectors
    magnitude1 = math.sqrt(sum(v ** 2 for v in vec1))
    magnitude2 = math.sqrt(sum(v ** 2 for v in vec2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0

    similarity = dot_product / (magnitude1 * magnitude2)
    return round(similarity * 100, 2)
