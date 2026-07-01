# Micromouse Maze Project

A collection of Python-based maze simulation and generation tools, exploring pathfinding and maze-building algorithms through visual simulation.

## Folders

### `micromouse sim/`
A Micromouse simulator that navigates a virtual maze using the floodfill algorithm, visualized with Python's `turtle` module. The mouse senses its surroundings step-by-step and updates a live cost map to find its way to the goal.

### `maze-solvers/`
A multi-algorithm maze solver, also built with `turtle`, that runs six different pathfinding algorithms (Flood Fill, BFS, DFS, Dead-End Solver, Dijkstra, A*) side by side on the same maze — visualizing how each one explores and solves it differently.
This project simulates navigating a grid-based maze using different pathfinding algorithms.

Built with Python and `turtle`, the simulation visually demonstrates how each algorithm explores and solves the maze.

## Project Structure

- **main.py**  
  Runs the maze simulation with all three solvers. Visualizes their paths in different colors:  
  - Yellow: Flood Fill (uses a dynamic cost map)
  - Blue: BFS (shortest path)  
  - Green: DFS (non-optimal path)  
  - Red: Dead-End Solver (eliminates all dead ends)
  - Magenta: Dijkstra (uses a cost function)
  - Cyan: A* (uses Dijkstra with an additional heuristic for estimated distance)

- **maze.py**  
  Generates the grid and walls. Includes functions to add or remove walls and builds a complex maze with loops and decoys.

- **logic.py**  
  Contains the core logic for solvers:
  - `BFS`: Finds the shortest path.
  - `DFS`: Explores deeply and may find non-optimal paths.
  - `DeadEndSolver`: Fills dead ends to isolate the true path.
  - `FloodFill`: Finds the shortest path using a cost map.
  - `Dijkstra`: Finds the path using a cost function.
  - `AStar`: Finds the path using Dijkstra with an extra heuristic estimate.

- **drawers.py**  
  Defines the `Mouse` class used to draw the maze, walls, and animate the robot's movement on the grid.

---

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

You'll see a visual simulation window. Each algorithm will take its turn solving the same maze.

---
---

### `maze-generators/`
A **visual maze generation tool** using `pygame` in Python, **with multiple algorithms**:  
Each algorithm runs step-by-step and visualizes the maze construction live with animated updates.

## File Structure

```
.
├── main.py                # Main entry point; handles pygame window and maze generation loop
├── cell.py                # Defines individual maze cells (walls, colors, draw logic)
├── grid.py                # Utility to create the grid of cells
├── mazemakers.py          # Contains all maze generation algorithms and shared logic
└── README.md              # You are here
```

---

## How to Run

Install pygame if not already installed:
```bash
pip install pygame
```

###  To Run the Visualizer:
```bash
python main.py
```

---

## Algorithms Implemented

### 1. **Depth-First Search (DFS) Maze Generator**
- Carves out a path by diving deep and backtracking.
- Stack-based approach.
- Visualization:
  - Orange cells: Currently being processed.
  - Blue fill: Finalized path.

---

### 2. **Prim's Algorithm**
- Randomly selects frontier cells and connects to an adjacent visited cell.
- Ensures uniform spread.
- Visualization:
  - Orange cells: Frontier set (border of the current maze).
  - Blue fill: Finalized path.

---

### 3. **Hunt-and-Kill Algorithm**
- Alternates between random walks ("kill mode") and scanning unvisited cells ("hunt mode").
- Quicker and easy to implement.
- Visualization:
  - Orange cells: Path during random walk.
  - Blue cells: Cells scanned during hunt.

---

### 4. **Binary tree Algorithm**
- Iterates through the entire grid.
- Is the simplest in logic, carves a path randomly north or west - that's it.
- Visualization:
  - Blue fill: Finalized path.

---

### 5. **Origin Shifter Algorithm**
- Initializes a "perfect" maze with a fully linked "tree".
- Each step shifts the “origin” by rewiring paths using directional arrows.
- If a wall exists, it removes the new wall and restores the old one.
- Visualization:
  - Blue fill: Modified cell.
  - Black fill: Unmodified cell.

---

### 6. **Sidewinder Algorithm**
- Connects entire first row.
- Processes each row, either by creating a "run" set by removing walls to the east, or by creating a connection of this "run" set to the upper row by a north passage.
- Visualization:
  - Blue fill: Finalized cell.
  - Orange fill: Cells in current "run" set.

---

### 7. **Kruskals Algorithm**
- Treats each cell as its own disjoint set.
- Processes random walls; removes them only if they connect disjoint sets.
- Ensures no cycles while creating a fully connected maze.
- Visualization:
  - Blue fill: Finalized cell.
  - Orange fill: Currently merged set.

---

### 8. **Growing Tree Algorithm**
- Starts with one cell and grows a path by choosing neighbors.
- Behavior depends on selection strategy (e.g., newest, random), backtracks via this strategy to select a new growing point when exceeding set length or when it has no valid neighbors.
- Visualization:
  - Blue fill: Finalized cell.
  - Orange fill: Actively growing cells.

---

### 9. **Wilsons Algorithm**
- Begins by selecting one random cell and marking it as part of the maze.
- Repeatedly performs a loop-erased random walk (a random walk that removes any loops it creates as it goes) from a random unvisited cell until it connects to the maze.
- On reaching the maze, the path is finalized.
- Can toggle backtrack prevention for random walk to increase generation speed
- Visualization:
  - Blue fill: Finalized cell.
  - Orange fill: Active walk path.

---

### 10. **Aldous Broder Algorithm**
- Starts at a random cell and walks randomly to neighbors.
- Removes walls only when visiting a cell for the first time.
- Repeats until all cells are visited, creating a perfect maze.
- Visualization:
  - Blue fill: Finalized cell.

---

## Cell Color Codes

| Color         | Meaning                          |
|---------------|----------------------------------|
| 🟩 Green       | Start cell                        |
| 🟨 Yellow      | End cell                          |
| 🟦 Blue        | Finalized (visited) cell          |
| 🟧 Orange      | Cell currently being processed    |
| ⬛ Black       | Wall / Undiscovered               |
| ⬜ White lines | Maze cell walls                   |

---

## Customization

You can change the maze generation algorithm by modifying this line in `main.py`:

```python
generator = <codename>_gen(maze_grid, ROWS, COLS, 0, 0, ROWS-1, COLS-1)
```

Available options:
```python
dfs_gen, hak_gen, prims_gen, btree_gen, ori_gen, 
side_gen, krus_gen, grow_gen, wil_gen, albr_gen
```

Just replace as required

---
---

## Requirements

- Python 3.9+
- `pygame` (only required for `maze-generator-visualizer/`)

## License

This project is licensed under the [MIT License](LICENSE).
