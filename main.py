"""
Intro to Programming – Final Project
Student Name: Owen Mainville
Project Title: Tactical Grid Engine

Description:

This project implements a turn-based tactical grid engine in Python using Pygame, featuring tile-based movement, unit pathfinding, and interactive terrain.
It includes an isometric tilemap renderer with visual effects such as water tiles that smoothly bobs using a sin function, and layered draw order to properly display units over tiles.
Player and enemy units occupy tiles, can move along calc1'
ulated paths with smooth interpolation, and face correct directions based on movement vectors.
Tile highlighting and reach indicators support click-to-move controls and visual feedback for valid movement ranges.
The engine is designed for extensibility, allowing for later implementation of combat logic, AI behaviors, and additional tile types.

Instructions:

==============================
 HOW TO RUN THE PROGRAM
==============================

To launch the demo, run main.py.
All initialization—tilemap creation, unit spawning, and rendering is handled internally.
No additional configuration files are required.

==============================
 THE DEMO - CONTROLS
==============================

Hovering over a tile highlights it in white if is able to be walked on by anyone, and red if it cannot be walked on.

Hovering over the character will highlight all tiles in movement range (the speed attribute) in Blue, and all tiles in attacking range in Red.
    (Tiles in both categories appear as Blue only)

Clicking on the tile with the character on it will select that character, and show all the movement options even without hovering.
Clicking on a tile in blue during this mode will move the character.

The Up arrow rotates the tilemap 90 degrees clockwise
The Down arrow rotates the tilemap 90 degrees counter clockwise

The escape button lifts the tiles off of the screen before exiting the program.

==============================
 TILEMAP — HOW TO MODIFY
==============================

Tile generation happens in TileMapClass.py inside LoadMap().
Tilemaps are nested lists that form 3d matrices. More can be made, and they should all be stored into this file.
TileMap (THE CLASS) contains 3 lists for different variations of coloured sprites that can indicate different things. So far, White, Red, and Blue are implemented.
Making them in different functions to only load them when needed might be wise.
They can be created with functions, and their sprite can be passed into the MakeTile functions (MakeTileWalkable(...), MakeTileUnwalkable(...)).
Pro tip: make wrapper functions inside the tilemap file that are 2 character long, that way tilemaps stay perfectly lined up.


Each tile gets a <sprite> attribute, which can then be checked for to implement custom logic for specific tiles.
For example, tiles with a water sprite have their own logic at the tilemap level to make them bob currently.
Tiles never have another version of their sprite assigned to that variable, instead conversions are used at runtime only when drawing.
Each tile also gets a <walkable> attribute that can be changed, but using one or the other MakeTile function will set this to true or false respectively.

Tile occupancy for units uses two systems:
  - Logical occupancy: AssignTileLogically(unit) / UnAssignUnitVisually()
  - Visual ordering: AssignUnitVisually(unit) / UnAssignUnitVisually()
  - Both at once: OccupyTile(unit) / UnOccupyTile()
These are all contained in the tile class, not the unit.

Draw order is computed in GetTileDrawOrder().

==============================
 UNITS — HOW TO MODIFY
==============================

Units are created in main.py using the Unit class. Changing the
(x, y, z) tile passed into Unit() changes where a unit spawns.

Movement uses flood-fill pathfinding through FindPath(), and actual motion
is animated in UpdateRelativePosition() using frame-based movement.
Currently units do not have a spritesheet setup, but it can be implemented if functions are added, and they have the parameter for it.

Unit facing uses helper functions:
  FaceLeft(), FaceRight(), FaceFront(), FaceBack(), etc.
These have a few hardcoded values in these that are spritesheet dependant.

You can safely edit attributes to create different unit combinations.
Unit Presets can be made, like Knight1.
Each Unit contains a link to the tile its on and each tile contains a link to unit its on, which allows for logic to work both ways.
"""


import pygame

import Sprites.SpriteInfo as SI
import ScreenAndClock as SaC

import TileClassAndOperations.TileClass as T

import TileClassAndOperations.TileMapClass as TC
import TileClassAndOperations.TileMaps as TM

from UnitTypes import PlayerCharacterUnitClass as PC
from UnitTypes import EnemyCharacterUnitClass as EC

import Sprites.BackgroundClass as B

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
    currentUnit = None

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

            Knight1 = PC.PlayerCharacterUnit(name="Knight", spritesheet=SI.AllyKnightSpritesheet, spriteIndex=1, reach=13, power=1, critChance=1, critDamage=1, health=1, speed=12, defense=1)
            currentTileMap.SafelyGetTile(11, 9, 0).OccupyTile(Knight1)

            tileMapLoaded = True

            pygame.event.clear()

        mouseX, mouseY = pygame.mouse.get_pos()

    # ALL TILE LOGIC AND RENDERING OF EVERYTHING DONE HERE

    # Logic for checking which tile is being hovered over/selected (Does not happen during transitions)
        if not paused:
            hoveredTile = currentTileMap.FindHoveredTile(mouseX, mouseY, currentUnit)


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
                            if hoveredTile.TileOccupied() and not currentUnit:
                                currentUnit = hoveredTile.unit

                            elif not hoveredTile.TileOccupied() and currentUnit:
                                currentUnit.SetPath(hoveredTile.ReconstructPath(Knight1.tile.GetTilesInReach(currentTileMap, Knight1.speed)))
                                currentUnit = None


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
