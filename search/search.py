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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    # We use Position Search problem instance. It's getSuccessors method returns state, action and cost.
    # Stack has LIFO. list.pop() pops the last element inserted into it.
    fringe = util.Stack()
    # A set to keep track of nodes visited.
    # Set() avoids duplicates thus abiding to principle of not visiting a node more than once in Graph search.
    nodes_expanded = set()
    # For DFS cost does not matter so we pass it as 1.
    # We initially push start state co-ordinates and empty list of directions onto stack.
    fringe.push((problem.getStartState(), [], 0))
    # The loop executes until all the nodes are popped off the fringe.
    while not fringe.isEmpty():
        state, actions, cost = fringe.pop()
        # We check if the dequeued(popped) node's state is equal to goal state.(Goal test).
        # If True we return the list of actions for the pacman to reach its goal state.
        if problem.isGoalState(state):
            return actions
        # If the node is already visited we do not push its successors onto fringe thus we avoid cycles in graph search.
        if state in nodes_expanded:
            continue
        # If the node is not visited we mark it as visited and we push its successors onto the fringe.
        nodes_expanded.add(state)
        for successor_state, successor_action, step_cost in problem.getSuccessors(state):
            fringe.push((successor_state, actions + [successor_action], step_cost))
    # Added as defensive mechanism.
    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # We use Position Search problem instance. It's getSuccessors method returns state, action and cost.
    # Queue has FIFO property. list.pop() pops the last element inserted into it.
    # Here in util.Queue() we insert(push) element at index 0.
    fringe = util.Queue()
    # Set() avoids duplicates thus abiding to principle of not visiting a node more than once in Graph search.
    nodes_expanded = set()
    # For BFS cost does not matter so we pass it as 1.
    # We initially push start state co-ordinates and empty list of directions onto fringe.
    fringe.push((problem.getStartState(), [], 0))
    # The loop executes until all the nodes are dequeued.
    while not fringe.isEmpty():
        state, actions, cost = fringe.pop()
        # We check if the dequeued(popped) node's state is equal to goal state.(Goal test).
        # If True we return the list of actions for the pacman to reach its Goal state.
        if problem.isGoalState(state):
            return actions
        # If the node is already visited we do not push its successors onto fringe thus we avoid cycles in graph search.
        if state in nodes_expanded:
            continue
        # If the node is not visited we mark it as visited and we push its successors onto the fringe.
        nodes_expanded.add(state)
        for successor_state, successor_action, step_cost in problem.getSuccessors(state):
            fringe.push((successor_state, actions + [successor_action], step_cost))
    # Added as defensive mechanism.
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # We use Position Search problem instance. It's getSuccessors method returns state, action and cost.
    # PriorityQueue has priority based retrieval. list.pop() pops the least priority element inserted into it.
    fringe = util.PriorityQueue()
    # Set() avoids duplicates thus abiding to principle of not visiting a node more than once in Graph search.
    nodes_expanded = set()
    # For UCS cost matters so we pass it as 0 for initial state and priority as 0.
    # We initially push start state co-ordinates and empty list of directions, cost and priority onto fringe.
    fringe.push((problem.getStartState(), [], 0), 0)
    # The loop executes until all the nodes are dequeued.
    while not fringe.isEmpty():
        state, actions, cost = fringe.pop()
        # We check if the dequeued(popped) node's state is equal to goal state.(Goal test).
        # If True we return the list of actions for the pacman to reach its Goal state.
        if problem.isGoalState(state):
            return actions
        # If the node is already visited we do not push its successors onto fringe thus we avoid cycles in graph search.
        if state in nodes_expanded:
            continue
        # If the node is not visited we mark it as visited and we push its successors onto the fringe.
        nodes_expanded.add(state)
        for successor_state, successor_action, step_cost in problem.getSuccessors(state):
            # Here we push our priority as cummulative cost.
            fringe.push((successor_state, actions + [successor_action], cost + step_cost), cost + step_cost)
    # Added as defensive mechanism.
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # We use Position Search problem instance. It's getSuccessors method returns state, action and cost.
    # PriorityQueue has priority based retrieval. list.pop() pops the least priority element inserted into it.
    fringe = util.PriorityQueue()
    # Set() avoids duplicates thus abiding to principle of not visiting a node more than once in Graph search.
    nodes_expanded = set()
    # For astar cost matters so we pass it as 0 for initial state and priority as 0(cost)+heuristic of start state.
    # We initially push start state co-ordinates and empty list of directions, cost and priority onto fringe.
    fringe.push((problem.getStartState(), [], 0), 0 + heuristic(problem.getStartState(), problem))
    # The loop executes until all the nodes are dequeued.
    while not fringe.isEmpty():
        state, actions, cost = fringe.pop()
        # We check if the dequeued(popped) node's state is equal to goal state.(Goal test).
        # If True we return the list of actions for the pacman to reach its Goal state.
        if problem.isGoalState(state):
            return actions
        # If the node is already visited we do not push its successors onto fringe thus we avoid cycles in graph search.
        if state in nodes_expanded:
            continue
        # If the node is not visited we mark it as visited and we push its successors onto the fringe.
        nodes_expanded.add(state)
        for successor_state, action, step_cost in problem.getSuccessors(state):
            # Here we push our priority as cummulative cost + heuristic.
            fringe.push((successor_state, actions + [action], cost + step_cost),
                        cost + step_cost + heuristic(successor_state, problem))
    # Added as defensive mechanism
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
