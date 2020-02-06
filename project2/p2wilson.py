"""
Math 590
Project 2
Fall 2019

p2wilson.py
"""

# Import random.
import random

"""
Node Class - used for the graph in Wilson's algorithm.
"""
class Node:

    """
    Class attributes:
    
    rank    # The rank of this node.
    neigh   # The list of neighbors in the original graph.
    neighST # The list of neighbors IN THE SPANNING TREE (ST).
    onPath  # A flag to check if the node is already on the path.
    inST    # A flag to check if the node is already in the ST.
    prev    # The previous node on the path.
    """

    """
    __init__ function to initialize the node.
    """
    def __init__(self, rank):

        self.rank = rank     # Set the rank of this node.
        self.neigh = []      # Set the graph neighbors.
        self.neighST = []    # Set the ST neighbors.
        self.onPath = False  # Not on the path yet.
        self.inST = False    # Not in the ST yet.
        self.prev = None     # No previous node on path yet.
        return

    """
    __repr__ function to print a node.
    Note: only prints the rank!
    """
    def __repr__(self):
        return 'Rank: %d' % self.rank

    """
    isEqual function compares this Node to an input Node object.
    Note: only needs to compare the rank!
    """
    def isEqual(self,node):
        return self.rank == node.rank

################################################################################

"""
wilson function performs Wilson's algorithm to uniformly generate a random
spanning tree for an input graph, input as an adjacency list of Node objects.
"""
def wilson(graph):
    # Create a list of ranks and randomly shuffle them.
    # Note: we don't want to shuffle the actual adjacency list because
    #       a Node's index corresponds to its rank...
    randNodesToVisit = list(range(len(graph)))
    random.shuffle(randNodesToVisit)

    # Now put the first randomly selected Node in the ST.
    graph[randNodesToVisit[0]].inST = True

    # Loop over all of the nodes in random order.
    for ind in randNodesToVisit:
        # Set the currNode to visit.
        currNode = graph[ind]
        
        # If this node is already in the ST, move along.
        if currNode.inST:
            continue

        # Start the path with this node, and reset its prev value.
        currNode.onPath = True
        currNode.prev = None

        # While the current node has not yet reached our ST...
        while not currNode.inST:
            # Choose a random neighbor of the node.
            r = random.randint(0,len(currNode.neigh)-1)
            nextNode = currNode.neigh[r]

            # Check if this next node is already on the path (and so
            # would create a loop if visited again).
            if not nextNode.onPath:
                # No loop, add to path and move on.
                nextNode.onPath = True
                nextNode.prev = currNode
                currNode = nextNode
            else:
                # Remove the loop by deleting this part of the path.
                while not currNode.isEqual(nextNode):
                    currNode.onPath = False
                    currNode = currNode.prev

        # Now currNode is in the spanning tree, and the chain of prev
        # values can all be added to the spanning tree as well.
        while currNode.prev is not None:
            currNode.inST = True
            currNode.onPath = False
            currNode.neighST.append(currNode.prev)
            currNode.prev.neighST.append(currNode)
            currNode = currNode.prev

        # Back at the start of the path.
        # Add to spanning tree.
        # Remove from the path.
        currNode.inST = True
        currNode.onPath = False
            
    return

################################################################################

"""
createRandMaze function will use Wilson's algorithm to generate a random maze
of the spcified size given as number of rooms per side of the maze. The returned
maze will have a row/column size of 2*numRooms+1.
"""
def createRandMaze(numRooms=12):
    # Create an adjacency list with numRooms^2 number of Nodes.
    graph = []
    for rank in range(numRooms**2):
        graph.append(Node(rank))

    # Now add the edges to the graph (i.e., fill out the neigh lists).
    for currNode in graph:
        # Get the current rank.
        r = currNode.rank

        # Fill the 'north' neighbor.
        if r >= numRooms:
            currNode.neigh.append(graph[r-numRooms])

        # Fill the 'south' neighbor.
        if r <= numRooms**2 - 1 - numRooms:
            currNode.neigh.append(graph[r+numRooms])

        # Fill the 'west' neighbor.
        if r % numRooms != 0:
            currNode.neigh.append(graph[r-1])

        # Fill the 'east' neighbor.
        if r % numRooms != numRooms-1:
            currNode.neigh.append(graph[r+1])

    # Now that the graph is created, run Wilson's to get the spanning tree.
    wilson(graph)

    # Store the maze size.
    mazeSize = 2*numRooms + 1

    # Create our initial, filled 'maze', which will be represented as a list
    # of lists filled with 0 (room/hallway) or 1 (wall).
    maze = [[1 for x in range(mazeSize)] for y in range(mazeSize)]

    # Now loop over each node in the graph, open the corresponding room in
    # the maze, and open any hallways leading out of the room.
    for node in graph:
        # Get the node's ROOM row and column indices.
        roomRow = node.rank//numRooms
        roomCol = node.rank % numRooms

        # Convert these room indices into indices in the full maze,
        # noting that the maze is lined with walls, and rooms have
        # walls between them.
        mazeRow = 2*roomRow + 1
        mazeCol = 2*roomCol + 1

        # Open this room in the maze.
        maze[mazeRow][mazeCol] = 0

        # Now look at this node's spanning tree neighbors.
        for nNode in node.neighST:
            # Check which hallways to open.
            if nNode.rank > node.rank+1:
                # Open southern hallway.
                maze[mazeRow+1][mazeCol] = 0
            elif nNode.rank > node.rank:
                # Open eastern hallway.
                maze[mazeRow][mazeCol+1] = 0
            elif nNode.rank >= node.rank-1:
                # Open western hallway.
                maze[mazeRow][mazeCol-1] = 0
            else:
                # Open northern hallway.
                maze[mazeRow-1][mazeCol] = 0

    # Now the interior maze has been created. Add the start and end.
    maze[0][1] = 0
    maze[mazeSize-1][mazeSize-2] = 0

    # Return the completed maze.
    return maze
