import pygame
import random

from UnitTypes.CharacterUnitClass import CharacterUnit

class PlayerCharacterUnit(CharacterUnit):
    def __init__(self, name:str, spritesheet:object, spriteIndex:int, reach:int, power:int, critChance:int, critDamage:int, health:int, speed:int, defense:int):
        """
        Create a player-controlled unit.
        Args:
            name (str): Unit name.
            spritesheet (Surface): Sprite sheet for the unit.
            spriteIndex (int): Index of sprite in sheet.
            reach (int): Attack range.
            power (int): Attack power.
            critChance (int): Critical hit chance.
            critDamage (int): Critical damage multiplier.
            health (int): Unit health.
            speed (int): Movement range.
            defense (int): Defense value.
        """

        self.team = 0
        self.isAlive = True
        super().__init__(name, spritesheet, spriteIndex, reach, power, critChance, critDamage, health, speed, defense, self.team, self.isAlive)

    def CheckAvailableTiles(self, tileMap):
        return [tile for tile in self.tile.GetTilesInReach(tileMap) if not tile.IsOccupied]
        