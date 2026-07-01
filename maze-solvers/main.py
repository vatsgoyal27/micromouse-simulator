from turtle import tracer, Screen
from maze import grid
from logic import BFS, DFS, DeadEndSolver, FloodFill, AStar, Dijkstra
from drawers import Mouse
import time

screen = Screen()
screen.setworldcoordinates(0, 0, 400, 400)

tracer(0)
my_mouse_bfs = Mouse("blue")
my_mouse_dfs = Mouse("green")
my_mouse_dead = Mouse("red")
my_mouse_flood = Mouse("yellow")
my_mouse_astar = Mouse("cyan")
my_mouse_dij = Mouse("magenta")
grid_mouse = Mouse("black")
grid_mouse.draw_grid()
grid_mouse.draw_walls(grid)
grid_mouse.delete()
screen.update()
tracer(1)

target = [8,9]

ast = AStar(grid, my_mouse_astar.mouse_pos, target)
ast_path = ast.find_path()
while ast_path:
    my_mouse_astar.move_actual(ast_path[0])
    ast_path.pop(0)

dij = Dijkstra(grid, my_mouse_dij.mouse_pos, target)
dij_path = dij.find_path()
while dij_path:
    my_mouse_dij.move_actual(dij_path[0])
    dij_path.pop(0)

ff = FloodFill(grid, my_mouse_flood.mouse_pos, [target])
ff_path = ff.find_path()
while ff_path:
    my_mouse_flood.move_actual(ff_path[0])
    ff_path.pop(0)

b = BFS(grid, my_mouse_bfs.mouse_pos, target)
shortest_path = b.bfs_path()
while shortest_path:
    my_mouse_bfs.move_actual(shortest_path[0])
    shortest_path.pop(0)

d = DFS(grid, my_mouse_dfs.mouse_pos, target)
faster_path = d.dfs_path()
while faster_path:
    my_mouse_dfs.move_actual(faster_path[0])
    faster_path.pop(0)

f = DeadEndSolver(grid, my_mouse_dead.mouse_pos, target)
dead_path = f.solve()
while dead_path:
    my_mouse_dead.move_actual(dead_path[0])
    dead_path.pop(0)

screen.exitonclick()

