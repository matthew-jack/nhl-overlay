import time
from queue import Queue
from threading import Thread
import tkinter as tk

from feed import Feed

class Main():
    def __init__(self):
        self.main()

    def update_overlay(self):
        new_text = self.q.get()
        if new_text is not None:
            self.label.config(text=new_text)
        self.root.after(2000, self.update_overlay)

    def main(self):
        self.q = Queue()

        feed = Feed(self.q)

        self.root = tk.Tk()

        self.root.geometry("200x200")
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-transparent", True)
        self.root.config(bg='systemTransparent')
        self.label = tk.Label(self.root, text="Hello World")
        self.root.config(bg='systemTransparent')
        self.label.pack()
        self.root.after(2000, self.update_overlay)
        self.root.mainloop()


if __name__ == '__main__':
    Main()
