from threading import Thread
import affichage
from son import*

class music(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True :                   ##Si la musique se termine, la relance
            try:
                initMixer()             ##Lance la musique
                pmusic(file)
            except KeyboardInterrupt:  # to stop playing, press "ctrl-c"
                stopmusic()
                print("\nPlay Stopped by user")
                break
            except Exception:
                print("unknown error")

thM=music()
thM.start()
affichage_grille()




