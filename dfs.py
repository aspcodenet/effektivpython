class PathFinder:

    def __init__(self, maze):
        self.maze = maze
        self.resulting_path = []  # Fungerar som en stack (använder append/pop)
        self.visited = {}  

    def get_path(self):
        # Eftersom Python-listan innehåller elementen i ordning returnerar vi en kopia.
        return list(self.resulting_path)

    def dfs(self, y, x, dest_row, dest_col):
        thisitem = f"{x},{y}"
        print(f"TRYING: {thisitem}")
        self.resulting_path.append(thisitem)

        # Är vi framme? return True
        if x == dest_col and y == dest_row:
            return True

        # Har vi redan varit här? pop och return False
        if self.visited.get(thisitem, False):
            self.resulting_path.pop()
            return False

        self.visited[thisitem] = True

        # LEFT
        if self.is_valid(y, x - 1):
            if self.dfs(y, x - 1, dest_row, dest_col):
                return True

        # DOWN
        if self.is_valid(y + 1, x):
            if self.dfs(y + 1, x, dest_row, dest_col):
                return True

        # RIGHT
        if self.is_valid(y, x + 1):
            if self.dfs(y, x + 1, dest_row, dest_col):
                return True

        # UP
        if self.is_valid(y - 1, x):
            if self.dfs(y - 1, x, dest_row, dest_col):
                return True

        self.resulting_path.pop()
        return False

    def is_valid(self, y, x):
        if x < 0:
            return False
        if x >= len(self.maze[0]):
            return False
        if y >= len(self.maze):
            return False
        if y < 0:
            return False
        if self.maze[y][x] == 1:
            return False
        return True


if __name__ == "__main__":
    maze = [
        [0, 1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
    ]

    path_finder = PathFinder(maze)
    found = path_finder.dfs(0, 0, 0, 2)

    if found:
        print("RESULT: ")
        for s in path_finder.get_path():
            print(s)