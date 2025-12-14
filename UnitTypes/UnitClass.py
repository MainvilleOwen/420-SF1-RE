import pygame
import random


from TileClassAndOperations.TileClass import Tile

class Unit:
    def __init__(self, name:str, spritesheet:object, spriteIndex:int, reach:int, power:int, critChance:int, critDamage:int, team:int):
        """
        Create a base unit with stats, sprite data, and team ownership.
        Args:
            name (str): Name of the unit.
            spritesheet (object): Spritesheet used to render the unit.
            spriteIndex (int): Default sprtesheet index
            reach (int): Attack range.
            power (int): Base attack power.
            critChance (int): Chance to deal critical damage.
            critDamage (int): Bonus damage on critical hit.
            team (int): Team ID (0 = player, 1+ = enemies).
        """

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


    def Attack(self, target):
        """
        Unused
        """
        chance = random.randint(1, 100)
        if chance > target.defense:
            pass

    def DealDamageTo(self, target:object):
        """
        Unused
        """
        chance = random.randint(1,100)

        totalDamage = self.power

        if chance <= self.critChance:
            totalDamage += self.critDamage

        target.TakeDamage(totalDamage)
        if not target.CheckForLife():
            target.KillSelf()
        
    def Blit(self, screen:pygame.surface, x:int, y:int):
        """
        Draw the unit sprite to the screen.
        Args:
            screen (Surface): Pygame screen surface.
            x (int): X screen position.
            y (int): Y screen position.
        Returns:
            None
        """
        screen.blit(self.spritesheet.GetSprite(self.spriteIndex, (not self.facingLeft)), (x, y - self.heightOfSprite + 32))

# Group of functions to rotate the unit. They return the value you woant self.facingLeft or self.facingFront to be
# The Front and Back ones offset the default sprite index so that it returns the backwards ones
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
        """
        Rotate the unit's facing direction.
        Args:
            clockwise (bool): True to rotate clockwise, False otherwise.
        Returns:
            None
        """

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
        """
        Set the current sprite index.
        Args:
            index (int): New sprite index.
        Returns:
            None
        """
        
        self.spriteIndex = index