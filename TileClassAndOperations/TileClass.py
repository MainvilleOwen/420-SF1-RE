import pygame
import Sprites.SpriteInfo as SI

# Each Tile in the tilemap is its own object
class Tile:
    def __init__(self, sprite:pygame.Surface, walkable:bool=True):
        """
        Initialize a Tile object.
        Args:
            sprite (pygame.Surface): Image of the tile.
            walkable (bool): Whether units can walk on this tile.
        """
# The image of the sprite
        self.sprite = sprite
# If the sprite can be walked on by units
        self.walkable = walkable

# If the tile contains any terrain elements, like trees or bushes or rocks, it will be stored here
        self.terrain = None

# If the tile currently has a unit on it, the object of that unit will be stored here
        self.unit = None
        self.displayUnit = None

# x, y, z position of tile (THESE ARE INDEX COORDINATES)
        self.x, self.y, self.z = None, None, None
        self.yOffset = 0
    

    def BlitWhite(self, screen:pygame.Surface, x:int, y:int, WTVX=None, WTVY=None):
        """
        Draw the tile in white (highlighted) on screen.
        Args:
            screen (pygame.Surface): The surface to draw on.
            x (int), y (int): Screen coordinates.
            WTVX, WTVY: Optional world-to-view functions for unit positioning.
        """
        heightChangeFactor = -2

        if self.walkable:

            screen.blit(SI.tileSelectedConversion[self.sprite], (x, y + self.yOffset + heightChangeFactor))

            if self.displayUnit and self.displayUnit.displayTile == self:
                if WTVX and WTVY:
                    unitTileX, unitTileY = WTVX(self.displayUnit.tile.x, self.displayUnit.tile.y), WTVY(self.displayUnit.tile.x, self.displayUnit.tile.y, self.displayUnit.tile.z)
                else:
                    unitTileX, unitTileY = x, y
                
                self.displayUnit.Blit(screen, unitTileX + (self.sprite.get_width() // 2) - (self.displayUnit.spritesheet.spriteWidth // 2), unitTileY)

        else:
            screen.blit(SI.tileUnselectableConversion[self.sprite], (x, y + self.yOffset + heightChangeFactor))

            if self.terrain:
                screen.blit(self.terrain, (x, y + heightChangeFactor))

    def BlitRed(self, screen:pygame.Surface, x:int, y:int, WTVX=None, WTVY=None):
        """
        Draw the tile in red (unwalkable/highlighted) on screen.
        Args: same as BlitWhite.
        """
        heightChangeFactor = 0
        screen.blit(SI.tileUnselectableConversion[self.sprite], (x, y + self.yOffset + heightChangeFactor))

        if self.terrain:
            screen.blit(self.terrain, (x, y + heightChangeFactor))

        if self.displayUnit and self.displayUnit.displayTile == self:
            if WTVX and WTVY:
                unitTileX, unitTileY = WTVX(self.displayUnit.tile.x, self.displayUnit.tile.y), WTVY(self.displayUnit.tile.x, self.displayUnit.tile.y, self.displayUnit.tile.z)
            else:
                unitTileX, unitTileY = x, y
                
            self.displayUnit.Blit(screen, unitTileX + (self.sprite.get_width() // 2) - (self.displayUnit.spritesheet.spriteWidth // 2), unitTileY)
            
    def BlitBlue(self, screen:pygame.Surface, x:int, y:int, WTVX=None, WTVY=None):
        """
        Draw the tile in blue (movement range) on screen.
        Args: same as BlitWhite.
        """
        heightChangeFactor = 0
        screen.blit(SI.tileBlueConversion[self.sprite], (x, y + self.yOffset + heightChangeFactor))

        if self.terrain:
            screen.blit(self.terrain, (x, y + heightChangeFactor))

        if self.displayUnit and self.displayUnit.displayTile == self:
            if WTVX and WTVY:
                unitTileX, unitTileY = WTVX(self.displayUnit.tile.x, self.displayUnit.tile.y), WTVY(self.displayUnit.tile.x, self.displayUnit.tile.y, self.displayUnit.tile.z)
            else:
                unitTileX, unitTileY = x, y
                
            self.displayUnit.Blit(screen, unitTileX + (self.sprite.get_width() // 2) - (self.displayUnit.spritesheet.spriteWidth // 2), unitTileY)

    def Blit(self, screen:pygame.Surface, x:int, y:int, WTVX=None, WTVY=None):
        """
        Draw the tile normally (no color highlight) on screen.
        Args: same as BlitWhite.
        """
        screen.blit(self.sprite, (x, y + self.yOffset))

        if self.terrain:
            screen.blit(self.terrain, (x, y))

        if self.displayUnit and self.displayUnit.displayTile == self:
            if WTVX and WTVY:
                unitTileX, unitTileY = WTVX(self.displayUnit.tile.x, self.displayUnit.tile.y), WTVY(self.displayUnit.tile.x, self.displayUnit.tile.y, self.displayUnit.tile.z)
            else:
                unitTileX, unitTileY = x, y

            self.displayUnit.Blit(screen, unitTileX + (self.sprite.get_width() // 2) - (self.displayUnit.spritesheet.spriteWidth // 2), unitTileY)

# Function that checks if the tile has a unit or a piece of terrain on it
    def TileOccupied(self):
        """
        Check if the tile has a unit or terrain.
        Returns:
            bool: True if occupied, False otherwise.
        """
        return (self.unit or self.terrain)
    
# Function that assigns a unit to a tile (LOGIC WISE AND VISUAL WISE)
    def OccupyTile(self, unit:object):
        """
        Assign a unit to the tile both logically and visually.
        Args:
            unit (object): Unit to occupy the tile.
        Returns:
            bool: True if successfully occupied, False otherwise.
        """
        if self.TileOccupied() or not self.walkable:
            return False
        
        self.unit = unit
        self.displayUnit = unit

        unit.tile = self
        unit.displayTile = self
        return True
    
    def UnOccupyTile(self):
        """
        Remove a unit from the tile both logically and visually.
        """
        if self.unit:
            self.unit.tile = None
            self.unit.displayTile = None

            self.unit = None
            self.displayUnit = None

    def AssignUnitVisually(self, unit:object):
        """
        Assign unit visually without affecting logical occupancy.
        Args:
            unit (object): Unit to assign visually.
        """
        self.displayUnit = unit
        unit.displayTile = self

    def UnAssignUnitVisually(self):
        """
        Remove visual assignment of a unit from this tile.
        """
        self.displayUnit.displayTile = None
        self.displayUnit = None

    def AssignUnitLogically(self, unit:object):
        """
        Assign unit logically without affecting visuals.
        Args:
            unit (object): Unit to assign logically.
        """
        self.unit = unit
        unit.tile = self

    def UnAssignUnitLogically(self):
        """
        Remove logical assignment of a unit from this tile.
        """
        self.unit.tile = None
        self.unit = None

# Function that returns the Adjacent Tiles of the tile object it is called on.
    def GetAdjacentTiles(self, tileMap:object):
        """
        Get all walkable adjacent tiles in 3D space.
        Args:
            tileMap (object): TileMap instance containing tiles.
        Returns:
            list: Adjacent walkable Tile objects.
        """
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
        """
        Get all tiles within movement or ability range.
        Args:
            tileMap (object): TileMap instance.
            reach (int): Range in tiles.
        Returns:
            dict: Tiles mapped to their parent tiles for path reconstruction.
        """

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
        
    def ReconstructPath(self, tileParents:dict):
        """
        Reconstruct path from parent dictionary.
        Args:
            tileParents (dict): Mapping of tiles to their parent tiles.
        Returns:
            list: Tiles in path from start to target.
        """
        path = []
        targetTile = self
        
        while targetTile in tileParents and tileParents[targetTile]:
            path.append(targetTile)
            targetTile = tileParents[targetTile]

        path.reverse() # So we can go from start to target instead of going backwards. Looping over the tiles is now way easier because it goes forwards
        return path

def MakeTileWalkable(sprite:pygame.Surface):
    """
    Create a walkable tile.
    Args:
        sprite (pygame.Surface): Tile image.
    Returns:
        Tile: Walkable Tile object.
    """
    return(Tile(sprite))

def MakeTileUnWalkable(sprite:pygame.Surface):
    """
    Create an unwalkable tile.
    Args:
        sprite (pygame.Surface): Tile image.
    Returns:
        Tile: Unwalkable Tile object.
    """
    return(Tile(sprite, False))

