import TileClassAndOperations.TileClass as T
import SpriteInfo as SI

def FG():
    return(T.makeTileWalkable(SI.FullGrassTile))

def FN():
    return(T.makeTileUnWalkable(SI.FullGrassTile))

def RG():
    return(T.makeTileWalkable(SI.RockGrassTile))

def RN():
    return(T.makeTileUnWalkable(SI.RockGrassTile))

def Wr():
    return(T.makeTileUnWalkable(SI.WaterTile))

def DS():
    return(T.makeTileWalkable(SI.DesertSandTile))

def DN():
    return(T.makeTileUnWalkable(SI.DesertSandTile))

def CreateTileMaps():
# These are the tilemaps. They are nested lists that act as 2d matrices.
# The cool part is because pygame has the origin of the screen at the top left corner and going up in y is down on the screen, this basically matches the list idndexes with [y][x]
    global tileMap1
    tileMap1 =  [[[None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, RG(), Wr(), Wr(), RG(), RG(), DS(), None, None, None],
                  [None, None, None, FG(), FG(), FG(), Wr(), Wr(), FG(), FG(), DS(), DS(), None, None],
                  [None, FG(), FG(), FG(), FG(), FG(), Wr(), Wr(), FG(), FG(), FG(), DS(), None, None],
                  [None, FG(), FG(), FG(), FG(), RG(), Wr(), Wr(), FG(), FG(), FG(), DS(), DS(), None],
                  [None, None, None, FG(), FG(), Wr(), Wr(), Wr(), FG(), FG(), FG(), DS(), DS(), None],
                  [None, None, None, FG(), FG(), Wr(), Wr(), FG(), FG(), FG(), FG(), FG(), DS(), DS()],
                  [None, None, None, None, RG(), Wr(), Wr(), FG(), FG(), None, None, FG(), RG(), DS()],
                  [None, None, None, None, RG(), Wr(), Wr(), FG(), None, None, None, FG(), FG(), DS()],
                  [None, None, FG(), FG(), FG(), Wr(), Wr(), FG(), FG(), FG(), FG(), FG(), FG(), RG()],
                  [None, None, None, RG(), Wr(), Wr(), RG(), RG(), RG(), RG(), RG(), RG(), RG(), None],
                  [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None, None, None, None, None, None]],

                 [[None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                  [None, None, None, RG(), RG(), None, None, None, None, None, None, DS(), None, None],
                  [None, RG(), FG(), None, None, None, None, None, None, None, None, None, DS(), None],
                  [RG(), FG(), None, None, None, None, None, None, None, None, None, None, DS(), None],
                  [RG(), FG(), None, None, None, None, None, None, None, None, None, None, DS(), None],
                  [None, FG(), FG(), None, None, None, None, None, None, None, None, None, None, DS()],
                  [None, FG(), FG(), None, None, None, None, None, None, None, None, None, None, None],
                  [None, None, None, FG(), None, None, None, None, None, FG(), FG(), None, None, None],
                  [None, None, RG(), FG(), None, None, None, None, FG(), FG(), FG(), None, None, None],
                  [None, FG(), None, None, None, None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None, None, None, None, None, None]],
        
                 [[None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None, None, None, None, DS(), None],
                  [None, None, None, None, None, None, None, None, None, None, None, None, None, DS()],
                  [None, None, None, None, None, None, None, None, None, None, None, None, None, DS()],
                  [None, None, None, None, None, None, None, None, None, None, None, None, None, DS()],
                  [RG(), None, None, None, None, None, None, None, None, None, None, None, None, None],
                  [RG(), None, None, None, None, None, None, None, None, None, None, None, None, None],
                  [Wr(), FG(), FG(), None, None, None, None, None, None, None, None, None, None, None],
                  [RG(), FG(), None, None, None, None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None, None, None, None, None, None]]]

# This is the order of the tilemaps from bottom to top. This list is used to know what order to draw them in
def SetTileMapInfo(tileMap):
    global tileMapXLenght
    global tileMapYLenght
    tileMapXLenght, tileMapYLenght = len(tileMap[0][0]), len(tileMap[0])

    global widthHeightDifference
    widthHeightDifference = (tileMapXLenght - tileMapYLenght)

    global zMaxIndex
    global yMaxIndex
    global xMaxIndex
    zMaxIndex, yMaxIndex, xMaxIndex = (len(tileMap)-1), (len(tileMap[0])-1), (len(tileMap[0][0])-1)