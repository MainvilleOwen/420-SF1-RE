import pygame
import random

import SpriteInfo as SI

heightChangeOfSelectedTile = 3
containedSpritesYOffset = 32
containedSpritesXOffset = 17

def InitializeScreen():
    pygame.init()
    global screen
    global screenWidth
    global screenHeight
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    screenWidth, screenHeight = screen.get_width(), screen.get_height()

class BackgroundClass:
    def __init__(self, sprite):
        self.sprite = sprite

    def ResizeBackground(self):
        self.sprite = pygame.transform.scale(SI.BackgroundSprite, (screenWidth, screenHeight))

    def ClearScreen(self):
        self.ResizeBackground()
        screen.blit(self.sprite, (0,0))

    def ChangeBackground(self, sprite:pygame.Surface):
        self.sprite = sprite

def CreateBackground(sprite):
    global Background
    Background = BackgroundClass(sprite)

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




class Unit:
    def __init__(self, name:str, sprite:pygame.surface, range:int, power:int,  defense:int, critChance:int, critDamage:int):
# Name that will be shown when Unit is selected
        self.name = name

# Spritesheet of unit
        self.sprite = sprite

# How far the unit can attack
        self.range = range

# How powerful the unit's attack is
        self.power = power

# How likely the unit is to dodge (RandInt generated, if it is higher than this the attack hits) AND how much damage they will ignore (% of the number?)
        self.defense = defense

# How likely the unit is to deal extra damage with their attack
        self.critChance = critChance

# How much extra damage the unit will deal if they
        self.critDamage = critDamage

# If the unit still has health left
        self.alive = True

        self.tile = None

        def Act(self):
            pass

class MovingUnit(Unit):
    def __init__(self, name:str, sprite:pygame.surface, range:int, power:int, defense:int, critChance:int, critDamage:int, health:int, speed:int):
        super().__init__(name, sprite, range, power, defense, critChance, critDamage)
        self.health = health
        self.speed = speed

        def setTargetTile(self, target):
            self.targetTile = target

        def moveTowardsTile(self, target:object):
            if self.tile != self.targetTile:
                self.targetTile = target

        def takeDamage(self, damage):
            self.health = max(0, self.health - damage)

        def dealDamage(self, target):
            chance = random.randint(1,100)
            target.takeDamage(self.power + self.critDamage) if (chance <= self.critChance) else target.takeDamage(self.power)

        def DoMovingAnimation(self, target):
            pass
        

class PlayerCharacter(MovingUnit): 
    def __init__(self, health, speed, range, power, critChance, critDamage):
        self.health = health
        self.speed = speed
        self.range = range
        self.power = power
        self.critChance = critChance
        self.critDamage = critDamage

    def move(self):
        pass

    def attack(self):
        pass