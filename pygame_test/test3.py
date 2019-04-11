import pygame_test
import time
import sys

pygame_test.init()

write= 0,255,255

display_weigth = 1920
display_heigth = 1200

gameExit = False

window = pygame_test.display.set_mode((display_weigth, display_heigth))
pygame_test.display.set_caption('my game')


blackgroud = pygame_test.image.load('C:/Users/吴泽良/Pictures/Saved Pictures/002.jpg')
show = blackgroud.get_rect()

window.fill(write)
window.blit(blackgroud,show)

pygame_test.display.flip()
