import pygame
import random

from UnitTypes.CharacterUnitClass import CharacterUnit

class PlayerCharacterUnit(CharacterUnit):
    def __init__(self, name:str, spritesheet:pygame.surface, sprite:pygame.surface, reach:int, power:int, critChance:int, critDamage:int, health:int, speed:int, defense:int, team:int):
        super().__init__(name, spritesheet, sprite, reach, power, critChance, critDamage, health, speed, defense, team)

    def Move():
        pass

    def ChooseAction():
        pass

    def Act(self):
        pass