import random

def objective_function( vector ):
    return sum([x ** 2.0 for x in vector])

def rand_in_bounds( mn, mx ):
    return mn + ((mx - mn) * random.random() )

def random_vector( minmax ):
    return [rand_in_bounds(vec[0], vec[1]) for i, vec in enumerate(minmax)]

def take_step( minmax, current, step_size ):
    position = [0] * len(current)
    for i, val in enumerate( position ):
        mn = max(minmax[i][0], current[i]-step_size)
        mx = min(minmax[i][1], current[i]+step_size)
        position[i] = rand_in_bounds(mn, mx)
    return position

def large_step_size( itr, step_size, s_factor, l_factor, iter_mult):
    if itr > 0 and itr % iter_mult == 0:
        return step_size * l_factor
    else:
        return step_size * s_factor

def take_steps( bounds, current, step_size, big_stepsize):
    step, big_step     = {}, {}
    step['vector']     = take_step( bounds, current['vector'], step_size )    
    step['cost']       = objective_function( step['vector'])
    big_step['vector'] = take_step( bounds, current['vector'], big_stepsize)
    big_step['cost']   = objective_function( big_step['vector'] )
    return step, big_step

def search( max_iter, bounds, init_factor, s_factor, l_factor, iter_mult, max_no_impr):
    step_size = (bounds[0][1] - bounds[0][0]) * init_factor
    current, count = {}, 0
    current['vector'] = random_vector( bounds )
    current['cost']   = objective_function( current['vector'] )
    for itr in range( max_iter ):
        big_stepsize = large_step_size( itr, step_size, s_factor, l_factor, iter_mult)
        step,big_step = take_steps( bounds, current, step_size, big_stepsize)
        if step['cost'] <= current['cost'] or big_step['cost'] <= current['cost']:
            if big_step['cost'] <= step['cost']:
                step_size, current = big_stepsize, big_step
            else:
                current = step
            count = 0
        else:
            count = count + 1
            if count >= max_no_impr:
                count, step_size = 0, (step_size/s_factor)
    return current
                                                       

problem_size = 2
bounds       = [[-5, 5]] * problem_size
max_iter     = 1000
init_factor  = 0.05
s_factor     = 1.5
l_factor     = 3.0
iter_mult    = 10.0
max_no_impr  = 30.0
best         = search(max_iter, bounds, init_factor, s_factor, l_factor, iter_mult, max_no_impr)

print "Best cost=%f " % (best['cost']), best['vector']

