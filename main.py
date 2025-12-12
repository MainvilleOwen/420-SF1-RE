import pygame

import SpriteInfo as SI
import ScreenAndClock as SaC

import TileClassAndOperations.TileClass as T

import TileClassAndOperations.TileMapClass as TC
import TileClassAndOperations.TileMaps as TM

from UnitTypes import PlayerCharacterUnitClass as PC
from UnitTypes import EnemyCharacterUnitClass as EC

import BackgroundClass as B

def main():
    # Functions that load in all elements needed to start running the game *(ORDER MATTERS, THESE ARE ESSENTIAL)*
    SaC.InitializeScreenAndClock()

    SI.LoadSpriteAssets()
    B.CreateBackground(SI.BackgroundSprite)

    TM.CreateTileMaps()


    # The variable that if true lets the loop run, if false closes the program
    running = True

    currentTileMap = TM.tileMap1
    hoveredTile = None

    nextTileMap = None
    tileMapLoaded = False

    paused = False



    # THE MAIN GAME LOOP
    # THIS IS WHAT IS RAN/COMPUTED/CALLED EVERY SINGLE FRAME
    while running:
    # Clears the screen (BY filling it with Black) for new stuff to be drawn
        B.Background.ClearScreen()

        if not tileMapLoaded:

            currentTileMap.LiftTilesOntoScreen()

            Knight1 = PC.PlayerCharacterUnit(name="Knight", spritesheet=SI.AllyKnightStanding, sprite=SI.AllyKnightStanding, reach=4, power=1, critChance=1, critDamage=1, health=1, speed=3, defense=1)
            currentTileMap.SafelyGetTile(11, 9, 0).OccupyTile(Knight1)

            tileMapLoaded = True

            pygame.event.clear()

        mouseX, mouseY = pygame.mouse.get_pos()

    # ALL TILE LOGIC AND RENDERING OF EVERYTHING DONE HERE

    # Logic for checking which tile is being hovered over/selected (Does not happen during transitions)
        if not paused:
            hoveredTile = currentTileMap.FindHoveredTile(mouseX, mouseY)


    # Draws every tile in order of rendering
        Knight1.UpdateRelativePosition(SaC.deltatime, currentTileMap)
        currentTileMap.UpdateWave(SaC.deltatime)
        currentTileMap.Blit()


    # ALL EVENT CHECKING DONE HERE        
        for event in pygame.event.get():
    # Close the window (X OUT)
                if (event.type == pygame.QUIT):
                    currentTileMap.LiftTilesOffScreen()
                    running = False


    # ALL MOUSE PRESSING EVENTS
                if (event.type == pygame.MOUSEBUTTONDOWN) and not paused:
                    if (event.button == 1):
                        if currentTileMap and hoveredTile and hoveredTile.walkable:
                            if not hoveredTile.TileOccupied():
                                Knight1.SetPath(hoveredTile.ReconstructPath(Knight1.tile.GetTilesInReach(currentTileMap, Knight1.speed)))
                                """hoveredTile.OccupyTile(PC.PlayerCharacterUnit(name="Knight", spritesheet=SI.AllyKnightStanding, sprite=SI.AllyKnightStanding, reach=2, power=1, critChance=1, critDamage=1, health=1, speed=1, defense=1))
                            else:
                                hoveredTile.unit.FaceLeft()
                                hoveredTile.unit.FaceRight()"""
                    elif (event.button == 3):
                        if hoveredTile and hoveredTile.walkable:
                            if not hoveredTile.TileOccupied():
                                """hoveredTile.OccupyTile(EC.EnemyCharacterUnit(name="Enemy", spritesheet=SI.EnemyKnightStanding, sprite=SI.EnemyKnightStanding, reach=1, power=1, critChance=1, critDamage=1, health=1, speed=1, defense=1))
                            else:
                                hoveredTile.unit.FaceLeft()
                                hoveredTile.unit.FaceRight()"""


    # ALL MOUSE PRESSING EVENTS
                if (event.type == pygame.KEYDOWN):

    # Rotate the tileMap 90 degrees clockwise\counterclockwise and calculates the new tileDrawOrder, which is stored
    # New and Old tilemap are then swapped with replacement animation (In trileTransitions.py)
    # Finally Old Tilemap is replaced with new one variable wise
                    if (event.key == pygame.K_UP) and not paused:
                        currentTileMap.RotateSelf(clockwise=True)

                    if (event.key == pygame.K_DOWN) and not paused:
                        currentTileMap.RotateSelf(clockwise=False)

    # Test function that makes current TileMap equal to tileMap1
                    if (event.key == pygame.K_1) and not paused:
                        currentTileMap = TM.tileMap1

                    if (event.key == pygame.K_ESCAPE):
                        currentTileMap.LiftTilesOffScreen()
                        running = False


    # Uploads everything drawn to the screen basically
        pygame.display.flip()

    # Stores the time between the current frame and the last frame, which is the time between the last time this was called in the last loop run and this time, updates every frame.
        SaC.deltaTime = SaC.clock.tick(60) / 1000

    pygame.quit()

main()
