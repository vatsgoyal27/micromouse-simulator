# Micromouse Maze Project

A collection of Python-based maze simulation and generation tools, exploring pathfinding and maze-building algorithms through visual simulation.

## Folders

### `micromouse sim/`
A Micromouse simulator that navigates a virtual maze using the floodfill algorithm, visualized with Python's `turtle` module. The mouse senses its surroundings step-by-step and updates a live cost map to find its way to the goal.

### `maze-solvers/`
A multi-algorithm maze solver, also built with `turtle`, that runs six different pathfinding algorithms (Flood Fill, BFS, DFS, Dead-End Solver, Dijkstra, A*) side by side on the same maze — visualizing how each one explores and solves it differently.

### `maze-generators/`
A `pygame`-based visual tool implementing ten different maze generation algorithms (DFS, Prim's, Hunt-and-Kill, Binary Tree, Origin Shifter, Sidewinder, Kruskal's, Growing Tree, Wilson's, Aldous-Broder), each animated step-by-step as the maze is constructed.

## Requirements

- Python 3.9+
- `pygame` (only required for `maze-generator-visualizer/`)

## License

This project is licensed under the [MIT License](LICENSE).
