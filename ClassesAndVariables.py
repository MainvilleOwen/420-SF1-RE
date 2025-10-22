import pygame

import SpriteInfo as SI

heightChangeOfSelectedTile = 3
containedSpritesYOffset = 32
containedSpritesXOffset = 17

def InitializeScreen():
    pygame.init()
    global screen
    global screenWidth
    global screenHeight
    screen = pygame.display.set_mode((0, 0))
    screenWidth, screenHeight = screen.get_width(), screen.get_height()


class Tile:
    def __init__(self, sprite, interactable=False):
        self.sprite = sprite
        self.interactable = interactable
        self.containedSprites = []

    def TestSpriteAddition(self, sprite):
        self.containedSprites.append(sprite)

    def Blit(self, screen, x, y, selected=False, selectable=False, addedSprites=[]):
        heightChangeOfSelectedTile = -3 if selected else 0
        
        if selected:
            screen.blit(SI.tileSelectedConversion[self.sprite] if selectable else SI.tileUnselectableConversion[self.sprite], (x, y - heightChangeOfSelectedTile))
        else:
            screen.blit(self.sprite, (x, y))

        for item in self.containedSprites:
            screen.blit(item, (x + containedSpritesXOffset, y - heightChangeOfSelectedTile - containedSpritesYOffset))

        for item in addedSprites:
            screen.blit(item, (x + containedSpritesXOffset, y - heightChangeOfSelectedTile - containedSpritesYOffset))

def makeTileInteractable(sprite):
    return(Tile(sprite, True))

def makeTileUninteractable(sprite):
    return(Tile(sprite))




class Character:
    def __init__(self, sprite, interactable):
        self.sprite = sprite
        self.interactable = interactable


