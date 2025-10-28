import pygame
import random

def InitializeScreen():
    pygame.init()
    global screen
    global screenWidth
    global screenHeight
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    screenWidth, screenHeight = screen.get_width(), screen.get_height()