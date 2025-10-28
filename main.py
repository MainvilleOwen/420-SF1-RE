import pygame

import SpriteInfo as SI
import Screen as S

import TileClassAndOperations.TileClass as T
import TileClassAndOperations.TileMaps as TM

from UnitTypes import PlayerCharacterUnitClass as PC
from UnitTypes import EnemyCharacterUnitClass as EC

import TileClassAndOperations.TIleOperations as TO
import TileClassAndOperations.TileTransitions as TR

import BackgroundClass as B


# Getting the clock to be able to control framerate, and getting deltaTime which is the time between current and last frame (0 for the first frame)
clock = pygame.time.Clock()
deltaTime = 0

# Functions that load in all elements needed to start running the game *(ORDER MATTERS, THESE ARE ESSENTIAL)*
S.InitializeScreen()

SI.LoadSpriteAssets()
B.CreateBackground(SI.BackgroundSprite)

TM.CreateTileMaps()


# The variable that if true lets the loop run, if false closes the program
running = True

currentSelectedTile = None

currentTileMap = TM.tileMap1
TM.SetTileMapInfo(TM.tileMap1)

nextTileMap = None
tilesToDraw = TO.TileDrawOrder(currentTileMap)
nextTilesToDraw = None
tileMapLoaded = False

paused = False


