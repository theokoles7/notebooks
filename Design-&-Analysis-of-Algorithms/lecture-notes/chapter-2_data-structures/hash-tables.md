# Hash Tables

* ## Universal Hashing

	* For the hash function of $h_{ab}(k) = ((a * k + b) % p) % m$, where *p* is a large prime number, with $p > m$, $a \in \{1, 2, ..., p - 1\}$ and $b \in \{0, 1, 2, p-1\}$, the collection of such hash functions is universal.
	* In this case, m can be any number and does not have to be a prime. For example, for p = 17 and m = 8, we have h_34(15) = (((3 * 15 + 4) % 17) % 8) = 7. 
    
* ## Open Addressing

	* Elements store inside the table
	* Calculating probe squence of given key, instead of using pointers: $<h(k, 0), h(k, 1), h(k, 2), ..., h(k, m-1)>$
	* If probe sequence is a permutation of $<0, 1, 2, ..., m - 1>$, every table entry is a candidate location for the element.
	* The probe sequence is fixed for a given key.
	* Key has to be stored in the table entry.

* ## Uniform Hashing Analysis on Open Addressing

	* Key probe sequance equal likely in one of *m!* permutations of $<0, 1, 2, ..., m - 1>$
	* Probe sequences defined for open addressing
		* ***Linear Probing***: $m$ different sequences
			* Dictated by $h(k, i) = (h'(k) + i)~\%~m$
			* Subject to primary clustering
            
		* ***Quadratic Probing***: $m$ different sequences
			* Dictated by $h(k, i) = (h'(k) + c_1i + c_2i^2)~\%~m$
			* Subject to secondary clustering, where both keys follow the *same* probe sequence

		* ***Double Hashing***: $m^2$ different sequences
			* Dictated by $h(k, i) = (h_1(k) + i \times h_2(k))~\%~m$
			* Many good dchoices:
				* $h_2(k)$ relatively prime to $m$
				* $m$ itself is prime
				* $m$ a power of 2 and $h_2(k)$ is always an odd number
				* $m$ is prime and $m'$ slightly less than $m$ (e.g., $m - 1$ or $m - 2$), with $h_1(k) = k~\%~m$ and $h_2(k) = 1 + (k~\%~m')$

* ## Open-Address Hashing Analysis

    **NOTE**: *Load factor* is he number of elements in a hash table divided by the number of slots

    * ***Theorem 1***:

        For an open-address hash table with load factor $\alpha = n/m < 1$, the expected number of probes in unsuccessful search under uniform hashing is at most $1/(1 - \alpha)$

        **NOTE**: *Unsuccessful search* ends at finding an empty entry

        + If $\alpha$ is a constant, an unsuccessful search runs in *O(1)* time
        + Inserting an element into an open-address hash table with load factor $\alpha$ takes at most $1/(1 - \alpha)$ probes on an average under uniform hashing, because it has $(1 - \alpha)$ for 1 probe, plus prob $\alpha\times(1 - \alpha)$ to take 2 probes, plus prob $\alpha^2 \times (1 - \alpha)$ to take 3 probes, etc., yielding $1 + \alpha + \alpha^2 + \alpha^3 + ... = 1/(1 - \alpha)$.

    * ***Theorem 2***:

        For an open-address hash table with load factor $\alpha < 1$, the expected number of probes in a successful search under uniform hashing is at most $\frac{1}{\alpha} \times ln\frac{1}{1 - \alpha}$

        + Successful search for a key equals the sequence of inserting the key
        + $2^{nd}$ key insertion takes $\le 1 / (1 - (1 / m))$ probes, on an average, when $\alpha$ is $1 / m$
        + $3^{rd}$ key takes $\le 1 / (1 - (2 / m))$ probes on an average, when $\alpha$ is $2 / m$
        + ...and so on.