# CSCE 500 - Midterm I (Fall 2022)
[< Back](../toc.md)

1. **A problem with size $n$ follows a typical divide-and-conquer approach to have its time complexity of $T(n) = T(\frac{n}{4}) + T(\frac{n}{4}) + T(\frac{n}{2}) + c \cdot n$. Solve $T(n)$.**

---

2. **Solve $T_1(n) = 2 \cdot T_1(n^{\frac{1}{2}}) + \lg(n)$.**

---

3. **Is $n^3$ asymptotically-tight bound of:**

    * **A. $(n^{2.9999}) \cdot (\lg n)$**
    * **B. $\frac{n^{3.001}}{\lg n}$**

---

4. **The utilization efficiency of a hash table depends heavily on its hashing function(s) emplyed. Describe with a diagram to illustrate how a multiplication method of hashing function works on a machine with a word size of $w$ bits for a hash table with $w^p$ entries | $p \lt w$.**

---

5. **For an open-address hash table with a load factor of $\alpha = \frac{n}{m} \lt 1$, prove that...**

    * **A. The expected number of probes for a successful probe under uniform hashing is at most $\frac{1}{1 - \alpha}$.**
    * **B. The expected number of probes for a successful probe under uniform hashing is at most $(\frac{1}{\alpha}) \cdot \ln(1 - \alpha)^-1$.**

---

6. **Cuckoo hashing:**

    * **A. Briefly explain how Cuckoo hashing works under two hash functions of $h_1$ and $h_2$.**
    * **B. State the situation when a new key cannot be inserted in a Cuckoo hashing table successfully, provide two possible solutions for key insertion failures, and contrast them in terms of advantages/disadvantages.**

---

7. **A Binary search tree $T$ is to be maintained following the in-order tree traversal order. Consider a sequence of arrival keys, {25, 23, 14, 7, 9, 21, 31, 34, 18, 24}, to $T$ which has just the root node with its key = 20 initially.**

    * **A. Show the resulting $T$ after inserting all arrival keys.**
    * **B. Show the resulting $T$ after its root node is then deleted.**
    * **C. Complete the schematic diagram of deleting Node $z$ in the figure below and also fill in the three missing statements in the deletion pseudo code.**

    ```
    TREE-DELETE(T, z)
        if z.left == NIL
            TRANSPLANT(T, z, z.right)
        elseif z.right == NIL
            TRANSPLANT(T, z, z.left)
        else
            y = TREE-MINIMUM(z.right)
            if y.p != z
                ____________
                ____________
                ____________
                
            TRANSPLANT(T, z, y)
            y.left = z.left
            y.left.p = y
    ```

    <img src="../images/CSCE500-MidtermI-Fall2022-7c.png">