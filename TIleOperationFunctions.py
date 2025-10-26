def TileDrawOrder(tileMap):
    zMaxIndex, yMaxIndex, xMaxIndex = (len(tileMap)-1), (len(tileMap[0])-1), (len(tileMap[0][0])-1)
    returnedTiles = []
    totalNum = 0
    while totalNum <= (zMaxIndex + yMaxIndex + xMaxIndex):
        
        refCoords = [0, 0, 0]
        refCoords[2] = totalNum
        if refCoords[2] > zMaxIndex:
            refCoords[1] = refCoords[2] - zMaxIndex
            refCoords[2] -= refCoords[1]
            if refCoords[1] > yMaxIndex:
                refCoords[0] = refCoords[1] - yMaxIndex
                refCoords[1] -= refCoords[0]
        x,y,z = refCoords[0], refCoords[1], refCoords[2]
    # The loop stops when totalNum is greater then the max these 3 values can be, youll never have an X too big to index
        counter = 0


        while (z >= 0) and ((x + y + z) <= totalNum):

            while (y >= 0) and (x <= xMaxIndex):
                tile = tileMap[z][y][x]
                if tile:
                    returnedTiles.append((x, y, z))
                x += 1
                y -= 1
            counter += 1
            x,y = (refCoords[0]), (refCoords[1] + counter)
            if y > yMaxIndex:
                diff = y - yMaxIndex
                y -= diff
                x += diff
            z -= 1
        totalNum += 1
    return(returnedTiles)

def RotateTileMap90pos(tileMap):
    return [[list(row) for row in zip(*layer[::-1])] for layer in tileMap]

def RotateTileMap90neg(tileMap):
    return [[list(row) for row in zip(*layer)][::-1] for layer in tileMap]

