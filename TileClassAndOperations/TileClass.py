import pygame
import SpriteInfo as SI

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

        if self.unit:
            self.unit.Blit(screen, x + (self.sprite.get_width())//4, y + heightChangeFactor)


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

# Function that returns the Adjacent Tiles of the tile object it is called on.
    def GetAdjacentTiles(self, tileMap:object):
        adjacentTiles = []

        x, y, z = self.x, self.y, self.z

        xAndYOffsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        zOffsets = [1, 0, -1]

        for xOffset, yOffset in xAndYOffsets:
            for zOffset in zOffsets:

                adjacentTile = tileMap.SafelyGetTile( x + xOffset, y + yOffset, z + zOffset)
                if adjacentTile and adjacentTile.walkable:
                    adjacentTiles.append(adjacentTile)
                    break

        return adjacentTiles
    
# Function that returns any tile within reach of the tile it is called on
# It takes in an int telling it how far in any direction to reach, each +1 is one more tile checked
# Takes in tilemap too since tiles dont store the tileMap they are from.
    def GetTilesInReach(self, tileMap:object, reach:int):

# Add self as the first element of the dictionary with a value of None because it doesnt come from another tile. Then adds it to the queue of tiles to be checked by the GetAdjacentTiles Function
        tilePathOrder = {self: None}
# If the reach is less than 1, we just return this dictionary as is. No other tile can be reached.
        if reach < 1: return tilePathOrder

# If the program continues, we add self to the queue to check the adjacent tiles here first.
        queue = [self]

# The for i in range(reach) makes the loop iterate through itself once for every tile that can be reached out to.
        for i in range(reach):
        
# The queue of tiles that will be checked next. These are added to the queue after it is cleared.
            nextQueue = []

# Runs once for every tile in the queue, giving each one the name referenceTile as they will be the reference to the next ones in the dictionary
            for referenceTile in queue:
#For each adjacent tile to the reference
                for adjacentTile in referenceTile.GetAdjacentTiles(tileMap):

# If the tile has already been checked, previously this step or earlier in another step, we just move on
                    if adjacentTile in tilePathOrder.keys(): continue

# We add the tiles to the nextQueue, and then add it to the returned dictionary with a reference to the tile it was obtained from. This allows for the tracing of the path to get to this tile
                    nextQueue.append(adjacentTile)
                    tilePathOrder[adjacentTile] = referenceTile

# Make the next tiles to check the queue for the next iteration of the loop
            queue = nextQueue

        return(tilePathOrder)
        
    

def MakeTileWalkable(sprite:pygame.Surface):
    return(Tile(sprite))

def MakeTileUnWalkable(sprite:pygame.Surface):
    return(Tile(sprite, False))

