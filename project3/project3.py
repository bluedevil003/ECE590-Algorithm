"""
Math 590
Project 3
Fall 2019

Partner 1: Yuhang Liu (yl655)
Partner 2: Kuan Wang (kw300)
Date:
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""
def detectArbitrage(currencies, tol=1e-15):
    # Set initial dist and prev
    for v in currencies.adjList:
        v.prev = None
        v.dist = math.inf  # Set all ve rtices to an infinite distance
    # Set the distance of starting point to be zero
    currencies.adjList[0].dist = 0

    # Iterate n-1 times (n is the number of vertexes)
    for index in range(0,len(currencies.adjList) - 1):
        # Look at each vertex
        for u in currencies.adjList:
            # Check each neighbor of u.
            # Update predictions and previous vertex
            for nei in u.neigh:
                # Only update if the new distance is shorter
                if u.dist + currencies.adjMat[u.rank][nei.rank] + tol < nei.dist:
                    nei.dist = u.dist + currencies.adjMat[u.rank][nei.rank]
                    nei.prev = u

    curr = None
    # Run for an extra iteration
    for u in currencies.adjList:
        for nei in u.neigh:
            # If any values change, there is a negative cost cycle
            if u.dist + currencies.adjMat[u.rank][nei.rank] + tol < nei.dist:
                # Record the vertex that had a change
                curr = u
                nei.prev = u
    # If no value changes, there is no negative cost cycle
    if curr is None:
        return []

    # follow the path backwards until a cycle is found
    a = [0 for k in range (len(currencies.adjList))]
    while a[curr.rank] == 0:
        a[curr.rank] += 1
        curr = curr.prev

    # Return the negative cycle in order
    begin = curr
    path = [begin.rank]
    curr = curr.prev
    while curr is not begin:
        path.insert(0, curr.rank)
        curr = curr.prev
    path.insert(0, begin.rank)
    ##### Your implementation goes here. #####
    return path
    ##### Your implementation goes here. #####

################################################################################

"""
rates2mat
"""
def rates2mat(rates):
    ##### Your implementation goes here. #####
    # Currently this only returns a copy of the rates matrix.
    return [[-math.log10(R) for R in row] for row in rates]
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
