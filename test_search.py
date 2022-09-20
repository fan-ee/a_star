import pytest
from search import *

eight_puzzle_test1 = EightPuzzle((1, 2, 3, 4, 5, 6, 0, 7, 8))
eight_puzzle_test2 = EightPuzzle((1, 0, 6, 8, 7, 5, 4, 2, 3), (0, 1, 2, 3, 4, 5, 6, 7, 8))

def test_heuristic():
    assert eight_puzzle_test1.h(eight_puzzle_test1.initial) == 3
    assert eight_puzzle_test1.h(eight_puzzle_test2.initial) == 8

def test_astar_search():
    assert astar_search(eight_puzzle_test1) == ['RIGHT', 'RIGHT']
    assert astar_search(eight_puzzle_test2) == ['DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT',
                                                'UP', 'UP', 'LEFT', 'DOWN', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT',
                                                'UP', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'UP',
                                                'LEFT', 'LEFT']
    
if __name__ == '__main__':
    pytest.main()
