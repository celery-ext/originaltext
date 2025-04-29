# my_frame.py
import tkinter as tk

class MyFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        label = tk.Label(self, text="ここに問題を表示(？)")
        label.pack()
