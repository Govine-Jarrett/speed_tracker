#!/usr/bin/python3
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class WordExApp:
    def __init__(self, master=None):
        # build ui
        self.WExTopLevel = tk.Tk() if master is None else tk.Toplevel(master)
        self.WExMainFrame = tk.Frame(self.WExTopLevel)
        self.BannerFrame = tk.Frame(self.WExMainFrame)
        self.BannerLabel = tk.Label(self.BannerFrame)
        self.img_WEx_Banner = tk.PhotoImage(file="res/image/WEx_Banner.png")
        self.BannerLabel.configure(image=self.img_WEx_Banner)
        self.BannerLabel.pack(side="top")
        self.BannerFrame.configure(height=100, width=585)
        self.BannerFrame.pack(side="top")
        self.TextFrame = tk.Frame(self.WExMainFrame)
        self.SentenceEntryBox = ScrolledText(self.TextFrame)
        self.SentenceEntryBox.configure(
            blockcursor="false",
            cursor="arrow",
            font="{Microsoft JhengHei} 14 {}",
            foreground="#0e2845",
        )
        self.SentenceEntryBox.configure(
            height=10,
            insertbackground="#64dd73",
            insertunfocussed="hollow",
            insertwidth=3,
        )
        self.SentenceEntryBox.configure(
            selectbackground="#64dd73",
            selectforeground="#0e2845",
            spacing1=2,
            state="normal",
        )
        self.SentenceEntryBox.configure(
            tabstyle="wordprocessor", takefocus=True, undo="true", wrap="word"
        )
        _text_ = " \n\n\n\n\n\t   E N T E R    Y O U R    T E X T    H E R E ."
        self.SentenceEntryBox.insert("0.0", _text_)
        self.SentenceEntryBox.pack(side="top")
        self.TextFrame.configure(height=200, takefocus=True, width=585)
        self.TextFrame.pack(side="top")
        self.ButtonsFrame = tk.Frame(self.WExMainFrame)
        self.ExtractWordBtn = tk.Button(self.ButtonsFrame)
        self.ExtractWordBtn.configure(
            activebackground="#0e2845",
            activeforeground="#64dd73",
            background="#64dd73",
            compound="top",
        )
        self.ExtractWordBtn.configure(
            cursor="hand2",
            default="normal",
            font="{@Microsoft JhengHei} 12 {bold}",
            foreground="#0e2845",
        )
        self.ExtractWordBtn.configure(height=2, text="E X T R A C T", width=12)
        self.ExtractWordBtn.place(relx=0.09, rely=0.19, x=0, y=0)
        self.ExtractWordBtn.configure(command=self.extract_words_to_list)
        self.ClearBtn = tk.Button(self.ButtonsFrame)
        self.ClearBtn.configure(
            activebackground="#0e2845",
            activeforeground="#e3edf9",
            background="#e3edf9",
            compound="top",
        )
        self.ClearBtn.configure(
            cursor="hand2",
            default="normal",
            font="{Microsoft JhengHei UI} 12 {bold}",
            foreground="#0e2845",
        )
        self.ClearBtn.configure(height=2, text="C L E A R", width=12)
        self.ClearBtn.place(relx=0.39, rely=0.19, x=0, y=0)
        self.ClearBtn.configure(command=self.clear_sentence)
        self.SaveBtn = tk.Button(self.ButtonsFrame)
        self.SaveBtn.configure(
            activebackground="#0e2845",
            activeforeground="#5093dc",
            background="#5093dc",
            compound="top",
        )
        self.SaveBtn.configure(
            cursor="hand2",
            default="normal",
            font="{Microsoft JhengHei UI} 12 {bold}",
            foreground="#0e2845",
        )
        self.SaveBtn.configure(height=2, text="S A V E", width=12)
        self.SaveBtn.place(relx=0.69, rely=0.19, x=0, y=0)
        self.SaveBtn.configure(command=self.save_words_to_file)
        self.VersionLabel = tk.Label(self.ButtonsFrame)
        self.VersionLabel.configure(
            background="#0e2845",
            font="{Microsoft} 10 {bold}",
            foreground="#64dd73",
            text="V 1 . 1",
        )
        self.VersionLabel.place(relx=0.47, rely=0.71, x=0, y=0)
        self.ButtonsFrame.configure(background="#0e2845", height=150, width=585)
        self.ButtonsFrame.pack(side="top")
        self.WExMainFrame.configure(height=300, relief="flat", width=585)
        self.WExMainFrame.pack(side="top")
        self.img_WEx_Logo = tk.PhotoImage(file="res/image/WEx_Logo.png")
        self.WExTopLevel.configure(height=200, takefocus=True, width=200)
        self.WExTopLevel.geometry("585x495")
        self.WExTopLevel.iconphoto(True, self.img_WEx_Logo)
        self.WExTopLevel.resizable(False, False)
        self.WExTopLevel.title("Word Extractor")

        # Main widget
        self.mainwindow = self.WExTopLevel

    def run(self):
        self.mainwindow.mainloop()

    def extract_words_to_list(self):
        pass

    def clear_sentence(self):
        pass

    def save_words_to_file(self):
        pass


if __name__ == "__main__":
    app = WordExApp()
    app.run()
