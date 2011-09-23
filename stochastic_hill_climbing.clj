; Random mutation hill climb
(def random-bit #(if (>= (rand) 0.5) 0 1))

(defn random-vector [n]
  (vec (take n (repeatedly random-bit))))

(defn onemax [c] (reduce + c))

(defn random-neighbor [v]
  (let [pos (rand-int (count v))
	i (if (= (v pos) 1) 0 1)]
    (assoc v pos i)))

(defn search [iterations, bits]
  (let [ rand-bit-string (random-vector bits)
	candidate {:vector rand-bit-string
		   :cost (onemax rand-bit-string)}
	]
    (loop [i iterations b bits c candidate]
      (let [neighbor-string (random-neighbor (:vector c))
	    neighbor {:vector neighbor-string
		      :cost (onemax neighbor-string)}]
	
	(if (or (zero? i) (= (:cost c) bits) ) {:itr i :soln c}
	    (if (>= (:cost neighbor) (:cost c))
	      (recur (dec i) b neighbor)
	      (recur (dec i) b c)))))))

(println (search 1000 64))
    