# The offsets that allow tiles to be centered on the screen no matter the size of the tilemap, as long as its square and centered within that square
xAxisOffset = (S.screenWidth//2 - SI.tileWidth/2) - (SI.tileWidth/2)*((TM.widthHeightDifference - 1)/2)
yAxisOffset = (S.screenHeight//2 - (SI.tileHeight/2)*(TM.tileMapYLenght + 1))

# Functions that convert from coordinates inside the tilemap to screen coordinates in isometric space
# The reason for the weird if statement instead of the simple <offset = xAxisOffset> in the function is because
# without it formatted like this python will not take note of any changes to the xAxisOffset inside the function after computing it once.
# This means that if the window is resized or anything the covnersion will still be centered
def fromXToIsoX(x, y, offset=None):
    if not offset:
        offset = xAxisOffset
    return(32*x - 32*y + offset)
def fromYToIsoY(x, y, z, offset=None):
    if not offset:
        offset = yAxisOffset
    return(16*x + 16*y + 12*((TM.zMaxIndex) - z) + yAxisOffset)



# THE MAIN GAME LOOP
# THIS IS WHAT IS RAN/COMPUTED/CALLED EVERY SINGLE FRAME
while running:
# Clears the screen (BY filling it with Black) for new stuff to be drawn
    B.Background.ClearScreen()

    if not tileMapLoaded:

        TR.liftTilesOntoScreen(clock, tilesToDraw, currentTileMap, fromXToIsoX,  fromYToIsoY)
        tileMapLoaded = True

        pygame.event.clear()

    mouseX, mouseY = pygame.mouse.get_pos()

# ALL TILE LOGIC AND RENDERING OF EVERYTHING DONE HERE

# Logic for checking which tile is being hovered over/selected (Does not happen during transitions)
    if not paused:
        for (tileX, tileY, tileZ) in tilesToDraw:
            tile = currentTileMap[tileZ][tileY][tileX]

            diffX = mouseX - (fromXToIsoX(tileX, tileY) + 32)
            diffY = mouseY - (fromYToIsoY(tileX, tileY, tileZ) + 16 + 10)

            if tile and tile != currentSelectedTile and (abs(diffX)/32 + abs(diffY)/16) <= 1:
                currentSelectedTile = tile

# Draws every tile in order of rendering
    for (tileX, tileY, tileZ) in tilesToDraw:
        tile = currentTileMap[tileZ][tileY][tileX]
        if not tile:
            continue
        elif currentSelectedTile and tile == currentSelectedTile:
            tile.BlitWhileSelected(S.screen, fromXToIsoX(tileX, tileY), fromYToIsoY(tileX, tileY, tileZ))
        else:
            tile.Blit(S.screen, fromXToIsoX(tileX, tileY), fromYToIsoY(tileX, tileY, tileZ))


# ALL EVENT CHECKING DONE HERE        
    for event in pygame.event.get():
# Close the window (X OUT)
            if (event.type == pygame.QUIT):
                TR.liftTilesOffScreen(clock, tilesToDraw, currentTileMap, fromXToIsoX, fromYToIsoY)
                running = False

            
            if (event.type == pygame.VIDEORESIZE):
                S.screenWidth = max(event.w, 960)
                S.screenHeight = max(event.h, 540)
                S.screen = pygame.display.set_mode((S.screenWidth,S.screenHeight), pygame.RESIZABLE)

                xAxisOffset = (S.screenWidth//2 - SI.tileWidth/2) - (SI.tileWidth/2)*((TM.widthHeightDifference - 1)/2)
                yAxisOffset = (S.screenHeight//2 - (SI.tileHeight/2)*(TM.tileMapYLenght + 1))


# ALL MOUSE PRESSING EVENTS
            if (event.type == pygame.MOUSEBUTTONDOWN) and not paused:
                if (event.button == 1):
                    if currentSelectedTile and currentSelectedTile.walkable:
                        if not currentSelectedTile.TileOccupied():
                            currentSelectedTile.OccupyTile(PC.PlayerCharacterUnit(name="Knight", spritesheet=SI.AllyKnightStanding, sprite=SI.AllyKnightStanding, reach=1, power=1, critChance=1, critDamage=1, health=1, speed=1, defense=1))
                        else:
                            currentSelectedTile.unit.FaceLeft()
                            currentSelectedTile.unit.FaceRight()
                elif (event.button == 3):
                    if currentSelectedTile and currentSelectedTile.walkable:
                        if not currentSelectedTile.TileOccupied():
                            currentSelectedTile.OccupyTile(EC.EnemyCharacterUnit(name="Enemy", spritesheet=SI.EnemyKnightStanding, sprite=SI.EnemyKnightStanding, reach=1, power=1, critChance=1, critDamage=1, health=1, speed=1, defense=1))
                        else:
                            currentSelectedTile.unit.FaceLeft()
                            currentSelectedTile.unit.FaceRight()


# ALL MOUSE PRESSING EVENTS
            if (event.type == pygame.KEYDOWN):

# Rotate the tileMap 90 degrees clockwise\counterclockwise and calculates the new tileDrawOrder, which is stored
# New and Old tilemap are then swapped with replacement animation (In trileTransitions.py)
# Finally Old Tilemap is replaced with new one variable wise
                if (event.key == pygame.K_UP) and not paused:

                    nextTileMap = TO.RotateTileMap90pos(currentTileMap)
                    nextTilesToDraw = TO.TileDrawOrder(nextTileMap)

                    TR.swapTilesOnScreenPos(clock, tilesToDraw, nextTilesToDraw, currentTileMap, nextTileMap, fromXToIsoX, fromYToIsoY)

                    currentTileMap = nextTileMap
                    tilesToDraw = nextTilesToDraw

                if (event.key == pygame.K_DOWN) and not paused:
                    

                    nextTileMap = TO.RotateTileMap90neg(currentTileMap)
                    nextTilesToDraw = TO.TileDrawOrder(nextTileMap)

                    TR.swapTilesOnScreenNeg(clock, tilesToDraw, nextTilesToDraw, currentTileMap, nextTileMap, fromXToIsoX, fromYToIsoY)

                    currentTileMap = nextTileMap
                    tilesToDraw = nextTilesToDraw

# Test function that makes current TileMap equal to tileMap1
                if (event.key == pygame.K_1) and not paused:
                    currentTileMap = TM.tileMap1
                    tilesToDraw = TO.TileDrawOrder(currentTileMap)

                if (event.key == pygame.K_ESCAPE):
                    TR.liftTilesOffScreen(clock, tilesToDraw, currentTileMap, fromXToIsoX,  fromYToIsoY)
                    running = False

                    currentSelectedTile = None
                    paused = not paused


# Uploads everything drawn to the screen basically
    pygame.display.flip()

# Stores the time between the current frame and the last frame, which is the time between the last time this was called in the last loop run and this time, updates every frame.
    deltaTime = clock.tick(60) / 1000

pygame.quit()
