###################################################################
#   CSE6521 Programming Homework 1                                #
#   1. Implement the A* graph search algorithm (`astar_search`)   #
###################################################################

from queue import PriorityQueue

class EightPuzzle:
    """ The problem of sliding tiles numbered from 1 to 8 on a 3x3 board, where one of the
    squares is a blank. A state is represented as a tuple of length 9, where element at
    index i represents the tile number at index i (0 if it's an empty square) """

    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        """ Define goal state and initialize a problem """
        self.initial = initial
        self.goal = goal

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""

        return state.index(0)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        # blank is the index of the blank square
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % 3 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 3:
            possible_actions.remove('UP')
        if index_blank_square % 3 == 2:
            possible_actions.remove('RIGHT')
        if index_blank_square > 5:
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def h(self, state):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles. """
        # new heuristic: from the ABSOLUTE difference between goal state and current state, add
        # diff % 3 and diff // 3 to get manhattan distance

        h_cost = 0
        for i in range(8):
            distance = abs(state.index(i) - self.goal.index(i))
            h_cost = distance % 3 + distance // 3

        return h_cost


class Node:
    # to keep track of the visited nodes
    def __init__(self, current, path, h):
        self.current = current
        self.path = path        # should be a list of previous states or somethin
        self.h = h



def astar_search(problem):
    """ TODO: implement A* search with the heuristic function you just defined. 
    
        This function should return the solution, i.e., the sequence of actions taken to reach
        from the initial state to the goal state, as a list. See the test file for example. """
    h = problem.h

    state = (1, 2, 3,5)

    h_value = puzzle.h(state)

    return NotImplementedError
