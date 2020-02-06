"""
Math 590
Project 4
Fall 2019

Partner 1: Yuhang Liu (yl655)
Partner 2: Kuan Wang (kw300)
Date: Dec 4th, 2019
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p4priorityQueue import *

################################################################################

"""
Prim's Algorithm
"""
def prim(adjList, adjMat):

    ## Initialize all costs to infinity and prev to null. Also all the vertices have not been visited.
    for v in adjList:
        v.prev = None
        v.cost = math.inf  # Set all vertices to an infinite distance
        v.visited = False

    #Pick an arbitrary start vertex and set cost to 0.
    start = adjList[0]
    start.cost = 0

    # Make the priority queue using cost for sorting.
    pq = PriorityQueue(adjList)

    while not pq.isEmpty():
        # Get the next unvisited vertex and visit it.
        next = pq.deleteMin()
        next.visited = True
        # For each edge out of u.
        for u in next.neigh:
            # If the edge leads out, update.
            if u.visited == False and adjMat[next.rank][u.rank] < u.cost:
                u.cost = adjMat[next.rank][u.rank]
                u.prev = next
    return

################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
"""
def kruskal(adjList, edgeList):

    # Initialize the empty MST.
    X = []
    # Initialize all singleton sets for each vertex.
    for v in adjList:
        makeset(v)

    # Loop through the edges in increasing order.
    for e in edgeList:
        r1 = find(e.vertices[0])
        r2 = find(e.vertices[1])

        # If the min edge crosses a cut, add it to our MST.
        if not r1.isEqual(r2):
            union(r1, r2)
            X.append(e)
    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
"""
def makeset(v):
    #create a singleton set containing vertex v
    v.pi = v
    v.height = 0
    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

"""
def find(v):
    #find which set vertex v belongs to (used for finding cuts)
    #Path compression is used in it.
    if not v.isEqual(v.pi):
        v.pi = find(v.pi)
    return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
    #Merge the sets containing vertices u and v
    ru = find(u)
    rv = find(v)

    if ru == rv:
        return
    if ru.height > rv.height:
        rv.pi = ru
    elif ru.height < rv.height:
        ru.pi = rv
    else:
        # Same height, break tie.
        ru.pi = rv
        # Tree got taller, increment rv.height.
        rv.height += 1
    return

################################################################################

"""
TSP
"""
def tsp(adjList, start):

    # Set all the vertices as unvisited before.
    tour = []
    for v in adjList:
        v.visited = False
    #tour.append(start.rank)
    s = []
    s.append(start)
    start.visited = True

    # Using DFS to search for the path
    # If the stack is not empty:
    while len(s) != 0:
        current = s.pop()
        tour.append(current.rank)
        # Searching the element in the MST
        for nei in current.mstN:
            if nei.visited == False:
                nei.visited = True
                s.append(nei)

    tour.append(start.rank)
    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p4tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
