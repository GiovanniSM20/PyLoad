import os
from tkinter import *
import tkinter as tk
from pytube import YouTube
import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

def yt_download():
    url = entry0.get()
    yt = YouTube(url)
    if var1.get() == 1:
        with ydl:
            audio = yt.streams.filter(only_audio=True).first()

            # You can specify the folder of the downloaded file below
            download_file = audio.download()
            base, ext = os.path.splitext(download_file)

            new_file = base + '.mp3'
            os.rename(download_file, new_file)

            notif.config(fg="green", text="Download Completed!")

    else:
        try:
            video = yt.streams.get_highest_resolution()
            # You can specify the folder of the downloaded file below
            video.download()
            notif.config(fg="green", text="Download Completed!")

        except Exception as e:
            print(e)
            notif.config(
                fg="red",
                text=
                "Video could not be downloaded. Perhaps the link is not copied correctly."
            )

window = tk.Tk()
window.title("PyLoad")
window.iconbitmap("./assets/icon.ico")

window.geometry("1000x600")
window.configure(bg="#212121")
canvas = Canvas(window,
                bg="#212121",
                height=600,
                width=1000,
                bd=0,
                highlightthickness=0,
                relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"./assets/background.png")
background = canvas.create_image(224.0, 386.5, image=background_img)

entry0_img = PhotoImage(file=f"./assets/img_textBox0.png")
entry0_bg = canvas.create_image(501.0, 300.0, image=entry0_img)

entry0 = Entry(bd=0, bg="#000000", fg="white", highlightthickness=0)

entry0.place(x=158.0, y=279, width=686.0, height=40)

var1 = tk.IntVar()
checkbox = tk.Checkbutton(window,
                          text="Audio only",
                          variable=var1,
                          onvalue=1,
                          offvalue=0,
                          command="")
checkbox.place(x=455, y=500)

img0 = PhotoImage(file=f"./assets/img0.png")
b0 = Button(image=img0,
            bg="#212121",
            borderwidth=0,
            highlightthickness=0,
            command=yt_download,
            relief="flat")

b0.place(x=427, y=339, width=146, height=30)

notif = Label(window, font=("Segoe UI", 12), bg="#212121")
notif.place(x=500, y=400)  # not working properly
window.resizable(False, False)
window.mainloop()
