import pygame
import SpriteInfo as SI


heightChangeOfSelectedTile = 3
containedSpritesYOffset = 32
containedSpritesXOffset = 17

# Each Tile in the tilemap is its own object
class Tile:
    def __init__(self, sprite:pygame.Surface, walkable:bool=True):
# The image of the sprite
        self.sprite = sprite
# If the sprite can be walked on by units
        self.walkable = walkable

# If the tile contains any terrain elements, like trees or bushes or rocks, it will be stored here
        self.terrain = None

# If the tile currently has a unit on it, the object of that unit will be stored here
        self.unit = None

    def TestSpriteAddition(self, sprite:pygame.Surface):
        self.unit = sprite if not self.TileOccupied() else self.unit

    def Blit(self, screen:pygame.Surface, x:int, y:int, selected:bool=False, selectable:bool=False):
        heightChangeOfSelectedTile = -3 if selected else 0
        
        if selected:
            screen.blit(SI.tileSelectedConversion[self.sprite] if selectable else SI.tileUnselectableConversion[self.sprite], (x, y - heightChangeOfSelectedTile))
        else:
            screen.blit(self.sprite, (x, y))

        if self.terrain:
            screen.blit(self.terrain, (x + containedSpritesXOffset, y - heightChangeOfSelectedTile - containedSpritesYOffset))

        if self.unit:
            screen.blit(self.unit, (x + containedSpritesXOffset, y - heightChangeOfSelectedTile - containedSpritesYOffset))

# Function that checks if the tile has a unit or a piece of terrain on it
    def TileOccupied(self):
        return True if (self.unit or self.terrain) else False
    
# Function that assigns a unit onto a tile
    def OccupyTile(self, unit):
        if self.isTileOccupied(self) or not self.walkable:
            return False
        self.unit = unit
        unit.tile = self
        return True
    
    def UnOccupyTile(self):
        if self.unit:
            self.unit.tile = None
            self.tile = None

def makeTileWalkable(sprite):
    return(Tile(sprite))

def makeTileUnWalkable(sprite):
    return(Tile(sprite, False))

