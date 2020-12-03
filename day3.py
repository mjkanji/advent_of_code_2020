import numpy as np

# This function solves for any arbirary map
def num_trees(s, right, down):
    '''
    Counts the number of trees given a slope going a certain number of steps down and right. It also automatically calculates the number
        of times the map must be repeated horizontally in order to avoid boundary issues.

    Args:
        - s: the given input/map as a string
        - right: number of steps to go right per iteration
        - down: number of steps to go down per iteration
    '''
    X = np.array([list( x.replace(".", '0').replace("#", "1") ) for x in s.split("\n")]).astype(int)
    h, w = X.shape
    reps = int(h*right/w) + 1
    X = np.hstack([X] * reps)
    return np.diag(X[::down, ::right]).sum()


### Example ###
s_test = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''

### Part 1 ###

ans_1 = num_trees(s_test, 3, 1)
print(ans_1) # Return 7, as in the given example

### Part 2 ###
slopes = [
    (1,1),
    (3, 1),
    (5,1),
    (7, 1),
    (1,2)
] # A list of tuples of the form (right, down)

ans_2 = np.array([num_trees(s_test, *x) for x in slopes]).astype("int64").prod()
print(ans_2) # Return 336, as in the given example