"""Audio Player in Python"""
"""Import Modules"""
import pygame
import tkinter as tkr
import os

"""Create Window"""
player = tkr.Tk()

"""Edit Window"""
player.title("Audio Player")
player.geometry("305x470")



"""Playlist Register"""
os.chdir("MoreSongs")
print(os.getcwd)
songlist = os.listdir()


"""playlist input"""

playlist = tkr.Listbox(player,highlightcolor="red",selectmode = tkr.SINGLE)
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

#player.blit(background_image, [0, 0])

"""Register Buttons"""
button1 = tkr.Button(player,width=5,height=3, text="PLAY",command=Play)
button2 = tkr.Button(player,width=5,height=3, text="STOP",command=ExitPlayer)
button3 = tkr.Button(player,width=5,height=3, text="PAUSE",command=Pause)
button4 = tkr.Button(player,width=5,height=3, text="UNPAUSE",command=Unpause)
#background_image = pygame.image.load("profile_sans_bg.jpeg")

"""Song Name"""
var = tkr.StringVar()
songtitle = tkr.Label(player,textvariable=var)


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
player.mainloop()