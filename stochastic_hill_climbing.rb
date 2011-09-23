# Random mutation hill climb
# Create a random binary string
# Seems similar to the code in the selfish gene
# Read it ages ago
# Outcome: string where all bits == 1

def onemax(vector)
  return vector.inject(0.0){ |sum,v| sum + ((v=="1") ? 1 : 0)}
end

def random_bitstring( num_bits )
  return Array.new( num_bits ) { |i| (rand<0.5) ? "1" : "0"}
end

def random_neighbour( bitstring )
  mutant = Array.new(bitstring)
  pos = rand(bitstring.size)
  mutant[pos] = (mutant[pos]=='1') ? '0' : '1'
  return mutant
end

def search( max_iterations, num_bits )
  candidate = {}
  candidate[:vector] = random_bitstring( num_bits )
  candidate[:cost]   = onemax( candidate[:vector] )
  max_iterations.times do |iter|
    neighbor = {}
    neighbor[:vector] = random_neighbour( candidate[:vector] )
    neighbor[:cost]   = onemax( neighbor[:vector] )
    candidate = neighbor if neighbor[:cost] >= candidate[:cost]
    puts "> iteration #{(iter+1)}, best=#{candidate[:cost]}"
    break if candidate[:cost] == num_bits
  end
  return candidate
end

num_bits = 64
max_iterations = 1000
best = search( max_iterations, num_bits )
puts "Done. Best Soln: c=#{best[:cost]}, v=#{best[:vector].join}"

