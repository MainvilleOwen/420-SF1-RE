import pygame
import random

from TileClassAndOperations.TileClass import Tile

class Unit:
    def __init__(self, name:str, spritesheet:pygame.surface, sprite:pygame.surface, reach:int, power:int, critChance:int, critDamage:int, team:int):
# Name that will be shown when Unit is selected
        self.name = name

# Spritesheet of unit
        self.spritesheet = spritesheet
# Current sprite used by the unit
        self.sprite = spritesheet
        self.heightOfSprite = self.sprite.get_height()

        self.facingLeft = True
        self.facingFront = True

# How far the unit can attack
        self.reach = reach

# How powerful the unit's attack is
        self.power = power

# How likely the unit is to deal extra damage with their attack
        self.critChance = critChance

# How much extra damage the unit will deal if they
        self.critDamage = critDamage

# The team of the unit. 0 for player, 1 for enemyTeam1, etc.
        self.team = team



        self.tile = None


    def Act(self, tileMap):
        pass

    def Attack(self, target):
        chance = random.randint(1, 100)
        if chance > target.defense:
            pass

    def DealDamageTo(self, target:object):
        chance = random.randint(1,100)

        totalDamage = self.power

        if chance <= self.critChance:
            totalDamage += self.critDamage

        target.TakeDamage(totalDamage)
        if not target.CheckForLife():
            target.KillSelf()
        
    def Blit(self, screen:pygame.surface, x:int, y:int):
        screen.blit(self.sprite, (x, y - self.heightOfSprite + 32))

    def FaceLeft(self):
        if not self.facingLeft:
            self.sprite = pygame.transform.flip(self.sprite, True, False)
            return True
        return False
    
    def FaceRight(self):
        if self.facingLeft:
            self.sprite = pygame.transform.flip(self.sprite, True, False)
            return True
        return False
    
    def FaceFront(self):
        if not self.facingFront:
            pass