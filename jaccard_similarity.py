import os

def calculate_jaccard_similarity(file1_path: str, file2_path: str) -> float:
    """
    Calculate the Jaccard similarity between two text files.

    Args:
        file1_path (str): Path to the first text file.
        file2_path (str): Path to the second text file.

    Returns:
        float: Jaccard similarity as a percentage.

    Raises:
        FileNotFoundError: If one or both files do not exist.
        ValueError: If the files are empty or contain non-readable content.
    """
    if not os.path.exists(file1_path) or not os.path.exists(file2_path):
        raise FileNotFoundError("One or both files do not exist.")

    with open(file1_path, 'r', encoding="utf-8") as f:
        text1 = f.read().lower().split()
    with open(file2_path, 'r', encoding="utf-8") as f:
        text2 = f.read().lower().split()

    if not text1:
        raise ValueError("First file is empty or unreadable.")
    if not text2:
        raise ValueError("Second file is empty or unreadable.")

    set1 = set(text1)
    set2 = set(text2)

    intersection = len(set1 & set2)
    union = len(set1 | set2)

    similarity = intersection / union * 100
    return similarity
