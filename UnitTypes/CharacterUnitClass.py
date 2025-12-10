import pygame
import random

from UnitTypes.UnitClass import Unit

class CharacterUnit(Unit):
    def __init__(self, name:str, spritesheet:pygame.Surface, sprite:pygame.Surface, reach:int, power:int, critChance:int, critDamage:int, health:int, speed:int, defense:int, team:int, isAlive:bool):
        self.isAlive = isAlive

        super().__init__(name, spritesheet, sprite, reach, power, critChance, critDamage, team)

        self.health = health
        self.maxHealth = health

        self.speed = speed

# How likely the unit is to dodge (RandInt generated, if it is higher than this the attack hits) AND how much damage they will ignore (% of the number?)
        self.defense = defense

# Path and movement logic variables
        self.relativeX, self.relativeY = 0, 0
        self.path = None


    def TakeDamage(self, damage):
        self.health = max(0, self.health - damage)
        return(damage)

    def CheckForLife(self):
        return(self.health)
    
    def KillSelf(self):
        """self.sprite = Prone Sprite"""
        self.isAlive = False

    def SetPath(self, path:list):
        if not self.path and path:
            self.path = path
            return True
        return False

    def UpdateRelativePosition(self, deltaTime, tileMap):
        # Amount of pixels moved per frame (sort of, its like directional pixels not bound by the grid if that makes sense. Distance formula)
        # Change the 4 to speed it up or slow it down
        deltaTime = 1 if deltaTime == 0 else deltaTime
        movedPixels = 4 * deltaTime

        if not self.path or len(self.path) < 1:
            self.tile.OccupyTile(self)
            self.relativeX, self.relativeY = 0, 0
            self.path = None
            return None
        
        nextTile = self.path[0]

        if self.displayTile != nextTile:
            if tileMap.tileDrawOrder.index((self.displayTile.x, self.displayTile.y, self.displayTile.z)) < tileMap.tileDrawOrder.index((nextTile.x, nextTile.y, nextTile.z)):
                self.displayTile.UnAssignUnitVisually()
                nextTile.AssignUnitVisually(self)
        
        currentTileX, currentTileY = tileMap.WorldToViewX(self.tile.x, self.tile.y), tileMap.WorldToViewY(self.tile.x, self.tile.y, self.tile.z)
        nextTileX, nextTileY = tileMap.WorldToViewX(nextTile.x, nextTile.y), tileMap.WorldToViewY(nextTile.x, nextTile.y, nextTile.z)

        distanceX, distanceY = (nextTileX - currentTileX), (nextTileY - currentTileY)

        distance = (distanceX**2 + distanceY**2)**0.5

        xComponent = distanceX/distance
        yComponent = distanceY/distance

        self.relativeX += movedPixels * xComponent
        self.relativeY += movedPixels * yComponent

        # Ok now check if we have reached the tile (or went over because we use an arbitrary number)
        if (self.relativeX**2 + self.relativeY**2)**0.5 >= distance:

            if not self.path:
                self.relativeX, self.relativeY = 0, 0
                return None

            self.tile.UnOccupyTile()
            nextTile.OccupyTile(self)

            self.path.pop(0)

            self.relativeX, self.relativeY = 0, 0

    def MovementCheck(self):
        return True if self.path else False

    def Blit(self, screen:pygame.surface, x:int, y:int):
        screen.blit(self.sprite, (x + self.relativeX, y + self.relativeY - self.heightOfSprite + 32))