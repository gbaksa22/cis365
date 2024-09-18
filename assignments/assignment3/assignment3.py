import heapq
import math


class Square:
    def __init__(self):
        self.parent_x = 0
        self.parent_y = 0
        self.f = float('inf')
        self.g = float('inf')
        self.h = 0


columns = 11
rows = 11


def valid(col, row):
    return (col >= 0) and (col < columns) and (row >= 0) and (row < rows)


def unblocked(grid, row, col):
    return grid[row][col] == 1


def h_value(col, row, dest):
    return ((col - dest[0]) ** 2 + (row - dest[1]) ** 2) ** 0.5


def destination(col, row, dest):
    return col == dest[0] and row == dest[1]


def trace(square_details, dest):
    print('The path is...')
    path = []
    col = dest[0]
    row = dest[1]

    while not (square_details[col][row].parent_x == col and square_details[col][row].parent_y == row):
        path.append((col, row))
        current_col = square_details[col][row].parent_x
        current_row = square_details[col][row].parent_y
        col = current_col
        row = current_row

    path.append((col, row))
    path.reverse()

    for s in path:
        print(s, '-->', end=' ')
    print()


def a_star(grid, start, dest):
    if not valid(start[1], start[0]) or not valid(dest[1], dest[0]):
        print('Invalid start or destination')
        return

    if not unblocked(grid, start[0], start[1]) or not unblocked(grid, dest[0], dest[1]):
        print('The source or destination is blocked')
        return

    if destination(start[0], start[1], dest):
        print('You have already reached the destination square')
        return

    closed_list = [[False for _ in range(columns)] for _ in range(rows)]
    square_details = [[Square() for _ in range(columns)] for _ in range(rows)]

    x = start[0]
    y = start[1]
    square_details[x][y].f = 0
    square_details[x][y].g = 0
    square_details[x][y].h = 0
    square_details[x][y].parent_x = x
    square_details[x][y].parent_y = y

    square_list = []
    heapq.heappush(square_list, (0.0, x, y))

    dest_found = False

    while len(square_list) > 0:
        p = heapq.heappop(square_list)

        x = p[1]
        y = p[2]

        closed_list[x][y] = True

        possible_directions = [(0, 1), (0, -1), (1, 0), (1, 1), (-1, 0), (-1, 1), (-1, -1), (1, -1)]

        for d in possible_directions:
            new_x = x + d[0]
            new_y = y + d[1]

            if valid(new_x, new_y) and unblocked(grid, new_x, new_y) and not closed_list[new_x][new_y]:
                if destination(new_x, new_y, dest):
                    square_details[new_x][new_y].parent_x = x
                    square_details[new_x][new_y].parent_y = y
                    print('We have a path to the destination square!')

                    trace(square_details, dest)

                    dest_found = True
                    return

                else:
                    new_g = square_details[x][y].g + 1.0
                    new_h = h_value(new_x, new_y, dest)
                    new_f = new_g + new_h

                    if square_details[new_x][new_y].f == float('inf') or square_details[new_x][new_y].f > new_f:
                        heapq.heappush(square_list, (new_f, new_x, new_y))

                        square_details[new_x][new_y].f = new_f
                        square_details[new_x][new_y].g = new_g
                        square_details[new_x][new_y].h = new_h
                        square_details[new_x][new_y].parent_x = x
                        square_details[new_x][new_y].parent_y = y

    if not dest_found:
        print('Could not find the destination square :(')


def main():
    # in the following grid, 1 means the path is available and 0 means it is blocked
    # the walls in the map diagram are "widened" to boxes to make sense in this application
    grid = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    start = [0, 0]

    dest = [10, 10]

    a_star(grid, start, dest)


if __name__ == "__main__":
    main()

