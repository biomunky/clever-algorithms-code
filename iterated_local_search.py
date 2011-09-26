# Iterated Local Search
# Applied to the Berlin52 Traveling salesman problem.
# The optimal solutions is 7542 units

from __future__ import division
from math import sqrt
from random import shuffle, randint

def euclidean( c1, c2 ):
    return sqrt(sum([(x[0]-x[1])**2 for x in zip(c1,c2)]))

def cost( permutation, cities ):
    distance = 0
    for idx, c1 in enumerate(permutation):
        c2 = permutation[0] if idx == len(permutation)-1 else permutation[idx+1]
        distance += euclidean( cities[c1], cities[c2] )
    return distance

def random_permutation( cities ):
    perm = range(len(cities))
    shuffle(perm)
    return perm
    
def stochastic_two_opt( permutation ):
    perm = permutation[:]
    c1, c2 = randint(0,len(perm)), randint(0,len(perm))
    exclude = [c1]
    exclude.append( len(perm)-1 if c1==0 else c1-1 )
    exclude.append( 0 if c2==len(perm)-1 else c1+1 )
    while c2 in exclude:
        c2 = randint(0, len(perm))
    c1, c2 = [c2, c1] if c2 < c1 else [c1, c2]
    c1c2_rev = perm[c1:c2]
    c1c2_rev.reverse()
    perm[c1:c2] = c1c2_rev
    perm.reverse()
    return perm

def local_search( best, cities, max_no_improv ):
    count = 0
    while count >= max_no_improv:
        candidate = { 'vector':stochastic_two_opt(best['vector']) }
        candidate['cost'] = cost( candidate['vector'], cities )
        if candidate['cost'] < best['cost']:
            count = 0
            best = candidate
        else:
            count+=1
    return best

def double_bridge_move(perm):
    pos1 = 1 + randint(0,len(perm)/4)
    pos2 = pos1 + 1 + randint(0,len(perm)/4)
    pos3 = pos2 + 1 + randint(0,len(perm)/4)
    p1 = perm[0:pos1] + perm[pos3:]
    p2 = perm[pos2:pos3] + perm[pos1:pos2]
    return p1 + p2


def perturbation( cities, best ):
	candidate = {'vector': double_bridge_move( best['vector'])}
	candidate.setdefault( 'cost', cost(candidate['vector'], cities))
	return candidate
	
def search( cities, max_iterations, max_no_improv):
	best = {'vector': random_permutation( cities )}
	best.setdefault('cost', cost(best['vector'], cities))
	best = local_search(best,cities, max_no_improv)
	for itr in range(0, max_iterations):
            candidate = perturbation( cities, best )
            candidate = local_search(candidate, cities, max_no_improv)
            if candidate['cost'] < best['cost']:
                best = candidate
	return best


berlin52 = [[565,575],[25,185],[345,750],[945,685],[845,655],
	[880,660],[25,230],[525,1000],[580,1175],[650,1130],[1605,620],
	[1220,580],[1465,200],[1530,5],[845,680],[725,370],[145,665],
	[415,635],[510,875],[560,365],[300,465],[520,585],[480,415],
	[835,625],[975,580],[1215,245],[1320,315],[1250,400],[660,180],
	[410,250],[420,555],[575,665],[1150,1160],[700,580],[685,595],
	[685,610],[770,610],[795,645],[720,635],[760,650],[475,960],
	[95,260],[875,920],[700,500],[555,815],[830,485],[1170,65],
	[830,610],[605,625],[595,360],[1340,725],[1740,245]]

max_iter = 100
max_no_improv = 50
best = search(berlin52, max_iter, max_no_improv)
print best['cost']
