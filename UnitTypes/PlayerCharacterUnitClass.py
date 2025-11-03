import pygame
import random

from UnitTypes.CharacterUnitClass import CharacterUnit

class PlayerCharacterUnit(CharacterUnit):
    def __init__(self, name:str, spritesheet:pygame.surface, sprite:pygame.surface, reach:int, power:int, critChance:int, critDamage:int, health:int, speed:int, defense:int, team:int):
        super().__init__(name, spritesheet, sprite, reach, power, critChance, critDamage, health, speed, defense, team)

    def CheckAvailableTiles(self, tileMap):
        return [tile for tile in self.tile.GetTilesInReach(tileMap) if not tile.IsOccupied]

    def Move(self, tileMap):
        availableTiles = self.CheckAvailableTiles(tileMap)
        