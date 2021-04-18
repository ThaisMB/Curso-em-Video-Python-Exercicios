from pygame import *
mixer.init()
mixer.music.load('rise.mp3')
pygame.mixer.music.play()

while mixer.music.get_busy():
    time.Clock().tick(10)