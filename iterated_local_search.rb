def euc_2d( c1, c2)
  Math.sqrt( (c1[0] - c2[0])**2 + (c1[1] - c2[0])**2)
end

def cost( permutation, cities )
  distance = 0
  permutation.each_with_index do | c1, i |
    c2 = (i == permutation.size-1) ? permutation[0] : permutation[i+1]
    distance += euc_2d(cities[c1], cities[c2])
  end
  return distance
end

def random_permutation( cities )
  perm = Array.new( cities.size ){ |i| i }
  perm.each_index do |i|
    r = rand( perm.size-i ) + i
    perm[r], perm[i] = perm[i], perm[r]
  end
  return perm
end

def stochastic_two_opt( permutation )
  perm = Array.new( permutation )
  c1, c2 = rand(perm.size), rand(perm.size)
  exclude = [c1]
  exclude << ( (c1 == 0) ? perm.size-1 : c1-1)
  exclude << ( (c1==perm.size-1) ? 0 : c1 + 1)
  c2 = rand(perm.size) while exclude.include?(c2)
  c1, c2 = c2, c1 if c2 < c1
  perm[c1...c2] = perm[c1...c2].reverse
  return perm
end

def local_search( best, cities, max_no_improv)
  count = 0
  begin
    c = {:vector => stochastic_two_opt(best[:vector])}
    c[:cost] = cost(c[:vector], cities)
    count = (c[:cost] < best[:cost]) ? 0 : count + 1
    best = c if c[:cost] < best[:cost]
  end until count >= max_no_improv
  return best
end

def double_bridge_move(perm)
  pos1 = 1 + rand(perm.size / 4)
  pos2 = pos1 + rand(perm.size / 4 )
  pos3 = pos2 + rand(perm.size / 4 )
  p1 = perm[0...pos1] + perm[pos3..perm.size]
  p2 = perm[pos2...pos3] + perm[pos1...pos2]
  return p1 + p2
end

def perturbation( cities, best)
  c = {:vector => double_bridge_move(best[:vector])}
  c[:cost]   = cost( c[:vector], cities)
  return c
end

def search( cities, max_iterations, max_no_improv)
  best = {}
  best[:vector] = random_permutation(cities)
  best[:cost]   =  cost( best[:vector], cities )
  best = local_search( best, cities, max_no_improv)
  max_iterations.times do |iter|
    c = perturbation( cities, best)
    c = local_search( c, cities, max_no_improv)
    best = c if c[:cost] < best[:cost]
  end
  return best
end


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
print best[:cost],"\n"








