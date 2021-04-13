# Source: https://codereview.stackexchange.com/questions/179434/codefights-snake-game
from sys import stdin, stdout

EMPTY = '.'
BODY = '*'
DEAD = 'X'
HEADS = {'v': (1, 0), '^': (-1, 0), '<': (0, -1), '>': (0, 1)}


class Snake(object):
    # Initialize a snake
    def __init__(self, bor_x, bor_y, head):
        self.bor_x = bor_x
        self.bor_y = bor_y
        self.body = [head]
        self.head_only = False
        self.alive = True

    # Checking if position conflicts with the snake?
    def pos_is_free(self, x, y):
        if any(x == dx and y == dy for [dx, dy, _] in self.body):
            return False
        else:
            if x in range(self.bor_x) and y in range(self.bor_y):
                return True

    # Adding body to snake
    def add_body(self, body_part):
        self.body.append(body_part)

    # Self test
    def testing(self, game_state, n):
        print("Borders: ", end='')
        print(self.bor_x, end='')
        print(self.bor_y)
        print("Body detail: ", end='')
        print(len(self.body))
        for body in self.body:
            print(body, sep =" ", end=" ")
        print("\n")
        print("Status: ", end='')
        print("Head only: ", self.head_only, end='\t')
        print("\tAlive: ", self.alive)
        print("Current game state: ")
        for i in range(int(n)):
            for j in game_board[i]:
                print(*j, sep='', end='')
            print('')

    # Aliven't <Roblox euf sound>
    def die(self):
        self.alive = False
        self.body = [[x, y, DEAD] for [x, y, _] in self.body]

    # Turning the snake's head
    def turn(self, command):
        new_direc = {'v': {'L': '>', 'R': '<'},
                     '^': {'L': '<', 'R': '>'},
                     '<': {'L': 'v', 'R': '^'},
                     '>': {'L': '^', 'R': 'v'}}
        x, y, head = self.body[0]
        new_head = new_direc[head][command]
        self.body[0] = [x, y, new_head]

    # Moving the entire snake, which is a pain in the ass because the snake is such a drag
    def move(self):
        x, y, char = self.body[0]
        dest_x, dest_y = HEADS[char]
        # Calculating the tail location versus the head
        tail_x, tail_y, tail_char = self.body[-1]
        # Calculating the next area the snake will move to
        new_x, new_y = x + dest_x, y + dest_y
        # Checking if it's a tail. If yes, move it up a notch and not kill it like an idiot
        if (new_x, new_y) == (tail_x, tail_y):
            self.body[0], self.body[-1] = self.body[-1], self.body[0]
            self.body[0][2] = self.body[-1][2]
            self.body[-1][2] = BODY
            return
        if self.pos_is_free(new_x, new_y):
            if self.head_only is False:
                self.body = [[new_x, new_y, char]] + [[x, y, BODY]] + self.body[1:-1]
            else:
                self.body = [[new_x, new_y, char]] + self.body[1:-1]
        else:
            self.die()

    # Updating the grid in a painful way
    def get_as_grid(self):
        g = [[EMPTY for i in range(self.bor_y)] for j in range(self.bor_x)]
        for x, y, c in self.body:
            g[x][y] = c
        return g


# Finding the head
def find_head(game_board, n, m):
    for i, row in enumerate(game_board):
        for head, (dx, dy) in HEADS.items():
            if head in row:
                return Snake(n, m, [i, row.index(head), head])
    return None


# Finding the body
def find_body(game_board, snake):
    x, y, char = snake.body[-1]
    for (dx, dy) in HEADS.values():
        new_x, new_y = x + dx, y + dy
        if char in HEADS:
            check_x, check_y = HEADS[char]
            if (dx, dy) == (check_x, check_y) and game_board[new_x][new_y] == BODY:
                continue
        if snake.pos_is_free(new_x, new_y) and game_board[new_x][new_y] == BODY:
            return [new_x, new_y, BODY]
    return None


# Finding the entire snake
def find_snake(game_board, n, m):
    # Get the head, duh
    init_snake = find_head(game_board, n, m)
    # Handling empty play field
    if init_snake is None:
        return
    # Get the body
    while True:
        bod = find_body(game_board, init_snake)
        if bod is None:
            break
        init_snake.add_body(bod)
    if len(init_snake.body) == 1:
        init_snake.head_only = True
    return init_snake


# Running the game
def snakeGame(gameBoard, n, m, commands):
    # Find snake
    s = find_snake(gameBoard, n, m)

    for command in commands:
        if command in "LR":
            # Change the head
            s.turn(command)
        else:
            s.move()
            if not s.alive:
                break
    return s.get_as_grid()


n, m, col = stdin.readline().split()
game_board = []
for i in range(int(n)):
    game_board.append(stdin.readline().strip())
    game_board[i] = list(game_board[i][:int(m)])
steps = stdin.readline().strip()
steps = steps[:int(col)]

final_res = snakeGame(game_board, int(n), int(m), steps)
for i in final_res:
    print(*i, sep='')