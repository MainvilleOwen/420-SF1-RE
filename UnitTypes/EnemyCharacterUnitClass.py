import pygame
import random

from UnitTypes.CharacterUnitClass import CharacterUnit

class EnemyCharacterUnit(CharacterUnit):
    def __init__(self, name:str, spritesheet:object, spriteIndex:int, reach:int, power:int, critChance:int, critDamage:int, health:int, speed:int, defense:int):
        super().__init__(name, spritesheet, spriteIndex, reach, power, critChance, critDamage, health, speed, defense, team=1, isAlive=True)

    def Move():
        pass

    def ChooseAction():
        pass

    def Act(self):
        pass