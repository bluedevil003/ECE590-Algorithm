"""
Math 590
Project 2
Fall 2019

project2.py

Partner 1: Yuhang Liu (yl655)
Partner 2: Kuan Wang (kw300)
Date: 2019.11.08
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The shortest path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    ##### Your implementation goes here. #####

    """
    Both DFS and BFS are implemented by adjacency list.
    """
    if alg == 'DFS':
        """
        First initialize all the vertices in the maze.
        Set all the previous as None, the distance from start is infinity, and not visited before.
        """
        for v in maze.adjList:
            v.prev = None
            v.dist = math.inf  # Set all vertices to an infinite distance
            v.visited = False
        # First put the start vertex in the stack.
        myStack = Stack()
        myStack.push(maze.start)

        while not myStack.isEmpty():
            current = myStack.pop()

            # We have found the exit
            if current is maze.exit:
                break

            # If we have not reached the exit, search its neighbors not visited before.
            for newVertex in current.neigh:
                if not newVertex.visited:
                    # Set previous vertex, update the dist, and set it as visited
                    myStack.push(newVertex)
                    newVertex.visited = True
                    newVertex.dist = current.dist + 1
                    newVertex.prev = current

        """
        This part is used to compute the path.
        First we set the rank of start as the first element in the path.
        Then search the vertex in the reverse way, from exit to start, and insert the rank at the second position.
        Note that the second position is the index as 1
        Repeat until we reach the start.
        """
        path = [maze.start.rank]    
        while current is not maze.start:
            path.insert(1,current.rank)
            current = current.prev

    elif alg == 'BFS':

        """
        First initialize all the vertices in the maze.
        Set all the previous as None, the distance from start is infinity, and not visited before.
        """
        for v in maze.adjList:
            v.prev = None
            v.dist = math.inf  # Set all vertices to an infinite distance
            v.visited = False

        myQueue = Queue()
        myQueue.push(maze.start)

        while not myQueue.isEmpty():
            current = myQueue.pop()

            if current is maze.exit:
                break

            # If we have not reached the exit, search its neighbors not visited before.
            for newVertex in current.neigh:
                if not newVertex.visited:
                    # Set previous vertex, uodate the dist, and set it as visited
                    myQueue.push(newVertex)
                    newVertex.visited = True
                    newVertex.dist = current.dist + 1
                    newVertex.prev = current

        """
        This part is used to compute the path.
        First we set the rank of start as the first element in the path.
        Then search the vertex in the reverse way, from exit to start, and insert the rank at the second position.
        Note that the second position is the index as 1
        Repeat until we reach the start.
        """
        path = [maze.start.rank]
        while current is not maze.start:
            path.insert(1, current.rank)
            current = current.prev

    return path

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(True)
