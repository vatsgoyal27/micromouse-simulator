class BFS:
    def __init__(self, grid, start_cell, goal_cell):
        self.grid = grid                      # Maze with wall info at each cell
        self.start = tuple(start_cell)        # Convert list to tuple for hashing
        self.goal = tuple(goal_cell)
        self.explored = [[False for _ in range(18)] for _ in range(18)]
        self.parent = {}                      # To backtrack the shortest path

    def get_neighbors(self, r, c):
        neighbors = []

        # North
        if r > 0 and 'n' not in self.grid[r][c][2]:
            neighbors.append((r - 1, c))
        # South
        if r < 17 and 's' not in self.grid[r][c][2]:
            neighbors.append((r + 1, c))
        # East
        if c < 17 and 'e' not in self.grid[r][c][2]:
            neighbors.append((r, c + 1))
        # West
        if c > 0 and 'w' not in self.grid[r][c][2]:
            neighbors.append((r, c - 1))

        return neighbors

    def bfs_path(self):
        from collections import deque
        q = deque()
        q.append(self.start)
        self.explored[self.start[0]][self.start[1]] = True
        self.parent[self.start] = None

        while q:
            current = q.popleft()

            if current == self.goal:
                return self.reconstruct_path()

            for neighbor in self.get_neighbors(current[0], current[1]):
                if not self.explored[neighbor[0]][neighbor[1]]:
                    self.explored[neighbor[0]][neighbor[1]] = True
                    self.parent[neighbor] = current
                    q.append(neighbor)

        return None  # No path found

    def reconstruct_path(self):
        path = []
        current = self.goal

        while current is not None:
            path.append(list(current))  # Convert tuple back to list
            current = self.parent[current]

        path.reverse()
        return path

class DFS:
    def __init__(self, grid, start_cell, goal_cell):
        self.grid = grid
        self.start = tuple(start_cell)
        self.goal = tuple(goal_cell)
        self.explored = [[False for _ in range(18)] for _ in range(18)]
        self.parent = {}  # To reconstruct path

    def get_neighbors(self, r, c):
        neighbors = []

        # Note: DFS order can affect path. Change order as needed.
        # North
        if r > 0 and 'n' not in self.grid[r][c][2]:
            neighbors.append((r - 1, c))
        # South
        if r < 17 and 's' not in self.grid[r][c][2]:
            neighbors.append((r + 1, c))
        # East
        if c < 17 and 'e' not in self.grid[r][c][2]:
            neighbors.append((r, c + 1))
        # West
        if c > 0 and 'w' not in self.grid[r][c][2]:
            neighbors.append((r, c - 1))

        return neighbors

    def dfs_path(self):
        stack = [self.start]
        self.explored[self.start[0]][self.start[1]] = True
        self.parent[self.start] = None

        while stack:
            current = stack.pop()

            if current == self.goal:
                return self.reconstruct_path()

            for neighbor in self.get_neighbors(current[0], current[1]):
                if not self.explored[neighbor[0]][neighbor[1]]:
                    self.explored[neighbor[0]][neighbor[1]] = True
                    self.parent[neighbor] = current
                    stack.append(neighbor)

        return None  # No path found

    def reconstruct_path(self):
        path = []
        current = self.goal

        while current is not None:
            path.append(list(current))
            current = self.parent[current]

        path.reverse()
        return path

class DeadEndSolver:
    def __init__(self, grid, start_cell, goal_cell):
        self.grid = grid
        self.start = tuple(start_cell)
        self.goal = tuple(goal_cell)
        self.dead_end_mark = [[False for _ in range(18)] for _ in range(18)]

    def get_neighbors(self, r, c):
        neighbors = []

        if r > 0 and 'n' not in self.grid[r][c][2]:
            neighbors.append((r - 1, c))
        if r < 17 and 's' not in self.grid[r][c][2]:
            neighbors.append((r + 1, c))
        if c < 17 and 'e' not in self.grid[r][c][2]:
            neighbors.append((r, c + 1))
        if c > 0 and 'w' not in self.grid[r][c][2]:
            neighbors.append((r, c - 1))

        return neighbors

    def is_dead_end(self, r, c):
        if (r, c) == self.start or (r, c) == self.goal:
            return False
        count = 0
        for neighbor in self.get_neighbors(r, c):
            if not self.dead_end_mark[neighbor[0]][neighbor[1]]:
                count += 1
        return count <= 1

    def fill_dead_ends(self):
        changed = True
        while changed:
            changed = False
            for r in range(18):
                for c in range(18):
                    if not self.dead_end_mark[r][c] and self.is_dead_end(r, c):
                        self.dead_end_mark[r][c] = True
                        changed = True  # Keep checking until no more changes

    def reconstruct_path(self):
        from collections import deque

        # Simple BFS on remaining unmarked path
        q = deque()
        visited = [[False for _ in range(18)] for _ in range(18)]
        parent = {}
        q.append(self.start)
        visited[self.start[0]][self.start[1]] = True
        parent[self.start] = None

        while q:
            r, c = q.popleft()
            if (r, c) == self.goal:
                break
            for nr, nc in self.get_neighbors(r, c):
                if not visited[nr][nc] and not self.dead_end_mark[nr][nc]:
                    visited[nr][nc] = True
                    parent[(nr, nc)] = (r, c)
                    q.append((nr, nc))

        # Backtrack path
        path = []
        current = self.goal
        while current is not None:
            path.append(list(current))
            current = parent.get(current)

        path.reverse()
        return path

    def solve(self):
        self.fill_dead_ends()
        return self.reconstruct_path()

