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
    screen = pygame.display.set_mode((0, 0))
    screenWidth, screenHeight = screen.get_width(), screen.get_height()


class Tile:
    def __init__(self, sprite:pygame.Surface, walkable:bool=True):
        self.sprite = sprite
        self.walkable = walkable

        self.terrain = None
        self.unit = None

    def TestSpriteAddition(self, sprite:pygame.Surface):
        self.unit = sprite

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

    def IsTileOppupied(self):
        return True if (self.unit or self.terrain) else False
    
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
        self.name = name
        self.sprite = sprite

        self.range = range
        self.power = power
        self.defense = defense
        self.critChance = critChance
        self.critDamage = critDamage

        self.alive = True

        self.tile = None
        self.screenPosition = None

        def Blit(self, screen, x, y):
            screen.blit(self.sprite, (x, y))

        def Act(self):
            pass

class MovingUnit(Unit):
    def __init__(self, name:str, sprite:pygame.surface, range:int, power:int, defense:int, critChance:int, critDamage:int, health:int, speed:int):
        super().__init__(name, sprite, range, power, defense, critChance, critDamage)
        self.health = health
        self.speed = speed
        self.targetTile = None

        def setTargetTile(self, target):
            self.targetTile = target

        def moveTowardsTile(self, target):
            if self.tile != self.targetTile:
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

    def takeDamage(self, damage):
        self.health = max(0, self.health - damage)

    def dealDamage(self, target):
        chance = random.randint(1,100)
        target.takeDamage(self.power + self.critDamage) if (chance <= self.critChance) else target.takeDamage(self.power)