graph = {
    "a1": ["b1", "a2"],
    "b1": ["a1", "c1", "b2"],
    "c1": ["b1", "d1", "c2"],
    "d1": ["c1", "e1", "d2"],
    "e1": ["d1", "f1", "e2"],
    "f1": ["e1", "g1", "f2"],
    "g1": ["f1", "h1", "g2"],
    "h1": ["g1", "h2"],

    "a2": ["a1", "b2", "a3"],
    "b2": ["b1", "a2", "c2", "b3"],
    "c2": ["c1", "b2", "d2", "c3"],
    "d2": ["d1", "c2"],  # Removed connection to d3
    "e2": ["e1"],  # Removed connection to e3
    "f2": ["f1"],  # Removed connections to g2, f3, g3
    "g2": ["g1", "h2"],
    "h2": ["h1", "g2", "h3"],

    "a3": ["a2", "b3", "a4"],
    "b3": ["b2", "a3", "c3", "b4"],
    "c3": ["c2", "b3", "d3", "c4"],
    "d3": ["c3"],  # Removed connection to d2 and e3
    "e3": [],  # Removed connections to e2, d3
    "f3": ["f4"],  # Removed connection to f2
    "g3": ["g4", "g2"],  # Removed connection to f2
    "h3": ["h2", "g3", "h4"],

    "a4": ["a3", "b4", "a5"],
    "b4": ["b3", "a4"],  # Removed connection to c5
    "c4": ["c3", "d4"],  # Removed connection to c5
    "d4": ["c4"],  # Removed connections to d5, e5, e4
    "e4": [],  # Removed connection to d4
    "f4": ["f3"],  # Removed connection to g5
    "g4": ["g3"],  # Removed connection to g5
    "h4": ["h3", "g4", "h5"],

    "a5": ["a4", "b5", "a6"],
    "b5": ["b4", "a5"],  # Removed connection to c5
    "c5": [],  # Removed all connections (walled on all sides)
    "d5": [],  # Removed connections to e5, d4, e4
    "e5": [],  # Removed connection to d5
    "f5": ["f4", "f6"],  # Removed connection to g5, g6
    "g5": ["g4"],  # Removed connections to f5, g6
    "h5": ["h4", "g5", "h6"],

    "a6": ["a5", "b6", "a7"],
    "b6": ["a6"],  # Removed connections to b5, c5, b7, c6, c7
    "c6": ["c7", "b6", "d6"],
    "d6": ["c6", "e6", "d7"],
    "e6": ["e5", "f6", "e7"],
    "f6": ["f5", "e6"],  # Removed connections to g5, g6, g7
    "g6": ["g7"],  # Removed connections to f6, f7
    "h6": ["h5"],  # Removed connection to h7

    "a7": ["a6", "b7", "a8"],
    "b7": ["a7"],  # Removed connections to b6, c6, c7, b8
    "c7": ["c6", "d7", "c8"],  # Removed connection to b7
    "d7": ["d6", "c7", "e7", "d8"],
    "e7": ["e6", "d7", "f7", "e8"],
    "f7": ["f6"],  # Removed connections to g7, g8
    "g7": ["g6"],  # Removed connections to f7, f8
    "h7": ["h6", "h8"],

    "a8": ["a7", "b8", "a9"],
    "b8": ["b7", "a8", "c8"],  # Removed connection to c7
    "c8": ["c7", "b8", "d8"],  # Removed connection to d7
    "d8": ["d7", "c8", "e8", "d9"],
    "e8": ["e7", "d8", "f8", "e9"],
    "f8": ["f7"],  # Removed connection to g7, g8
    "g8": ["g7"],  # Removed connection to f8
    "h8": ["h7", "g8", "h9"],

    "a9": ["a8", "b9"],
    "b9": ["b8", "a9", "c9"],
    "c9": ["c8", "b9", "d9"],
    "d9": ["d8", "c9", "e9"],
    "e9": ["e8", "d9", "f9"],
    "f9": ["f8", "e9", "g9"],
    "g9": ["g8", "f9", "h9"],
    "h9": ["h8", "g9"]
}

