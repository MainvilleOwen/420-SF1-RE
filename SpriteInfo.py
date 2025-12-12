import pygame

def LoadSpriteAssets():
     global tileWidth
     global tileHeight
     tileWidth, tileHeight = 64, 32

# BACKGROUND IMAGES
# Creating the background image sprite
     global BackgroundSprite
     BackgroundSprite = pygame.image.load("Assets/BackgroundFirstEdition.png")

# TILE SPRITES
# Creating Full Grass Tile Sprites
     global FullGrassTile 
     FullGrassTile = pygame.image.load("Assets/IsoTileset/Grass/FullGrass/FullGrassTile.png").convert_alpha()

     global FullGrassTileSelected
     FullGrassTileSelected = pygame.image.load("Assets/IsoTileset/Grass/FullGrass/FullGrassSelectedTile.png").convert_alpha()

     global FullGrassTileUnselectable
     FullGrassTileUnselectable = pygame.image.load("Assets/IsoTileset/Grass/FullGrass/FullGrassTileUnselectable.png").convert_alpha()

     global FullGrassTileBlue
     FullGrassTileBlue = pygame.image.load("Assets/IsoTileset/Grass/FullGrass/FullGrassTileBlue.png").convert_alpha()

# Creating Rock Grass Tile Sprites
     global RockGrassTile
     RockGrassTile = pygame.image.load("Assets/IsoTileset/Grass/RockGrass/RockGrassTile.png").convert_alpha()

     global RockGrassTileSelected
     RockGrassTileSelected = pygame.image.load("Assets/IsoTileset/Grass/RockGrass/RockGrassSelectedTile.png").convert_alpha()

     global RockGrassTileUnselectable
     RockGrassTileUnselectable = pygame.image.load("Assets/IsoTileset/Grass/RockGrass/RockGrassTileUnselectable.png").convert_alpha()

     global RockGrassTileBlue
     RockGrassTileBlue = pygame.image.load("Assets/IsoTileset/Grass/RockGrass/RockGrassTileBlue.png").convert_alpha()


# Creating Desert Sand Tile Sprites
     global DesertSandTile
     DesertSandTile = pygame.image.load("Assets/IsoTileset/Desert/DesertSandTile.png").convert_alpha()

     global DesertSandTileSelected
     DesertSandTileSelected = pygame.image.load("Assets/IsoTileset/Desert/DesertSandSelectedTile.png").convert_alpha()

     global DesertSandTileUnselectable
     DesertSandTileUnselectable = pygame.image.load("Assets/IsoTileset/Desert/DesertSandTileUnselectable.png").convert_alpha()

     global DesertSandTileBlue
     DesertSandTileBlue = pygame.image.load("Assets/IsoTileset/Desert/DesertSandTileBlue.png").convert_alpha()


# Creating Water Tile Sprite
     global WaterTile
     WaterTile = pygame.image.load("Assets/IsoTileset/Common/WaterTile.png").convert_alpha()

     global WaterTileUnselectable
     WaterTileUnselectable = pygame.image.load("Assets/IsoTileset/Common/WaterTileUnselectable.png").convert_alpha()

# Creating Ally Knight Sprite
     global AllyKnightStanding
     AllyKnightStanding = pygame.image.load("Assets/CharacterSprites/Player/AllyKnightFFTSprite2.png").convert_alpha()

# Creating Ally Knight Sprite
     global EnemyKnightStanding
     EnemyKnightStanding = pygame.image.load("Assets/CharacterSprites/Enemy/EnemyKnightFFTSprite2.png").convert_alpha()
	

# This dictionary takes in a regular version of a sprite and gives back the selected version of the sprite, highlighted
     global tileSelectedConversion
     tileSelectedConversion = {
          FullGrassTile: FullGrassTileSelected,
          RockGrassTile: RockGrassTileSelected,
          DesertSandTile: DesertSandTileSelected,
          }
     
# This dictionary takes in a regular tile sprite and returns the unselectable version of that tile
     global tileUnselectableConversion
     tileUnselectableConversion = {
          FullGrassTile: FullGrassTileUnselectable,
          RockGrassTile: RockGrassTileUnselectable,
          DesertSandTile: DesertSandTileUnselectable,
          WaterTile: WaterTileUnselectable
     }

     global tileBlueConversion
     tileBlueConversion = {
          FullGrassTile: FullGrassTileBlue,
          RockGrassTile: RockGrassTileBlue,
          DesertSandTile: DesertSandTileBlue,
          }

# This is a list of all the tiles that can be interacted with
     global interactableTiles
     interactableTiles = [ FullGrassTile, RockGrassTile, DesertSandTile]