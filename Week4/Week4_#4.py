#Source: https://codereview.stackexchange.com/questions/197287/codefights-pyraminx-puzzle
from sys import stdin

#User mod: 200_success
def make_moves(moves):
    """
    Extrapolate from a table of moves to build a table that includes
    clockwise moves, counterclockwise moves, and corner-only moves.
    Each resulting key will be the name of a move (e.g. "U'"), and each
    resulting value will be a function that mutates a puzzle.
    """
    def make_move(new_positions, old_positions):
        def move(puzzle):
            old_colors = [puzzle[r][c] for r, c in old_positions]
            for (r, c), color in zip(new_positions, old_colors):
                puzzle[r][c] = color
        return move
    for turn, pos in moves.items():
        # Clockwise variant
        yield turn, make_move(pos[-4:] + pos[:-4], pos)
        # Counterclockwise variant
        yield turn + "'", make_move(pos[4:] + pos[:4], pos)
        # Corner-only clockwise variant
        yield turn.upper(), make_move([pos[i] for i in range(-4, 8, 4)], pos[::4])
        # Corner-only counterclockwise variant
        yield turn.upper() + "'", make_move([pos[i] for i in range(-8, 4, 4)], pos[::4])


MOVES = dict(make_moves({
    "u": [(0, 0), (0, 1), (0, 2), (0, 3),
          (3, 8), (3, 3), (3, 7), (3, 6),
          (2, 4), (2, 6), (2, 5), (2, 1)],
    "l": [(2, 0), (2, 1), (2, 2), (2, 3),
          (1, 8), (1, 3), (1, 7), (1, 6),
          (0, 4), (0, 6), (0, 5), (0, 1)],
    "r": [(3, 0), (3, 1), (3, 2), (3, 3),
          (0, 8), (0, 3), (0, 7), (0, 6),
          (1, 4), (1, 6), (1, 5), (1, 1)],
    "b": [(1, 0), (1, 1), (1, 2), (1, 3),
          (2, 8), (2, 3), (2, 7), (2, 6),
          (3, 4), (3, 6), (3, 5), (3, 1)],
}))


def pyraminx_puzzle(face_colors, moves):
    puzzle = [[c] * 9 for c in face_colors]
    for move in reversed(moves):
        MOVES[move](puzzle)
    return puzzle


colours = stdin.readline().split()
while True:
    patterns = stdin.readline().split()
    if patterns[0] == '.':
        break
    new_puzzle = pyraminx_puzzle(colours, patterns)
    for i in range(4):
        print(*new_puzzle[i])