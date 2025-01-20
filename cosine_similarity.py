"""
Provides a function to calculate cosine similarity between tokenized texts.
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


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

    vectr = CountVectorizer()
    processed = [" ".join(tokens1), " ".join(tokens2)]
    vectors = vectr.fit_transform(processed).toarray()

    # Calculate cosine similarity and extract the similarity value from the result matrix
    sim = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
    return round(sim * 100, 2)
