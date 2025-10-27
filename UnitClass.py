import pygame
import random

from TileClass import Tile

class Unit:
    def __init__(self, name:str, spritesheet:pygame.surface, reach:int, power:int, critChance:int, critDamage:int, isAlive=True):
# Name that will be shown when Unit is selected
        self.name = name

# Spritesheet of unit
        self.spritesheet = spritesheet
# Current sprite used by the unit
        self.sprite = None

# How far the unit can attack
        self.reach = reach

# How powerful the unit's attack is
        self.power = power

# How likely the unit is to deal extra damage with their attack
        self.critChance = critChance

# How much extra damage the unit will deal if they
        self.critDamage = critDamage

# If the unit still has health left
        self.isAlive = isAlive

        self.tile = None

    def Act(self):
        pass

    def DealDamage(self, target:object):
        chance = random.randint(1,100)

        totalDamage = self.power

        if chance <= self.critChance:
            totalDamage += self.critDamage

        target.TakeDamage(totalDamage)
        if not target.CheckForLife():
            target.KillSelf()
        