# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import*
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    stack = Stack()
    visited = set()
    stack.push((problem.getStartState(), []))

    start_time = time.perf_counter()

    while not stack.isEmpty():
        current_state, path = stack.pop()

        if current_state in visited:
            continue
        visited.add(current_state)

        if problem.isGoalState(current_state):
            execution_time = time.perf_counter() - start_time
            path_cost = problem.getCostOfActions(path)
            print(f"DFS Execution Time: {execution_time:.6f} seconds")
            print(f"DFS Total Path Length: {len(path)}")
            print(f"DFS Total Path Cost: {path_cost}")
            return path

        for successor, action, step_cost in problem.getSuccessors(current_state):
            if successor not in visited:
                stack.push((successor, path + [action]))

    execution_time = time.perf_counter() - start_time
    print(f"DFS Execution Time: {execution_time:.6f} seconds")
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    queue = Queue()
    visited = set()
    queue.push((problem.getStartState(), []))

    start_time = time.perf_counter()

    while not queue.isEmpty():
        current_state, path = queue.pop()

        if current_state in visited:
            continue
        visited.add(current_state)

        if problem.isGoalState(current_state):
            execution_time = time.perf_counter() - start_time
            path_cost = problem.getCostOfActions(path)
            print(f"BFS Execution Time: {execution_time:.6f} seconds")
            print(f"BFS Total Path Length: {len(path)}")
            print(f"BFS Total Path Cost: {path_cost}")
            return path

        for successor, action, step_cost in problem.getSuccessors(current_state):
            if successor not in visited:
                queue.push((successor, path + [action]))

    execution_time = time.perf_counter() - start_time
    print(f"BFS Execution Time: {execution_time:.6f} seconds")
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    pq = PriorityQueue()
    visited = set()
    pq.push((problem.getStartState(), []), 0)

    start_time = time.perf_counter()

    while not pq.isEmpty():
        current_state, path = pq.pop()

        if current_state in visited:
            continue
        visited.add(current_state)

        if problem.isGoalState(current_state):
            execution_time = time.perf_counter() - start_time
            path_cost = problem.getCostOfActions(path)
            print(f"UCS Execution Time: {execution_time:.6f} seconds")
            print(f"UCS Total Path Length: {len(path)}")
            print(f"UCS Total Path Cost: {path_cost}")
            return path

        for successor, action, step_cost in problem.getSuccessors(current_state):
            if successor not in visited:
                new_path = path + [action]
                total_cost = problem.getCostOfActions(new_path)
                pq.push((successor, new_path), total_cost)

    execution_time = time.perf_counter() - start_time
    print(f"UCS Execution Time: {execution_time:.6f} seconds")
    return []
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch