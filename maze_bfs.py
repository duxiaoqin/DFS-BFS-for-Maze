# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 21:41:31 2018

@author: duxiaoqin
Functions:
    (1)BFS for Maze;
"""

from myqueue import Queue
from graphics import *
from myarray2d import Array2D
from maze import Maze
from mazedraw import MazeDraw

def BFS(maze, v, goal, came_from):
    frontier = Queue()
    frontier.enqueue(v)
    came_from[v] = None
    while not frontier.is_empty():
        v = frontier.dequeue()
        if maze[v[0], v[1]] == Maze.EMPTY:
            if v == goal:
                return v
            else:
                maze[v[0], v[1]] = Maze.OCCUPIED
                for w in maze.getAllMoves(v[0], v[1]):
                    if maze[w[0], w[1]] == Maze.EMPTY:
                        frontier.enqueue(w)
                        came_from[w] = v
    return None

def drawPath(win, maze, came_from):
    current = maze.goal
    while current != maze.start:
        next = came_from[current]
        line = Line(Point(next[1]+1+0.5, \
                          maze.numRows()-next[0]+1-0.5), \
                    Point(current[1]+1+0.5, \
                          maze.numRows()-current[0]+1-0.5))
        line.setOutline('white')
        line.setArrow('last')
        line.draw(win)
        
        current = next

def main():
    win = GraphWin('BFS for Maze', 600, 600, autoflush=False)
    maze = Maze(20, 20)
    mazedraw = MazeDraw(win, maze)
    mazedraw.draw()
    came_from = {}
    found = BFS(maze, maze.start, maze.goal, came_from)
    print(found)
    text = Text(Point(11, 0.5), '')
    if found == maze.goal:
        text.setText('Goal found!')
        drawPath(win, maze, came_from)
    else:
        text.setText('Goal not found!')
    text.draw(win)
        
    while win.checkKey() != 'Escape':
        pass
    win.close()
    
if __name__ == '__main__':
    main()