from collections import deque

class FloodFill:
    def __init__(self, grid, start_cell, goal_cells):
        self.grid = grid
        self.start = tuple(start_cell)
        self.goal_cells = [tuple(g) for g in goal_cells]
        self.rows = 18
        self.cols = 18
        self.cost = [[255 for _ in range(self.cols)] for _ in range(self.rows)]
        self.parent = {}  # For path reconstruction

    def get_neighbors(self, r, c):
        neighbors = []
        if r > 0 and 'n' not in self.grid[r][c][2]:
            neighbors.append((r - 1, c))
        if r < self.rows - 1 and 's' not in self.grid[r][c][2]:
            neighbors.append((r + 1, c))
        if c < self.cols - 1 and 'e' not in self.grid[r][c][2]:
            neighbors.append((r, c + 1))
        if c > 0 and 'w' not in self.grid[r][c][2]:
            neighbors.append((r, c - 1))
        return neighbors

    def fill_cost_map(self):
        q = deque()
        for goal in self.goal_cells:
            gr, gc = goal
            self.cost[gr][gc] = 0
            q.append(goal)
            self.parent[goal] = None  # Goal has no parent

        while q:
            r, c = q.popleft()
            for nr, nc in self.get_neighbors(r, c):
                if self.cost[nr][nc] == 255:  # Unvisited
                    self.cost[nr][nc] = self.cost[r][c] + 1
                    self.parent[(nr, nc)] = (r, c)
                    q.append((nr, nc))

    def reconstruct_path(self):
        path = []
        current = self.start

        while current is not None:
            path.append(list(current))
            current = self.parent.get(current)

        return path

    def find_path(self):
        self.fill_cost_map()

        if self.cost[self.start[0]][self.start[1]] == 255:
            return None  # No path to any goal

        return self.reconstruct_path()

import heapq

class AStar:
    def __init__(self, grid, start_cell, goal_cell):
        self.grid = grid
        self.start = tuple(start_cell)
        self.goal = tuple(goal_cell)
        self.rows = 18
        self.cols = 18
        self.parent = {}
        self.cost_so_far = [[float('inf') for _ in range(self.cols)] for _ in range(self.rows)]

    def get_neighbors(self, r, c):
        neighbors = []
        if r > 0 and 'n' not in self.grid[r][c][2]:
            neighbors.append((r - 1, c))
        if r < self.rows - 1 and 's' not in self.grid[r][c][2]:
            neighbors.append((r + 1, c))
        if c < self.cols - 1 and 'e' not in self.grid[r][c][2]:
            neighbors.append((r, c + 1))
        if c > 0 and 'w' not in self.grid[r][c][2]:
            neighbors.append((r, c - 1))
        return neighbors

    def heuristic(self, cell):
        # Manhattan distance to the goal
        return abs(cell[0] - self.goal[0]) + abs(cell[1] - self.goal[1])

    def find_path(self):
        heap = []
        heapq.heappush(heap, (0 + self.heuristic(self.start), 0, self.start))  # (priority, cost, position)
        self.parent[self.start] = None
        self.cost_so_far[self.start[0]][self.start[1]] = 0

        while heap:
            _, cost, current = heapq.heappop(heap)

            if current == self.goal:
                return self.reconstruct_path()

            for neighbor in self.get_neighbors(*current):
                nr, nc = neighbor
                new_cost = self.cost_so_far[current[0]][current[1]] + 1

                if new_cost < self.cost_so_far[nr][nc]:
                    self.cost_so_far[nr][nc] = new_cost
                    self.parent[neighbor] = current
                    priority = new_cost + self.heuristic(neighbor)
                    heapq.heappush(heap, (priority, new_cost, neighbor))

        return None  # No path

    def reconstruct_path(self):
        path = []
        current = self.goal

        while current is not None:
            path.append(list(current))
            current = self.parent.get(current)

        path.reverse()  # Optional
        return path

class Dijkstra:
    def __init__(self, grid, start_cell, goal_cell):
        self.grid = grid
        self.start = tuple(start_cell)
        self.goal = tuple(goal_cell)
        self.rows = 18
        self.cols = 18

    def get_neighbors(self, r, c):
        neighbors = []
        if r > 0 and 'n' not in self.grid[r][c][2]:
            neighbors.append((r - 1, c))
        if r < self.rows - 1 and 's' not in self.grid[r][c][2]:
            neighbors.append((r + 1, c))
        if c < self.cols - 1 and 'e' not in self.grid[r][c][2]:
            neighbors.append((r, c + 1))
        if c > 0 and 'w' not in self.grid[r][c][2]:
            neighbors.append((r, c - 1))
        return neighbors

    def find_path(self):
        open_set = []
        heapq.heappush(open_set, (0, self.start))  # (g_score, cell)
        parent = {self.start: None}
        g_score = {self.start: 0}

        while open_set:
            current_g, current = heapq.heappop(open_set)

            if current == self.goal:
                return self.reconstruct_path(parent)

            for neighbor in self.get_neighbors(current[0], current[1]):
                tentative_g = current_g + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    heapq.heappush(open_set, (tentative_g, neighbor))
                    parent[neighbor] = current

        return None  # No path

    def reconstruct_path(self, parent):
        path = []
        current = self.goal
        while current is not None:
            path.append(list(current))
            current = parent.get(current)
        path.reverse()
        return path
