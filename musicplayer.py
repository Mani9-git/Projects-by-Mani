# importing necessary modules
import pygame
import tkinter as tkr
import os

from tkinter.filedialog import askdirectory
# importing application window
musicplayer = tkr.Tk()
# setting title for project
musicplayer.title("Mani\'s Music Player")
# setting dimensions for window
musicplayer.geometry("450x350")

# asking for directory
directory = askdirectory()
# setting music directory to the current working directory
os.chdir(directory)

# creating our songslist
# os.listdir returns a list containing all the entries in the directory given by the path
songslist = os.listdir()

# creating a playlist
playlist = tkr.Listbox(musicplayer, font="Cambria 14 bold",
                       bg="cyan2", selectmode=tkr.SINGLE)

# adding songs from songlist to the playlist
for item in songslist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

# initializing modules
pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def pause():
    pygame.mixer.music.pause()


def resume():
    pygame.mixer.music.unpause()


def Exitmusicplayer():
    pygame.mixer.music.stop()


Button_play = tkr.Button(musicplayer, height=3, width=5, text="Play Music",
                         font="Cambria 14 bold", command=play, bg="sky blue", fg="black")
Button_pause = tkr.Button(musicplayer, height=3, width=5, text="Pause Music",
                          font="Cambria 14 bold", command=pause, bg="light green", fg="black")
Button_resume = tkr.Button(musicplayer, height=3, width=5, text="Resume Music",
                           font="Cambria 14 bold", command=resume, bg="purple", fg="black")
Button_stop = tkr.Button(musicplayer, height=3, width=5, text="Stop Music",
                         font="Cambria 14 bold", command=Exitmusicplayer, bg="red", fg="black")

Button_play.pack(fill="x")
Button_pause.pack(fill="x")
Button_resume.pack(fill="x")
Button_stop.pack(fill="x")

playlist.pack(fill="both", expand="yes")

var = tkr.StringVar()

songtitle = tkr.Label(musicplayer, font="Cambria 12 bold", textvariable=var)
songtitle.pack()
musicplayer.mainloop()
