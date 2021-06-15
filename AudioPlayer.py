
import pygame
import tkinter as tkr
import os

app = tkr.Tk()
app.title("Luke's Audio Player")
app.geometry("300x400")

"""get song"""

os.chdir("MoreSongs")
print(os.getcwd)
songlist = os.listdir()

"""playlist input"""

playlist = tkr.Listbox(app,highlightcolor="red",selectmode = tkr.SINGLE)
print(songlist)
for item in songlist:
	pos = 0
	playlist.insert(pos, item)
	pos = pos + 1

"""Action Event"""

def Play():
	pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
	var.set(playlist.get(tkr.ACTIVE))
	pygame.mixer.music.play()

def ExitPlayer():
		pygame.mixer.music.stop()

def Pause():
		pygame.mixer.music.pause()

def Unpause():
		pygame.mixer.music.unpause()


"""Register Buttons"""
button1 = tkr.Button(app,width=5,height=3, text="PLAY",command=Play)
button2 = tkr.Button(app,width=5,height=3, text="STOP",command=ExitPlayer)
button3 = tkr.Button(app,width=5,height=3, text="PAUSE",command=Pause)
button4 = tkr.Button(app,width=5,height=3, text="UNPAUSE",command=Unpause)

"""Song Name"""
var = tkr.StringVar()
songtitle = tkr.Label(app,textvariable=var)

"""Pygame Inits"""
pygame.init()
pygame.mixer.init()

"""Place Widgets"""
songtitle.pack()
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
playlist.pack(fill="both", expand="yes")

"""Activate"""
app.mainloop()

