# CSCE 500 - Midterm Exam I (Fall 2024)
[< Back](../toc.md)

1. **Solve the recurrence relations:**

    * **A. $T_1(n) = 3 \cdot T_1(n^{\frac{1}{2}}) + \lg(n)$**

        $$
        Let~m = \lg(n), n = 2^m                                     \\
        T_1(2^m) = 3 \cdot T_1(2^{\frac{m}{2}}) + m                 \\
        Let~T_1(2^m) = S(m)                                         \\
        Therefore:                                                  \\
        S(m) = 3 \cdot S(\frac{m}{2}) + m                           \\
        m^{\lg_2(3)}~vs.~m', is~polynomially~larger                 \\
        Apply~case~1~of~Master~Method:                              \\
        S(m) = \Theta(m^{\lg_2(3)}) = \Theta((\lg n)^{\lg_2(3)})    \\
        T(2^m) = T(n) = \Theta((\lg n)^{\lg_2(3)})
        $$

    * **B. $T_2(n) = T_2(\frac{n}{3}) + T_2(\frac{2n}{3}) + n \cdot \lg(n)$**

---

2. **Is $n^3$ asymptotically-tight bound of**

    * **A. $(n^{2.99}) \cdot (\lg n)$**
    * **B. $\frac{n^3}{\lg \cdot \lg n}$**

---

3. **The utilization efficiency of a hash table depends heavily on its hashing function(s) employed. Describe with a diagram to illustrate how a multiplication method of hashing functions works on a machine with a word size of $w$ bits for a hash table with $2^p$ entries | $p \lt w$.**

---

4. **For an open-address hash table with load factor $\alpha = \frac{n}{m} \lt 1$, prove that:**

    * **A. The expected number of probes in an unsuccessful search under uniform hashing is at most $\frac{1}{1 - \alpha}$.**
    * **B. The expected number of probes in a successful probe under uniform hashing is at most $(\frac{1}{\alpha}) \cdot \lg(1 - \alpha)^{-1}$. (Proof sketch suffices by explaining the probe count needed to locate existing keys)**

---

5. **A binary search tree ($T$) is to be maintained following the in-order tree traversal order. Consider a sequence of arrival keys, {32, 27, 42, 14, 23, 33, 25, 34, 37, 28, 39}, to $T$ which is initially empty.**

    * **A. Show the resulting $T$ after inserting all arrival keys.**

        <img src="../images/CSCE500-MidtermI-Fall2024-5a.png">

    * **B. Show the resulting $T$ after its root node is deleted.**

        <img src="../images/CSCE500-MidtermI-Fall2024-5b.png">
    
    * **C. Show the resulting $T$ after deleting 27.**

        <img src="../images/CSCE500-MidtermI-Fall2024-5c.png">

---

6. **Show that a Red-Black (RB)-tree with $n$ internal nodes has the height of $h \le 2 \cdot \lg(n + 1)$.**

---

7. **For the RB-tree below...**

    <img src="../images/CSCE500-MidtermI-Fall2024-7.png">

    **...show the resulting tree in sequence after:**

    * **A. Inserting 4**

        <img src="../images/CSCE500-MidtermI-Fall2024-7a.png">

    * **B. Inserting 17**

        <img src="../images/CSCE500-MidtermI-Fall2024-7b.png">