###################################################################
#   CSE6521 Programming Homework 1                                #
#   1. Implement the A* graph search algorithm (`astar_search`)   #
###################################################################

import numpy as np 
from itertools import permutations
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

        
        return sum(s != g for (s, g) in zip(state, self.goal))


def reconstruct_path(current_state, came_from):
    reverse_path = []

    while current_state in came_from:
        current_state, current_action = came_from[current_state]
        reverse_path.append(current_action)

    reverse_path.reverse()
    return reverse_path


def astar_search(problem: EightPuzzle):
    """ TODO: implement A* search with the heuristic function you just defined. 
    
        This function should return the solution, i.e., the sequence of actions taken to reach
        from the initial state to the goal state, as a list. See the test file for example. """

    reached = set()
    frontier = PriorityQueue()
    came_from = {}

    g_score = {state: np.inf for state in permutations(problem.initial)}
    g_score[problem.initial] = 0

    f_score = {state: np.inf for state in permutations(problem.initial)}
    f_score[problem.initial] = problem.h(problem.initial)
    
    frontier.put((problem.h(problem.initial), problem.initial))
    
    while not frontier.empty():
        current_value, current_state = frontier.get()
        reached.add(current_state)
        if problem.goal_test(current_state):
            return reconstruct_path(current_state, came_from)

        possible_actions = problem.actions(current_state)
        for current_action in possible_actions:
            tentative_g_score = g_score[current_state] + 1
            next_state = problem.result(current_state, current_action)
            if (next_state not in reached) and (tentative_g_score < g_score[next_state]):
                came_from.update({next_state: (current_state, current_action)})
                g_score[next_state] = tentative_g_score
                f_score[next_state] = tentative_g_score + problem.h(next_state)
                frontier.put((f_score[next_state], next_state))
                

    return None
