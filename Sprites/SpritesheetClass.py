import pygame

class Spritesheet:
    def __init__(self, spritesheet:pygame.Surface, spriteWidth:int):
        """
        Store a spritesheet and split it into individual sprites.
        Args:
            spritesheet (pygame.Surface): Full spritesheet image.
            spriteWidth (int): Width of one sprite in pixels.
        """

        self.spritesheet = spritesheet
        self.height = spritesheet.get_height()
        self.width = spritesheet.get_width()

        self.spriteWidth = spriteWidth
        self.amountOfSprites = self.width//self.spriteWidth

        self.memory = {}

    def GetSprite(self, index:int, flipped:bool=False):
        """
        Extract and return a single sprite from the spritesheet.
        Args:
            index (int): Index of the sprite.
            flipped (bool): Whether the sprite is horizontally flipped.
        Returns:
            pygame.Surface or None: The requested sprite, or None if invalid index.
        """
        
        startingPixelX = index * self.spriteWidth

        if index < 0 or index >= self.amountOfSprites: return None

        if (index, flipped) in self.memory:
            return self.memory[(index, flipped)]

        sprite = pygame.Surface((self.spriteWidth, self.height), pygame.SRCALPHA)
        sprite.blit(self.spritesheet, (0, 0), (startingPixelX, 0, self.spriteWidth, self.height))

        if flipped: sprite = pygame.transform.flip(sprite, True, False)

        self.memory[(index, flipped)] = sprite
        
        return sprite
