"""
Screen settings
"""
RESOLUTION = (1024, 1024)
OFFSET = (RESOLUTION[0] // 2, RESOLUTION[1] // 2)


"""
Colour settings
"""
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

EMPTY_NODE_COLOUR = (50, 50, 50)
BACKGROUND_COLOUR = BLACK
TEXT_COLOUR = WHITE


"""
Tile and settings
"""
# radius (center to long side) of hex grids
HEX_RADIUS = 50
TILE_SIDE_WIDTH = 16
TILE_PADDING = 0

DECK_POS_X = RESOLUTION[0] - HEX_RADIUS - 10
DECK_POS_Y = RESOLUTION[1] - HEX_RADIUS - 10
