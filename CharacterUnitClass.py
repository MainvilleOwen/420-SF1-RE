import pygame
import random

from UnitClass import Unit

class CharacterUnit(Unit):
    def __init__(self, name:str, spritesheet:pygame.surface, sprite:pygame.surface, reach:int, power:int, critChance:int, critDamage:int, health:int, speed:int, defense:int):
        super().__init__(name, spritesheet, sprite, reach, power, critChance, critDamage)
        self.health = health
        self.maxHealth = health

        self.speed = speed
        # How likely the unit is to dodge (RandInt generated, if it is higher than this the attack hits) AND how much damage they will ignore (% of the number?)
        self.defense = defense

    def TakeDamage(self, damage):
        self.health = max(0, self.health - damage)
        return(damage)

    def CheckForLife(self):
        return(self.health)
    
    def KillSelf(self):
        """self.sprite = Prone Sprite"""
        self.isAlive = False

    def DoMovingAnimation(self, target):
        """Move towards target tile gradually somehow?"""
        pass