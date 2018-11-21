import pygame


def pmusic(file):                               ##Joue la musique de Tetris et attend la fin avant de sortir de la fonction
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():

        clock.tick(1000)

def stopmusic():                        ##arrête la musique
    pygame.mixer.music.stop()


def getmixerargs():                         ##Prend les variables du mixeur
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan


def initMixer():                ##Initialisation du mixeur de pygame
    BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)

