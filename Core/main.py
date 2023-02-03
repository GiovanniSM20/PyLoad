import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import customtkinter as ctk
from Services.app_services import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Pyload")
        # self.iconbitmap("../assets/icon.ico") // iconbitmap deprecado
        self.geometry("500x350")
        UIFont = ctk.CTkFont(family="Segoe UI", weight="bold")
        frame = ctk.CTkFrame(master=self)
        frame.pack(pady=30, padx=60, fill="both", expand=True)

        label = ctk.CTkLabel(master=frame, text="Insert an YouTube link below")
        label.pack(pady=12, padx=10)

        entry0 = ctk.CTkEntry(master=frame,
                              placeholder_text="Enter a valid link")
        entry0.pack(pady=10, padx=10)

        checkboxValue = ctk.IntVar()
        checkbox = ctk.CTkCheckBox(master=frame,
                                   text="Audio Only",
                                   variable=checkboxValue,
                                   onvalue=1,
                                   offvalue=0)
        checkbox.pack(pady=12, padx=10)

        button = ctk.CTkButton(
            hover_color="#035bbd",
            font=UIFont,
            master=frame,
            text="Download",
            command=lambda: Threads.AudioThread(entry0.get())
            if checkboxValue.get() == 1 else Threads.VideoThread(entry0.get()))
        button.pack(pady=12, padx=10)

    # def isBoxMarked(self, url):

    #     if self.checkboxValue.get() == 1:
    #         Download.audio_download(url)
    #     else:
    #         Download.video_download(url)


app = App()
app.mainloop()
