import pygame
import random


from TileClassAndOperations.TileClass import Tile

class Unit:
    def __init__(self, name:str, spritesheet:object, spriteIndex:int, reach:int, power:int, critChance:int, critDamage:int, team:int):
# Name that will be shown when Unit is selected
        self.name = name

# Spritesheet of unit
        self.spritesheet = spritesheet
# Current sprite used by the unit
        self.baseIndex = spriteIndex
        self.spriteIndex = self.baseIndex

        self.facingLeft = True
        self.facingFront = True

        self.heightOfSprite = self.spritesheet.GetSprite(self.spriteIndex, (not self.facingLeft)).get_height()

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
        self.displayTile = None


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
        screen.blit(self.spritesheet.GetSprite(self.spriteIndex, (not self.facingLeft)), (x, y - self.heightOfSprite + 32))

    def FaceLeft(self):
        return True
    
    def FaceRight(self):
        return False
    
    def FaceFront(self):
        if not self.facingFront:
            if self.baseIndex > 2:
                self.baseIndex -= 3
            return True
        return True
        
    def FaceBack(self):
        if self.facingFront:
            if self.baseIndex < 3:
                self.baseIndex += 3
            return False
        return False

    def Rotate(self, clockwise:bool):
        if clockwise:
            if self.facingLeft:
                if self.facingFront: self.facingFront = self.FaceBack()
                else: self.facingLeft = self.FaceRight()

            else:
                if self.facingFront: self.facingLeft = self.FaceLeft()
                else: self.facingFront = self.FaceFront()

        elif not clockwise:
            if self.facingLeft:
                if self.facingFront: self.facingLeft = self.FaceRight()
                else: self.facingFront = self.FaceFront()

            else:
                if self.facingFront: self.facingLeft = self.FaceLeft()
                else: self.facingFront = self.FaceBack()

    def SetSprite(self, index:int):
        self.spriteIndex = index