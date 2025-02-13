# Python Plagiarism Scanner

## Description

This project is a **Plagiarism Scanner** for any text-based file. It allows users to select two Python files and calculates the similarity percentage based on their content, providing an easy way to check for similarities. The project includes a GUI built with `tkinter` to make file selection and result display user-friendly.

### Features
- Calculates the percentage similarity between two text files.
- Displays results in a simple GUI.
- Supports files in any text-based format.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/SamuelWalzel/Plagiarism-Scanner.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Plagiarism-Scanner
    ```

3. Install any required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
    ```bash
    python -m spacy download en_core_web_md
    ```

## Usage

1. Run the main script to start the plagiarism scanner:

    ```bash
    python ui.py
    ```

2. Use the GUI to:
   - **Select First File**: Choose the first file you want to check for similarity.
   - **Select Second File**: Choose the second file for comparison.
   - **Check Similarity**: Click this button to calculate and display the similarity percentage between the two files.
