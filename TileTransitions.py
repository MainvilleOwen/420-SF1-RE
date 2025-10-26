import pygame

import ClassesAndVariables as CV
import TileMaps as TM

maxLiftMinimum = 900

def clampFunc(val, a=0, b=1):
    return max(a, min(b, val))

def smoothStepFunc(val):
    clampedVal = clampFunc(val)
    return ((clampedVal**2) * (3 - 2*clampedVal))

def liftTilesOffScreen(clock, tileList, tileMap, isoXConvert, isoYConvert):
    running = True
    deltaTime = 0.0

    transitionTime = 0.0
    transitionDuration = 0.9
    maxLift = max(maxLiftMinimum, CV.screenHeight)

    tileOffset = 0.02

    maxTileDelay = (TM.xMaxIndex + TM.yMaxIndex) * tileOffset

    while running:
        CV.Background.ClearScreen()

        transitionTime += deltaTime
        progress = transitionTime/transitionDuration

        for (tileX, tileY, tileZ) in tileList:
            tile = tileMap[tileZ][tileY][tileX]

            tileDepth = (tileX + tileY)
            tileDelay = tileDepth * tileOffset

            tileProgress = clampFunc(progress - tileDelay)
            lift = maxLift * smoothStepFunc(tileProgress)

            if not tile:
                continue
            tile.Blit(CV.screen, isoXConvert(tileX, tileY), isoYConvert(tileX, tileY, tileZ) - lift)

        pygame.display.flip()
        deltaTime = clock.tick(60)/1000

        if progress >= 1.0 + maxTileDelay:
            break


def liftTilesOntoScreen(clock, tileList, tileMap, isoXConvert, isoYConvert):
    running = True
    deltaTime = 0.0

    transitionTime = 0.0
    transitionDuration = 0.9
    maxLift = max(maxLiftMinimum, CV.screenHeight)

    tileOffset = 0.02

    maxTileDelay = (TM.xMaxIndex + TM.yMaxIndex) * tileOffset

    while running:
        CV.Background.ClearScreen()

        transitionTime += deltaTime
        progress = transitionTime/transitionDuration

        for (tileX, tileY, tileZ) in tileList:
            tile = tileMap[tileZ][tileY][tileX]

            tileDepth = (tileX + tileY)
            tileDelay = tileDepth * tileOffset

            tileProgress = clampFunc(progress - tileDelay)
            lift = maxLift * smoothStepFunc(tileProgress)

            if not tile:
                continue
            tile.Blit(CV.screen, isoXConvert(tileX, tileY), isoYConvert(tileX, tileY, tileZ) + maxLift - lift)

        pygame.display.flip()
        deltaTime = clock.tick(60)/1000

        if progress >= 1.0 + maxTileDelay:
            break

def swapTilesOnScreenPos(clock, originalTileList, rotatedTileList, originalTileMap, rotatedTileMap, isoXConvert, isoYConvert):
    running = True
    deltaTime = 0.0

    transitionTime = 0.0
    transitionDuration = 1.2
    maxLift = max(maxLiftMinimum, CV.screenHeight)

    tileOffset = 0.02
    maxTileDelay = (TM.xMaxIndex + TM.yMaxIndex) * tileOffset

    while running:
        CV.Background.ClearScreen()

        transitionTime += deltaTime
        progress = transitionTime/transitionDuration

        for (tileX, tileY, tileZ) in originalTileList:
            tile = originalTileMap[tileZ][tileY][tileX]

            if tile:
                tileDepth = (tileX + tileY)
                tileDelay = tileDepth * tileOffset

                tileProgress = clampFunc(progress - tileDelay)
                lift = maxLift * smoothStepFunc(tileProgress)

                tile.Blit(CV.screen, isoXConvert(tileX, tileY), isoYConvert(tileX, tileY, tileZ) - lift)


        for (tileX, tileY, tileZ) in rotatedTileList:
            tile = rotatedTileMap[tileZ][tileY][tileX]

            if tile:
                tileDepth = (tileX + tileY)
                tileDelay = tileDepth * tileOffset
                
                tileProgress = clampFunc(progress - tileDelay)
                lift = maxLift * smoothStepFunc(tileProgress)

                tile.Blit(CV.screen, isoXConvert(tileX, tileY), isoYConvert(tileX, tileY, tileZ) + maxLift - lift)

        pygame.display.flip()
        deltaTime = clock.tick(60)/1000

        if progress <= 0.1 + maxTileDelay:
            pygame.event.clear()

        if progress >= 1.0 + maxTileDelay:
            break

def swapTilesOnScreenNeg(clock, originalTileList, rotatedTileList, originalTileMap, rotatedTileMap, isoXConvert, isoYConvert):
    running = True
    deltaTime = 0.0

    transitionTime = 0.0
    transitionDuration = 1.2
    maxLift = max(maxLiftMinimum, CV.screenHeight)

    tileOffset = 0.02
    maxTileDelay = (TM.xMaxIndex + TM.yMaxIndex) * tileOffset

    while running:
        CV.Background.ClearScreen()

        transitionTime += deltaTime
        progress = transitionTime/transitionDuration

        for (tileX, tileY, tileZ) in originalTileList:
            tile = originalTileMap[tileZ][tileY][tileX]

            if tile:
                tileDepth = ((TM.xMaxIndex - tileX) + (TM.yMaxIndex - tileY))
                tileDelay = tileDepth * tileOffset

                tileProgress = clampFunc(progress - tileDelay)
                lift = maxLift * smoothStepFunc(tileProgress)

                tile.Blit(CV.screen, isoXConvert(tileX, tileY), isoYConvert(tileX, tileY, tileZ) + lift)


        for (tileX, tileY, tileZ) in rotatedTileList:
            tile = rotatedTileMap[tileZ][tileY][tileX]

            if tile:
                tileDepth = ((TM.xMaxIndex - tileX) + (TM.yMaxIndex - tileY))
                tileDelay = tileDepth * tileOffset
                
                tileProgress = clampFunc(progress - tileDelay)
                lift = maxLift * smoothStepFunc(tileProgress)

                tile.Blit(CV.screen, isoXConvert(tileX, tileY), isoYConvert(tileX, tileY, tileZ) - maxLift + lift)

        pygame.display.flip()
        deltaTime = clock.tick(60)/1000

        if progress <= 0.1 + maxTileDelay:
            pygame.event.clear()

        if progress >= 1.0 + maxTileDelay:
            break