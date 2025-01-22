'''
Title: UI for the Final Project in Introduction to Python for the Winter Semester 2024/2025 in the FHOOE
Authors: Joao Varejao, Samuel Walzel, Tobias Czerwenka
Version: 06.01.2025
Description: Provides the user interface for the plagiarism scanner project.

'''

import tkinter as tk
from tkinter import filedialog
import difflib as dl
import text_processing as tp
import word_movers_distance as wmd
from jaccard_similarity import calculate_jaccard_similarity
from cosine_similarity import calc_cosine_sim
from PIL import Image, ImageTk

class Frame:
    """
    A GUI frame class for processing and displaying information about a text file.

    Instance Variables:
        root: 
            The parent Tkinter root window.
        instance (int): 
            Identifier for the frame instance.
        frame (tk.LabelFrame): 
            A labeled frame widget for the GUI.
        filepath (str): 
            Path to the file selected by the user.
        path (tk.StringVar): 
            StringVar to display the file path in the frame.
        path_label (tk.Label): 
            Label widget for showing the file path.
        count (tk.StringVar): 
            StringVar to display the token count in the frame.
        count_label (tk.Label): 
            Label widget for showing the token count.
        button (tk.Button): 
            Button widget for file selection.
        text (tp.Text):
            A Text instance for processing the file content.

    Methods:
        __init__(self, root, frame_instance):
            Initializes a Frame instance, sets up the GUI components, and initializes class variables.

        buttons(self):
            Creates and packs a button for selecting a file into the frame.

        open_file(self):
            Opens a file dialog for selecting a text file. Updates the file path display and processes the file's content.

        show_path(self):
            Creates and packs a label for displaying the file path.

        show_token_count(self):
            Creates and packs a label for displaying the token count.

    """

    def __init__(self, root, frame_instance: int):
        """
        Initializes the Frame instance.

        Args:
            root: The parent Tkinter root window.
            frame_instance (int): Identifier for the frame instance.
        """
        self.root = root
        self.text = tp.Text('')
        self.instance = frame_instance
        border_label = f'File {str(self.instance)}'
        self.frame = tk.LabelFrame(self.root, text=border_label, relief="groove", borderwidth=2)
        self.filepath = None
        self.buttons()
        self.show_path()
        self.show_token_count()

    def buttons(self):
        """
        Creates a 'Choose file' button in the frame to allow the user to select a text file.
        """
        self.button = tk.Button(self.frame, text='Choose file', command=self.open_file)
        self.button.pack(pady=5, padx=5)

    def open_file(self):
        """
        Opens a file dialog for selecting a text file. Updates the file path display and processes the file content.
        
       Raises:
            FileNotFoundError: If the selected file is not found.
            
        """
        try:
            self.filepath = filedialog.askopenfilename(filetypes=[("text files", "*.txt")])
            if not self.filepath:
                print('No file selected')
                return
            else:
                with open(self.filepath) as file:
                    self.text = tp.Text(file.read())
                    self.count.set(f'Tokens: {str(self.text.token_count)}')
                    self.path.set(f'Filepath: {self.filepath}')
        except FileNotFoundError:
            print('File not found')

    def show_path(self):
        """
        Creates a label to display the file path and adds it to the frame.
        
        """
        self.path = tk.StringVar(value=f'Filepath: {self.filepath}')
        self.path_label = tk.Label(self.frame, textvariable=self.path, anchor='w')
        self.path_label.pack(pady=5, padx=5, fill='x')

    def show_token_count(self):
        """
        Creates a label to display the token count and adds it to the frame.
        """
        self.count = tk.StringVar(value=f'Tokens: {str(self.text.token_count)}')
        self.count_label = tk.Label(self.frame, textvariable=self.count, anchor='w')
        self.count_label.pack(pady=5, padx=5, fill='x')
    
