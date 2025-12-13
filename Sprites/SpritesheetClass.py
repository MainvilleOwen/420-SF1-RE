import pygame

class Spritesheet:
    def __init__(self, spritesheet:pygame.Surface, spriteWidth:int):
        self.spritesheet = spritesheet
        self.height = spritesheet.get_height()
        self.width = spritesheet.get_width()

        self.spriteWidth = spriteWidth
        self.amountOfSprites = self.width//self.spriteWidth

        self.memory = {}

    def GetSprite(self, index:int, flipped:bool=False):
        startingPixelX = index * self.spriteWidth

        if index < 0 or index >= self.amountOfSprites: return None

        if (index, flipped) in self.memory:
            return self.memory[(index, flipped)]

        sprite = pygame.Surface((self.spriteWidth, self.height), pygame.SRCALPHA)
        sprite.blit(self.spritesheet, (0, 0), (startingPixelX, 0, self.spriteWidth, self.height))

        if flipped: sprite = pygame.transform.flip(sprite, True, False)

        self.memory[(index, flipped)] = sprite
        
        return sprite
