#Input: NumIterations, ProblemSize, SearchSpace
#Output: The best!

import random

# Create a new random vector
def random_vector( search_space ):
    random_vector = [0] * len(search_space)
    for i, vec in enumerate( search_space ):
        random_vector[i] = \
            vec[0] + \
            ((vec[1] - vec[0]) * random.random())
    return random_vector

# Cost function
def objective_function( candidate ):
    return sum([ i ** 2.0 for i in candidate])    

def random_search( number_of_iterations, search_space):
    best = None
    
    for i in range(0, number_of_iterations):
        candidate = {}
        candidate.setdefault('vector', random_vector( search_space ))
        candidate.setdefault('cost', objective_function( candidate['vector'] ))
        if best is None or candidate['cost'] < best['cost']:
            best = candidate
    return best

problem_size = 2
number_of_iterations = 10000
search_space = [[-5, +5]] * problem_size

print random_search( number_of_iterations, search_space )