class GUI:
    """
    A graphical user interface (GUI) application for comparing two text files and calculating their similarity.

    Instance Variables:
        root (tk.Tk): 
            The main Tkinter application window.
        heading1 (tuple): 
            Font settings for primary headings.
        heading2 (tuple): 
            Font settings for secondary headings.
        body (tuple): 
            Font settings for body text.
        frame_1 (Frame): 
            Custom frame for selecting and displaying information about the first file.
        frame_2 (Frame): 
            Custom frame for selecting and displaying information about the second file.
        result_frame (tk.LabelFrame): 
            Frame for displaying the comparison results.
        button (tk.Button): 
            Button for triggering the file comparison.
        sim_print (tk.StringVar): 
            A string variable for displaying the similarity percentage.

    Methods:
        __init__(self):
            Initializes the GUI application, configures the main window, and sets up all components.

        root_config(self):
            Configures the root window, including size, title, and grid layout.

        first_labels(self):
            Creates and displays the main title label at the top of the GUI.

        set_frames(self):
            Creates and places two frames for file selection and processing.

        comparison_frame(self):
            Creates and places a frame for displaying comparison results, along with a button and label.

        compare_files(self):
            Compares the processed text from the two frames and calculates the similarity percentage.
    """

    def __init__(self):
        """
        Initializes the GUI class instance, setting up the root window, frames, and labels.
        """
        self.root = tk.Tk()
        self.root_config()
        self.first_labels()
        self.set_frames()
        self.comparison_frame()

    def root_config(self):
        """
        Configures the root window by setting the title, size, and grid layout for uniform column widths.
        """
        self.root.title('ROOT WINDOW')
        self.root.geometry('800x500')
        self.root.grid_columnconfigure(0, weight=1, uniform='equal')
        self.root.grid_columnconfigure(1, weight=1, uniform='equal')
        self.root.rowconfigure(0, weight=0)
        self.root.rowconfigure(1, weight=0)
        self.root.rowconfigure(2, weight=0)

    def first_labels(self):
        """
        Creates and displays the main title label at the top of the GUI.
        """
        self.label1 = tk.Label(self.root, text='Compare two files')
        self.label1.grid(columnspan=2, row=0, pady=10, padx=10)
     
        try:
            logo_image = Image.open("plagiarism_logo2.jpg")
            logo_image = logo_image.resize((120, 120))
            self.logo = ImageTk.PhotoImage(logo_image)

            logo_label = tk.Label(self.root, image=self.logo)
            logo_label.grid(column=1, row=0, sticky='ne', padx=10, pady=10)

        except FileNotFoundError:
            print("Logo 'plagiarism_logo2.jpg' not found.")

    def set_frames(self):
        """
        Creates two `Frame` instances for file selection and displays them in the main window.
        """
        self.frame_1 = Frame(self.root, 1)
        self.frame_1.frame.grid(column=0, row=1, pady=10, padx=10, sticky='EW')
        self.frame_2 = Frame(self.root, 2)
        self.frame_2.frame.grid(column=1, row=1, pady=10, padx=10, sticky='EW')

    def comparison_frame(self):
        """
        Creates a frame for displaying the comparison results and sets up the button and label within it.
        """
        self.result_frame = tk.LabelFrame(self.root, text='Results', labelanchor='n', relief="groove", borderwidth=2)
        self.result_frame.grid(columnspan=2, row=2, pady=10, padx=10, sticky="ew")
        self.button = tk.Button(self.result_frame, text='Show results', command=self.compare_files)
        self.button.pack(pady=5, padx=5)
        self.sim_print = tk.StringVar(value=f'Similarity: ...')
        lbl = tk.Label(self.result_frame, textvariable=self.sim_print)
        lbl.pack(pady=5, padx=5)

    def compare_files(self):
        """
        Compares the processed text from the two frames using the SequenceMatcher from the difflib module.
        
        This method calculates the similarity percentage between the texts stored in `frame_1` and `frame_2`, 
        and displays the result in the `result_frame`.

        Raises:
            KeyError: If one or both texts are missing in `Frame.stored_tokens`.

        """
        if self.frame_1.text.text != '' and self.frame_2.text.text != '':
            text1 = self.frame_1.text.text
            text2 = self.frame_2.text.text
            tokens1 = self.frame_1.text.tokens
            tokens2 = self.frame_2.text.tokens
            word_likeness = round(dl.SequenceMatcher(None, tokens1, tokens2).ratio()*100, 2)
            print(f'word likeness: {word_likeness} %')
            token_closeness = wmd.spacy_similarity(' '.join(tokens1), ' '.join(tokens2))
            print(f'token closeness: {token_closeness} %')
            raw_text_closeness = wmd.spacy_similarity(text1, text2)
            print(f'raw text closeness: {raw_text_closeness} %')
            jaccard_similarity = calculate_jaccard_similarity(tokens1, tokens2)
            print(f'Jaccard Similarity: {jaccard_similarity} %')
            cosine_similarity = calc_cosine_sim(tokens1, tokens2)
            print(f'Cosine Similarity: {cosine_similarity} %')
         
            average_score = round(((word_likeness + jaccard_similarity)/2 + cosine_similarity + token_closeness + raw_text_closeness)/4, 2)
            self.sim_print.set(f'Similarity: {str(average_score)} %')
        else:
            print('texts missing')
     
def main():
    gui = GUI()
    gui.root.mainloop()
        
if __name__ == '__main__':
    main()
    
