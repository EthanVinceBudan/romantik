import pygame

from lib.board import Board, BoardNode
from lib.cubecoordinate import coords_from_xy
from lib.tile_renderer import TileRenderer
from lib.deck import Deck
import config


class Hex:
    node: BoardNode
    vertices: list[tuple[int, int, int]]

    def __init__(self, node: BoardNode) -> None:
        self.node = node
        self.vertices = node.get_location().get_vertices(
            config.OFFSET, config.HEX_RADIUS, 4)


class Renderer:
    _screen: pygame.Surface
    _instructions: pygame.Surface
    _images: dict[tuple[str, int | None], pygame.Surface]
    _font: pygame.font.Font
    _status_position: tuple[int, int]
    _board: Board
    _deck_tile: TileRenderer
    _nodes: list[Hex]
    _tileRenderers: list[TileRenderer]

    def __init__(self, board: Board, deck: Deck) -> None:
        self._screen = pygame.display.set_mode(config.RESOLUTION)
        self._board = board
        self._deck = deck
        self._hexes = []
        self._nodes = []
        self._tileRenderers = []

        self.update_board()
        self.update_deck_tile()

        self._font = pygame.font.Font(pygame.font.get_default_font(), 14)

    def clear(self) -> None:
        """Clear the screen with BACKGROUND_COLOUR.
        """
        self._screen.fill(config.BACKGROUND_COLOUR)

    def update_board(self):
        for node in self._board.all_nodes():
            if node.has_tile():
                position = node.get_location().to_cartesian()
                self._tileRenderers.append(TileRenderer(
                    self._screen, node.get_tile(),
                    (position[0] * config.HEX_RADIUS + config.OFFSET[0],
                     position[1] * config.HEX_RADIUS + config.OFFSET[1]),
                    config.HEX_RADIUS))
            else:
                self._hexes.append(Hex(node))

    def draw_board(self) -> None:
        """Draw each block in blocks onto the screen.
        """

        for hex in self._hexes:
            pygame.draw.polygon(
                self._screen, config.EMPTY_NODE_COLOUR, hex.vertices, 0)

        for tileRenderer in self._tileRenderers:
            tileRenderer.render()

    def update_deck_tile(self):
        self._deck_tile = TileRenderer(self._screen, deck.peek(),
                (config.DECK_POS_X, config.DECK_POS_Y), config.HEX_RADIUS)

    def draw_deck(self) -> None:
        if self._deck_tile:
            self._deck_tile.render()

    def highlight_block(self, vertices: list[tuple[int, int]]) -> None:
        """Draw a highlighted border at pos with size.
        """
        pygame.draw.polygon(
            self._screen, config.WHITE, vertices, 2)


def process_event(board: Board, deck: Deck, event: pygame.event.Event):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            node = get_selected_node(board)
            if node and not node.has_tile() and len(deck) > 0:
                tile = deck.peek()
                neighbor_tiles = []
                for neighbor in node._neighbors:
                    if neighbor and neighbor.has_tile():
                        neighbor_tiles.append(neighbor.get_tile())
                    else:
                        neighbor_tiles.append(None)
                if tile._validate_placement(neighbor_tiles):
                    board.expand(node.get_location())
                    node.set_tile(deck.draw())
                    renderer.update_board()
                    renderer.update_deck_tile()
        elif event.key == pygame.K_a:
            deck.peek().rotate(1)
            renderer.update_deck_tile()
        elif event.key == pygame.K_d:
            deck.peek().rotate(-1)
            renderer.update_deck_tile()


def get_selected_node(board: Board) -> BoardNode | None:
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos = (mouse_pos[0] - config.OFFSET[0],
                 mouse_pos[1] - config.OFFSET[1])
    coords = coords_from_xy(mouse_pos, config.HEX_RADIUS)
    if coords in board._positions:
        return board._positions[coords]
    else:
        return None


if __name__ == '__main__':
    board = Board()
    deck = Deck()

    pygame.init()
    renderer = Renderer(board, deck)

    clock = pygame.time.Clock()

    while True:
        clock.tick(30)

        selected_node = get_selected_node(board)

        # Process events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            else:
                process_event(board, deck, e)

        renderer.clear()
        renderer.draw_board()
        renderer.draw_deck()
        if selected_node:
            renderer.highlight_block(
                selected_node.get_location().get_vertices(config.OFFSET, 
                                                          config.HEX_RADIUS, 0))

        # Update the screen
        pygame.display.flip()
