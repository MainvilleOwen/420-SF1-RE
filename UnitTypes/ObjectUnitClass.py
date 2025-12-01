import pygame
import random

from UnitTypes.UnitClass import Unit

class ObjectUnit(Unit):
    def __init__(self, name:str, spritesheet:pygame.Surface, sprite:pygame.Surface, reach:int, power:int, countdown:int, team:int):
        super().__init__(name, spritesheet, sprite, reach, power, team)
# Amount of turns the the object lasts
        self.countdown = countdown
    
    def KillSelf(self):
        del self

    def Attack(self, tileMap, areaAttack:bool=True):
        TilesInReach = self.tile.GetTilesInReach(tileMap)
        targets = []

        for tile in TilesInReach.keys():
            if tile.IsTileOccupied and tile.unit.team != self.team:
                targets.append(tile.unit)

# Chooses a random target in the possible targets if the attack is not specified to be an areaAttack
        if not areaAttack:
            targets = targets[random.randint(0, len(targets) - 1)]
        
# Deals damage to all targets according to power
        for target in targets:
            self.DealDamageTo(target)


    def TickCountdown(self):
        self.countdown -= 1

        if self.countdown <= 0:
            self.Attack()
            self.KillSelf()

    def Act(self, tileMap):
        self.Attack(tileMap)
        self.TickCountdown()