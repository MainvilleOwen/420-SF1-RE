import TileClassAndOperations.TileClass as T
import TileClassAndOperations.TileMapClass as TC
import SpriteInfo as SI

def FG():
    return(T.MakeTileWalkable(SI.FullGrassTile))

def FN():
    return(T.MakeTileUnWalkable(SI.FullGrassTile))

def RG():
    return(T.MakeTileWalkable(SI.RockGrassTile))

def RN():
    return(T.MakeTileUnWalkable(SI.RockGrassTile))

def Wr():
    return(T.MakeTileUnWalkable(SI.WaterTile))

def DS():
    return(T.MakeTileWalkable(SI.DesertSandTile))

def DN():
    return(T.MakeTileUnWalkable(SI.DesertSandTile))

def CreateTileMaps():
# These are the tilemaps. They are nested lists that act as 2d matrices.
# The cool part is because pygame has the origin of the screen at the top left corner and going up in y is down on the screen, this basically matches the list idndexes with [y][x]
        global tileMap1
        tileMap1 = TC.TileMap([[[None, None, None, None, None, None, None, None, None, None, None, None, None, None],
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
                                [None, None, None, None, None, None, None, None, None, None, None, None, None, None]]])
            