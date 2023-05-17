from tkinter import filedialog
from tkinter import *
import pygame
import os
import numpy as np

root=Tk()
root.title("Muisc Player")
root.geometry("1000x600")
pygame.mixer.init()

menubar=Menu(root)
root.config(menu=menubar)

arr=np.array([x for x in range(1,21)])
np.random.shuffle(arr)
songs=[]
songs.extend(arr)
paused=False
current_song=0
count=0
def play_music():
    global current_song,paused,count

    if not paused:
        pygame.mixer.music.load('songs/'+str(songs[current_song])+'.mp3')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused=False

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused=True

def next_music():
   global current_song,paused ,count
   if count%20==0:
       np.random.shuffle(arr)
       songs.extend(arr)
   current_song=current_song+1
   pygame.mixer.music.load('songs/' + str(songs[current_song]) + '.mp3')
   pygame.mixer.music.play()

def prev_music():
    global current_songs, paused
    try:
        current_song = current_song-1
        pygame.mixer.music.load('songs/' + str(songs[current_song]) + '.mp3')
        pygame.mixer.music.play()
        paused=False
    except:
        pass


list=Listbox(root, bg="black",fg="white",height=16,width=50)
list.pack()

pause_button=PhotoImage(file='pause.png')
play_button=PhotoImage(file='play.png')
previous_button=PhotoImage(file='previous.png')
next_button=PhotoImage(file='next.png')

control_frame=Frame(root)
control_frame.pack()
previous_btn=Button(control_frame,image=previous_button,borderwidth=0, command=prev_music)
previous_btn.grid(row=0,column=0,padx=7,pady=10)
play_btn=Button(control_frame,image=play_button,borderwidth=0, command=play_music)
play_btn.grid(row=0,column=1,padx=7,pady=10)
pause_btn=Button(control_frame,image=pause_button,borderwidth=0, command=pause_music)
pause_btn.grid(row=0,column=2,padx=7,pady=10)
next_btn=Button(control_frame,image=next_button,borderwidth=0, command=next_music)
next_btn.grid(row=0,column=3,padx=7,pady=10)


root.mainloop()