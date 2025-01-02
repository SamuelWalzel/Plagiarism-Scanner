'''
Title: UI for the Final Project in Introduction to Python for the Winter Semester 2024/2025 in the FHOOE
Authors: Joao Varejao, Samuel Walzel, Tobias Czerwenka
Version: 02.01.2025
Description: Provides the user interface for the plagiarism scanner project.
'''

import tkinter as tk
from tkinter import filedialog
import difflib as dl
import text_processing as tp
 
class Frame:
    
    stored_texts = {}
    token_count = {}
    
    def __init__(self, root, frame_instance: int):
        self.root = root
        self.instance = frame_instance
        Frame.token_count[self.instance] = None
        border_label = f'File {str(self.instance)}'
        self.frame = tk.LabelFrame(self.root, text= border_label, relief="groove", borderwidth=2)
        self.filepath = None
        self.buttons()
        self.show_path()
        self.show_token_count()
        
    def buttons(self):
        self.button = tk.Button(self.frame, text='Choose file', command=self.open_file)
        self.button.pack(pady=5, padx=5)
        
    def open_file(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("text files", "*.txt")])
        print(self.filepath)
        self.path.set(f'Filepath: {self.filepath}')
        with open(self.filepath) as file:
            Frame.update_dict(self, file.read())

    def show_path(self):
        self.path = tk.StringVar(value=f'Filepath: {self.filepath}')
        self.path_label = tk.Label(self.frame, textvariable=self.path, anchor='w')
        self.path_label.pack(pady=5, padx=5, fill='x')
        
    def show_token_count(self):
        self.count = tk.StringVar(value=f'Tokens: {str(Frame.token_count[self.instance]) }')
        self.count_label = tk.Label(self.frame, textvariable=self.count, anchor='w')
        self.count_label.pack(pady=5, padx=5, fill='x')

    @classmethod
    def update_dict(cls, self, text):
        Frame.stored_texts[self.instance] = tp.process(text)
        Frame.token_count[self.instance] = len(Frame.stored_texts[self.instance])
        self.count.set(f'Tokens: {str(Frame.token_count[self.instance])}')
        print(f'Result: {Frame.stored_texts[self.instance]}')
    
class GUI:
    
    def __init__(self):
        self.root = tk.Tk()
        self.heading1 = ('Arial', 20)
        self.heading2 = ('Arial', 16)
        self.body = ('Arial', 12)
        self.root_config()
        self.first_labels()
        self.set_frames()
        self.comparison_frame()

    def root_config(self):
        self.root.title('ROOT WINDOW')
        self.root.geometry('800x500')
        self.root.grid_columnconfigure(0, weight=1, uniform='equal')
        self.root.grid_columnconfigure(1, weight=1, uniform='equal')
        self.root.rowconfigure(0, weight=0)
        self.root.rowconfigure(1, weight=0)
        self.root.rowconfigure(2, weight=0)
        
    def first_labels(self):
        self.label1 = tk.Label(self.root, text='Compare two files', font=self.body)
        self.label1.grid(columnspan=2, row=0, pady=10, padx=10)
        
    def set_frames(self):
        self.frame_1 = Frame(self.root, 1)
        self.frame_1.frame.grid(column=0, row=1, pady=10, padx=10, sticky='EW')
        self.frame_2 = Frame(self.root, 2)
        self.frame_2.frame.grid(column=1, row=1, pady=10, padx=10, sticky='EW')
             
    def comparison_frame(self):
        self.result_frame = tk.LabelFrame(self.root, text='Results', labelanchor='n', relief="groove", borderwidth=2)
        self.result_frame.grid(columnspan=2, row=2, pady=10, padx=10, sticky="ew")
        self.button = tk.Button(self.result_frame, text='Show results', command=self.compare_files)
        self.button.pack(pady=5, padx=5)
        self.sim_print = tk.StringVar(value=f'Similarity: ...')
        lbl = tk.Label(self.result_frame, textvariable=self.sim_print)
        lbl.pack(pady=5, padx=5)
        
    def compare_files(self):
        try:
            text1 = Frame.stored_texts[1]
            text2 = Frame.stored_texts[2]
            sim = int(dl.SequenceMatcher(None, text1, text2).ratio()*100)
            self.sim_print.set(f'Similarity: {str(sim)} %')
        except KeyError:
            print('texts missing')
     
def main():
    gui = GUI()
    gui.root.mainloop()
        
if __name__ == '__main__':
    main()
    