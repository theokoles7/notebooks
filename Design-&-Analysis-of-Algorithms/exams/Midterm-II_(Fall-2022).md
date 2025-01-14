# CSCE 500 - Midterm Exam II (Fall 2022)
[< Back](../toc.md)

1. **For a given Balanced (B)-tree of height $h$ and minmum node degree of $t\le2$, what is the maximum number of keys held in such a tree?**

    $$
    n \le (2t-1) \Sigma_{i = 0}^h (2t)^i            \\
    n \le (2t-1) \cdot \frac{(2t)^h - 1}{2t - 1}    \\
    n \le (2t)^h - 1
    $$

---
 
2. **Given the Red-Black (RB) -tree below...**

    <img src="../images/CSCE500-MidtermII-Fall2022-2.png">

    ...show the resulting tree in sequence after:

    * **A. Inserting 5**

        <img src="../images/CSCE500-MidtermII-Fall2022-2a.png">

    * **B. Deleting 2**

        <img src="../images/CSCE500-MidtermII-Fall2022-2b.png">

    * **C. Deleting 8**

        <img src="../images/CSCE500-MidtermII-Fall2022-2c.png">

---

3. **Given the initial B-Tree with a minimum node degree of $t=3$...**

    <img src="../images/CSCE500-MidtermII-Fall2022-3.png">

    ...show the results of:

    * **A. Deleting $T$**

        <img src="../images/CSCE500-MidtermII-Fall2022-3a.png">

    * **B. Deleting $C$**

        <img src="../images/CSCE500-MidtermII-Fall2022-3b.png">

    * **C. Inserting $J_2$ | $J \lt J_2 \lt K$**

        <img src="../images/CSCE500-MidtermII-Fall2022-3c.png">

    * **D. Deleting $Y$**

        <img src="../images/CSCE500-MidtermII-Fall2022-3d.png">

---

 4. **Procedure `EXTENDED-BOTTOM-UP-CUT-ROD(P, N)` below exhibits low time complexity by utilizing two auziliary arrays, $r[0 \dots n]$ and $s[0 \dots n]$ to keep solutions for sub-problems obtained thus far, following the bottom-up approach.**

    ```
    Extended-Bottom-Up-Cut-Rod(p, n)
        let r[0...n] and s[0...n] be new arrays
        r[0] = 0
        for j = 1 to n
            q = -infinity
            for i = 1 to j
                if q < p[i] + r[j - i]
                    q = p[i] + r[j - i]
                    __________________
            r[j] = q
        return r and s
    ```

    * **A. Fill in the missing statement.**

        `s[j] = i` (Record the optimal cut-length found thus far)

    * **B. Give its time complexity.**

        $\Theta(n^2)$

    * **C. If `Extended-Bottom-Up-Cut-Rod(p, 8)` returns...**
    
        | $i$       | 0 | 1 | 2 | 3 | 4     | 5     | 6     | 7     | 8     |
        |:---------:|---|---|---|---|-------|-------|-------|-------|-------|
        | $r[i]$    | 0 | 1 | 5 | 8 | 10    | 13    | 17    | 18    | 22    |
        | $s[i]$    | 0 | 1 | 2 | 3 | 2     | 2     | 6     | 1     | 2     |

        **...show your resulting cut of the rod with 8 units in length for the maximum revenue.**

        <img src="../images/CSCE500-MidtermII-Fall2022-4c.png">

---

5. **Given a set of 4 keys, with the following probabilities, determine the cost and the structure of an optimal binary search tree (OBST), following the tabular, bottom-up method realized in the procedure `OPTIMAL-BST` below to construct and fill $e[1 \dots 5, 0 \dots 4]$, $w[1 \dots 5, 0 \dots 4]$, and $root[1 \dots 4, 1 \dots 4]$...**

    | $i$   | 0     | 1     | 2     | 3     | 4     |
    |:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
    | $p_i$ |       | 0.12  | 0.08  | 0.15  | 0.18  |
    | $q_i$ | 0.08  | 0.06  | 0.09  | 0.10  | 0.14  |

    ```
    OPTIMAL-BST(p, q, n)
        let e[1:n + 1, 0:n], w[1:n + 1, 0:n], and root[1:n, 1:n] be new tables
        for i = 1 to n + 1
            e[i, i - 1] = q_{i - 1}
            w[i, i - 1] = q_{i - 1}
        for l = 1 to n
            for i = 1 to n - l + 1
                j = i + l - 1
                e[i, j] = infinity
                w[i, j] = w[i, j - 1] + p_j + q_j
                for r = i to j
                    t = ___________________________________ (a)
                    if t < e[i, j]
                        e[i, j] = t
                        ________________ (b)
        return e and root
    ```

    * A. **Fill in the missing 2 statements of the procedure.**

        * a: `e[i, r - 1] + e[r + 1, j] + w[i, j]`
        * b: `root[i, j] = r`

    * **B. Construct and fill the three tables and show the OBST obtained.**