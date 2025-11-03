import pygame

import SpriteInfo as SI
import ScreenAndClock as S

class BackgroundClass:
    def __init__(self, sprite):
        self.sprite = sprite

    def ResizeBackground(self):
        self.sprite = pygame.transform.scale(SI.BackgroundSprite, (S.screenWidth, S.screenHeight))

    def ClearScreen(self):
        self.ResizeBackground()
        S.screen.blit(self.sprite, (0,0))

    def ChangeBackground(self, sprite:pygame.Surface):
        self.sprite = sprite

def CreateBackground(sprite):
    global Background
    Background = BackgroundClass(sprite)