import pygame
import ScreenAndClock as SaC
import SpriteInfo as SI
import BackgroundClass as B


# Smoothstep and Clamp live here as they are used at the tilemap level, but don't need to be inside the classS
def clampFunc(val:float, a=0, b=1):
    return max(a, min(b, val))

def smoothStepFunc(val:float):
    clampedVal = clampFunc(val)
    return ((clampedVal**2) * (3 - 2*clampedVal))



class TileMap:
    def __init__(self, tileList:list):

        self.tileList = tileList

# All of these variables are redefined by the RedefineAttributes() Function
        self.xLength = len(tileList[0][0])
        self.yLength = len(tileList[0])

        self.widthHeightDifference = (self.xLength - self.yLength)

        self.zMaxIndex, self.yMaxIndex, self.xMaxIndex = (len(tileList)-1), (len(tileList[0])-1), (len(tileList[0][0])-1)

        self.tileDrawOrder = self.GetTileDrawOrder()


# The offsets that allow tiles to be centered on the screen no matter the size of the tilemap, as long as its square and centered within that square
        self.xAxisOffset = (SaC.screenWidth//2 - SI.tileWidth/2) - (SI.tileWidth/2)*((self.widthHeightDifference - 1)/2)
        self.yAxisOffset = (SaC.screenHeight//2 - (SI.tileHeight/2)*(self.yLength + 1))

        self.Whites = []
        self.Reds = []


    def RedefineAtributes(self):

        self.xLength = len(self.tileList[0][0])
        self.yLength = len(self.tileList[0])

        self.widthHeightDifference = (self.xLength - self.yLength)

        self.zMaxIndex, self.yMaxIndex, self.xMaxIndex = (len(self.tileList)-1), (len(self.tileList[0])-1), (len(self.tileList[0][0])-1)

        self.tileDrawOrder = self.GetTileDrawOrder()

        self.xAxisOffset = (SaC.screenWidth//2 - SI.tileWidth/2) - (SI.tileWidth/2)*((self.widthHeightDifference - 1)/2)
        self.yAxisOffset = (SaC.screenHeight//2 - (SI.tileHeight/2)*(self.yLength + 1))


    def SafelyGetTile(self, x:int, y:int, z:int):
        if z < 0 or z > self.zMaxIndex: return None
        if y < 0 or y > self.yMaxIndex: return None
        if x < 0 or x > self.xMaxIndex: return None
        
        return(self.tileList[z][y][x])


    def GetTileDrawOrder(self):
        returnedTiles = []
        totalNum = 0
        while totalNum <= (self.zMaxIndex + self.yMaxIndex + self.xMaxIndex):
            
            refCoords = [0, 0, 0]
            refCoords[2] = totalNum
            if refCoords[2] > self.zMaxIndex:
                refCoords[1] = refCoords[2] - self.zMaxIndex
                refCoords[2] -= refCoords[1]
                if refCoords[1] > self.yMaxIndex:
                    refCoords[0] = refCoords[1] - self.yMaxIndex
                    refCoords[1] -= refCoords[0]
            x,y,z = refCoords[0], refCoords[1], refCoords[2]
        # The loop stops when totalNum is greater then the max these 3 values can be, youll never have an X too big to index
            counter = 0


            while (z >= 0) and ((x + y + z) <= totalNum):

                while (y >= 0) and (x <= self.xMaxIndex):
                    tile = self.SafelyGetTile(x, y, z)
                    if tile:
                        returnedTiles.append((x, y, z))
                        tile.x, tile.y, tile.z = x, y, z
                    x += 1
                    y -= 1
                counter += 1
                x,y = (refCoords[0]), (refCoords[1] + counter)
                if y > self.yMaxIndex:
                    diff = y - self.yMaxIndex
                    y -= diff
                    x += diff
                z -= 1
            totalNum += 1
        return(returnedTiles)
    
    def WorldToViewX(self, x:int, y:int):
        return(32*x - 32*y + self.xAxisOffset)
    
    def WorldToViewY(self, x:int, y:int, z:int):
        return(16*x + 16*y + 12*((self.zMaxIndex) - z) + self.yAxisOffset)



    def Blit(self):
        screen = SaC.screen
        for (x, y, z) in self.tileDrawOrder:
            tile = self.SafelyGetTile(x, y, z)
            viewX = self.WorldToViewX(x, y)
            viewY = self.WorldToViewY(x, y, z)
# This skips over any items in the tileMap that are empty or "None"
            if tile in self.Whites:
                tile.BlitWhite(screen, viewX, viewY, self.WorldToViewX, self.WorldToViewY)
            elif tile in self.Reds:
                tile.BlitRed(screen, viewX, viewY, self.WorldToViewX, self.WorldToViewY)
            else:
                tile.Blit(screen, viewX, viewY, self.WorldToViewX, self.WorldToViewY)


    def RotateSelf(self, clockwise:bool):
        if clockwise:
            rotatedTileList =  [[list(row) for row in zip(*layer[::-1])] for layer in self.tileList]
            rotatedTileMap = TileMap(rotatedTileList)
        else:
            rotatedTileList =  [[list(row) for row in zip(*layer)][::-1] for layer in self.tileList]
            rotatedTileMap = TileMap(rotatedTileList)



        running = True
        SaC.deltaTime = 0.0
        maxLiftMinimum = 900

        transitionTime = 0.0
        transitionDuration = 1.2
        maxLift = max(maxLiftMinimum, SaC.screenHeight)

        tileOffset = 0.02
        maxTileDelay = (self.xMaxIndex + self.yMaxIndex) * tileOffset

        unitsAlreadyRotated = set()

        while running:
            B.Background.ClearScreen()

            transitionTime += SaC.deltaTime
            progress = transitionTime/transitionDuration

            for (x, y, z) in self.tileDrawOrder:
                tile = self.SafelyGetTile(x, y, z)

                if clockwise: tileDepth = (x + y)
                else: tileDepth = (self.xMaxIndex - x) + (self.yMaxIndex - y)
                
                tileDelay = tileDepth * tileOffset

                tileProgress = clampFunc(progress - tileDelay)

                if clockwise: lift = -maxLift * smoothStepFunc(tileProgress)
                else: lift = maxLift * smoothStepFunc(tileProgress)

                tile.Blit(SaC.screen, self.WorldToViewX(x, y), self.WorldToViewY(x, y, z) + lift)


                if tile.unit and (progress >= 0.5 + tileDelay) and not (tile.unit in unitsAlreadyRotated):
                    tile.unit.Rotate(clockwise=clockwise)
                    unitsAlreadyRotated.add(tile.unit)



            for (x, y, z) in rotatedTileMap.tileDrawOrder:
                tile = rotatedTileMap.SafelyGetTile(x, y, z)

                if clockwise: tileDepth = (x + y)
                else: tileDepth = (self.xMaxIndex - x) + (self.yMaxIndex - y)

                tileDelay = tileDepth * tileOffset
                    
                tileProgress = clampFunc(progress - tileDelay)

                if clockwise:
                    lift = -maxLift * smoothStepFunc(tileProgress)
                else:
                    lift = maxLift * smoothStepFunc(tileProgress)

                tile.Blit(SaC.screen, rotatedTileMap.WorldToViewX(x, y), rotatedTileMap.WorldToViewY(x, y, z) + (maxLift if clockwise else -maxLift) + lift)

            pygame.display.flip()
            SaC.deltaTime = SaC.clock.tick(60)/1000

            if transitionTime >= 0.4:
                pygame.event.clear()

            if progress >= 1.0 + maxTileDelay:
                break


        self.tileList = rotatedTileList
        del rotatedTileMap
        self.RedefineAtributes()


    def LiftTilesOffScreen(self):
        running = True
        SaC.deltaTime = 0.0
        maxLiftMinimum = 900

        transitionTime = 0.0
        transitionDuration = 1.2
        maxLift = max(maxLiftMinimum, SaC.screenHeight)

        tileOffset = 0.02
        maxTileDelay = (self.xMaxIndex + self.yMaxIndex) * tileOffset

        while running:
            B.Background.ClearScreen()

            transitionTime += SaC.deltaTime
            progress = transitionTime/transitionDuration

            for (x, y, z) in self.tileDrawOrder:
                tile = self.SafelyGetTile(x, y, z)

                tileDepth = (x + y)
                tileDelay = tileDepth * tileOffset

                tileProgress = clampFunc(progress - tileDelay)

                lift = -maxLift * smoothStepFunc(tileProgress)

                tile.Blit(SaC.screen, self.WorldToViewX(x, y), self.WorldToViewY(x, y, z) + lift)

            pygame.display.flip()
            SaC.deltaTime = SaC.clock.tick(60)/1000

            if transitionTime <= 0.4:
                pygame.event.clear()

            if progress >= 1.0 + maxTileDelay:
                break


    def LiftTilesOntoScreen(self):
            running = True
            SaC.deltaTime = 0.0
            maxLiftMinimum = 900

            transitionTime = 0.0
            transitionDuration = 1.2
            maxLift = max(maxLiftMinimum, SaC.screenHeight)

            tileOffset = 0.02
            maxTileDelay = (self.xMaxIndex + self.yMaxIndex) * tileOffset

            while running:
                B.Background.ClearScreen()

                transitionTime += SaC.deltaTime
                progress = transitionTime/transitionDuration

                for (x, y, z) in self.tileDrawOrder:
                    tile = self.SafelyGetTile(x, y, z)

                    tileDepth = (x + y)
                    tileDelay = tileDepth * tileOffset

                    tileProgress = clampFunc(progress - tileDelay)

                    lift = -maxLift * smoothStepFunc(tileProgress)

                    tile.Blit(SaC.screen, self.WorldToViewX(x, y), self.WorldToViewY(x, y, z)+ maxLift + lift)

                pygame.display.flip()
                SaC.deltaTime = SaC.clock.tick(60)/1000

                if transitionTime <= 0.4:
                    pygame.event.clear()

                if progress >= 1.0 + maxTileDelay:
                    break

    
    def FindHoveredTile(self, mouseX:int, mouseY:int):
        currentSelectedTile = None
        for (x, y, z) in self.tileDrawOrder:
            tile = self.SafelyGetTile(x, y, z)

            diffX = mouseX - (self.WorldToViewX(x, y) + 32)
            diffY = mouseY - (self.WorldToViewY(x, y, z) + 16 + 10)

            if (abs(diffX)/32 + abs(diffY)/16) <= 1:
                currentSelectedTile = tile
            

        if not currentSelectedTile:
            self.Reds = []
            self.Whites = []
            return None
        else:
            self.Whites = [currentSelectedTile]

            if currentSelectedTile.TileOccupied():
                self.Reds = currentSelectedTile.GetTilesInReach(self, currentSelectedTile.unit.reach)
            else:
                self.Reds = []

        return(currentSelectedTile)
            