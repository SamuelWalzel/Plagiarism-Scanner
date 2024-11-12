"""
Python Plagiarism Scanner

Author:
    Czerwenka Tobias
    Samuel Walzel
    Varejao Joao

Date: 12.11.2024
Python Version: 3.12.6
"""
import difflib
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def calculate_similarity(file1_path: str, file2_path: str) -> float:
    """
    Calculate the similarity between two Python scripts based on their content.

    Args:
        file1_path (str): The path to the first file.
        file2_path (str): The path to the second file.

    Returns:
        float: The percentage similarity between the two files' contents, ranging from 0.0 to 100.0.

    Raises:
        FileNotFoundError: If either of the files does not exist.
        ValueError: If the files are empty or contain non-readable content.
    """
    if not os.path.exists(file1_path) or not os.path.exists(file2_path):
        raise FileNotFoundError("One or both files do not exist.")

    with open(file1_path, 'r', encoding="utf-8") as f:
        content1 = f.readlines()
    with open(file2_path, 'r', encoding="utf-8") as f:
        content2 = f.readlines()

    if not content1:
        raise ValueError("First file is empty or unreadable.")
    if not content2:
        raise ValueError("Second file is empty or unreadable.")

    similarity = difflib.SequenceMatcher(None, content1, content2).ratio()
    return similarity * 100


def browse_file(entry: tk.Entry) -> None:
    """
    Open a file dialog to select a file and insert the selected file path into the entry widget.

    Args:
        entry (tk.Entry): The entry widget where the selected file path will be displayed.

    Returns:
        None
    """
    file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def check_similarity(entry_file1: tk.Entry, entry_file2: tk.Entry) -> None:
    """
    Retrieve file paths from entry widgets, calculate similarity, and display the result.

    Args:
        entry_file1 (tk.Entry): Entry widget containing the path to the first file.
        entry_file2 (tk.Entry): Entry widget containing the path to the second file.

    Returns:
        None
    """
    file1_path = entry_file1.get()
    file2_path = entry_file2.get()
    # To Do

def run_gui() -> None:
    """
    Launch a GUI for the plagiarism scanner, allowing users to select two files
    and view the similarity percentage.

    Returns:
        None
    """
    root = tk.Tk()
    root.title("Python Plagiarism Scanner")

    root.mainloop()

if __name__ == "__main__":
    run_gui()
