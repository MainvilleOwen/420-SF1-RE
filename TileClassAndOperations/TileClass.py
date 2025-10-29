import pygame
import SpriteInfo as SI
import Screen as S

from TileClassAndOperations.TileOperations import SafelyGetTile

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

        self.x, self.y, self.z = None, None, None

    def BlitWhite(self, screen:pygame.Surface, x:int, y:int):
        heightChangeFactor = -2

        if self.walkable:

            screen.blit(SI.tileSelectedConversion[self.sprite], (x, y + heightChangeFactor))

            if self.unit:
                self.unit.Blit(screen, x + (self.sprite.get_width())//4, y + heightChangeFactor)

        else:
            screen.blit(SI.tileUnselectableConversion[self.sprite], (x, y + heightChangeFactor))

            if self.terrain:
                screen.blit(self.terrain, (x, y + heightChangeFactor))

    def BlitRed(self, screen:pygame.Surface, x:int, y:int):
        heightChangeFactor = 0
        screen.blit(SI.tileUnselectableConversion[self.sprite], (x, y + heightChangeFactor))

        if self.terrain:
            screen.blit(self.terrain, (x, y + heightChangeFactor))


    def Blit(self, screen:pygame.Surface, x:int, y:int):
        screen.blit(self.sprite, (x, y))

        if self.terrain:
            screen.blit(self.terrain, (x, y))

        if self.unit:
            self.unit.Blit(screen, x + (self.sprite.get_width())//4, y)

# Function that checks if the tile has a unit or a piece of terrain on it
    def TileOccupied(self):
        return (self.unit or self.terrain)
    
# Function that assigns a unit onto a tile
    def OccupyTile(self, unit:object):
        if self.TileOccupied() or not self.walkable:
            return False
        self.unit = unit
        unit.tile = self
        return True
    
    def UnOccupyTile(self):
        if self.unit:
            self.unit.tile = None
            self.unit = None

    def GetAdjacentTiles(self, tileMap):
        adjacentTiles = []

        x, y, z = self.x, self.y, self.z

        xAndYOffsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        zOffsets = [1, 0, -1]

        for xOffset, yOffset in xAndYOffsets:

            for zOffset in zOffsets:
                adjacentTile = SafelyGetTile(tileMap, x + xOffset, y + yOffset, z + zOffset)
                if adjacentTile and adjacentTile.walkable:
                    adjacentTiles.append(adjacentTile)
                    break

        return adjacentTiles
    
# Function that returns any tile within reach of the tile it is called on
# It takes in an int telling it how far in any direction to reach, each +1 is one more tile checked
# Takes in tilemap too since tiles dont store the tileMap they are from.
    def GetTilesInReach(self, tileMap:list, reach:int):
# Add self as the first element of the dictionary with a value of None because it didnt 
        tilePathOrder = {self: None}
        queue = [self]

        if reach < 1: return tilePathOrder

        for i in range(reach):
            nextQueue = []

            for referenceTile in queue:
                for adjacentTile in referenceTile.GetAdjacentTiles(tileMap):
                    if adjacentTile in tilePathOrder.keys(): continue

                    nextQueue.append(adjacentTile)
                    tilePathOrder[adjacentTile] = referenceTile

            queue = nextQueue

        return(tilePathOrder)
        
    

def MakeTileWalkable(sprite):
    return(Tile(sprite))

def MakeTileUnWalkable(sprite):
    return(Tile(sprite, False))

