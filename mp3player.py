from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def _init_(self, window ):
        window.geometry('720x1080'); window.title('Iris Player'); window.resizable(0,0)
        Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), bg =('blue'),command = self.load)
        Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), bg =('green'),command = self.play)
        Pause = Button(window,text = 'Pause',  width = 10, font = ('Times', 10), bg =('yellow'), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 10, font = ('Times', 10),bg =('orange'), command = self.stop)
        Load.place(x=300,y=620);Play.place(x=300,y=820);Pause.place(x=300,y=1020);Stop.place(x=300,y=1220) 
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
root = Tk()
app= MusicPlayer(root)
root.mainloop()
