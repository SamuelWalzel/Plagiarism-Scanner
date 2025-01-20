def calculate_jaccard_similarity(tokens1, tokens2):
    """
    Calculates the Jaccard similarity between two sets of tokens.

    Args:
        tokens1 (list): Tokens from the first text.
        tokens2 (list): Tokens from the second text.

    Returns:
        float: Jaccard similarity as a percentage.
    """
    set1 = set(tokens1)
    set2 = set(tokens2)
    intersection = len(set1 & set2) # Intersection of both sets
    union = len(set1 | set2)  # Union of both sets
    jaccard_similarity = round((intersection / union) * 100, 2) if union > 0 else 0.0
    return jaccard_similarity
