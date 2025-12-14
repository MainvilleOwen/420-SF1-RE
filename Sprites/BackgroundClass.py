import pygame

import Sprites.SpriteInfo as SI
import ScreenAndClock as S

class BackgroundClass:
    def __init__(self, sprite:pygame.Surface):
        """
        Create a background object with an initial sprite.
        Args:
            sprite (pygame.Surface): Background image.
        """

        self.sprite = sprite

    def ResizeBackground(self):
        """
        Resize the background sprite to match the current screen size.
        Returns:
            None
        """

        self.sprite = pygame.transform.scale(SI.BackgroundSprite, (S.screenWidth, S.screenHeight))

    def ClearScreen(self):
        """
        Clear the screen by drawing the background.
        Returns:
            None
        """
        
        self.ResizeBackground()
        S.screen.blit(self.sprite, (0,0))

    def ChangeBackground(self, sprite:pygame.Surface):
        """
        Change the background sprite.
        Args:
            sprite (pygame.Surface): New background image.
        Returns:
            None
        """

        self.sprite = sprite

def CreateBackground(sprite:pygame.Surface):
    """
    Create and store a global background object.
    Args:
        sprite (pygame.Surface): Background image.
    Returns:
        None
    """
    global Background
    Background = BackgroundClass(sprite)