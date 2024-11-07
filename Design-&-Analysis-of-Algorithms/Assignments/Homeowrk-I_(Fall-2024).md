# <p style="text-align:center; font-family: Times New Roman">CSCE 500 - 001 - Assignment I</p>
<p style="text-align:center;">Gabriel C. Trahan - C00058009</p>

---

**NOTE**: Questions 1 - 9 are sourced from textbook: _Introduction to Algorithms_ $4^{th}$ _ed_

1. _4.4-1.d (page 101)_

    For each of the following recurrences sketch its recursion tree, and guess a good asymptotic upper bound on its solution. Then, use the substitution method to verify your answer.

    d. $T(n) = 3T(n-1) + 1$

    **NOTE**: This is a _linear_ recurrence relation.

    ![image center](./images/4.4-1.d_sketch.svg)

    Assume that $T(1)=\Theta(1)$.
    The height of the recursion tree is $n$.
    At depth $i$, for $i=0, 1, \dots, n-1$, there are $3^i$ nodes incurring a unit cost each, so the total cost of all nodes at depth $i$ is $3^i$.
    The bottom level, at depth $n$, contains $3^n$ leaves, so the total leaf cost is $\Theta(3^n)$.
    Thus, we get
    $$
        T(n) = \sum_{i=0}^{n-1}3^i+\Theta(3^n) \\
        = \frac{3^n-1}{3-1}+\Theta(3^n) \\
        < 2\cdot3^n+\Theta(3^n) \\
        = O(3^n).
    $$

    To prove this bound we adopt the inductive hypothesis that $T(n)\le c3^n-d$ for all $n\ge n_0$, where $c$, $n_0>0$ and $d\ge0$ are constants, and assume that the inductive hypothesis holds for all numbers at least as big as $n_0$ and less than $n$.
    When $n\ge n_0+1$ it holds that $T(n-1)\le c3^{n-1}-d$, so
    $$
        T(n) \le 3(c3^{n-1}-d)+1 \\
        = c3^n-3d+1 \\
        = c3^n-d+(1-2d) \\
        \le c3^n-d
    $$

    If we now let $n_0=1$, we can choose $c=(T(1)+d)/3$ to satisfy $T(1)\le c\cdot3^1-d$, establishing the bound for the base case.

    We've shown that $T(n)\le c3^n-d\le c3^n$ for all $n\ge1$, which implies that the solution to the recurrence is $T(n)=O(3^n)$.

2. _4.5-1.c (page 106)_

    Use the master method to give tigh asymptotic bounds for the following recurrences:

    c. $T(n) = 2T(n / 4) + \sqrt{n}\log^2n$

    Here, $a = 2$ and $b = 4$.

    From $n^{\log_4{2}} = O(n^{1/2})$, we have $f(n) = \sqrt{n}~lg^2n = \Omega(n^{\log_4{2}} + \epsilon)$ to get $T(n) = \Theta(\sqrt{n}~log^2n)$.

    This relation applies to case 3 of master method theorem 1, as $f(n)$ is polynomially larger than $n^{log_b{a}}$.

3. _4.1.c (page 119)_

    Give asymptotically tight upper and lower bounds for $T(n)$ in each of the following algorithmic recurrences. Justify your answers.

    c. $T(n) = 16T(n/4) + n^2$

    Here, $a = 16$ and $b = 4$.

    From $n^{log_{4}{16}} = O(n^{2})$, we have $f(n) = n^2 = n^{log_{b}{a}}$

4. _4-1.f (page 119)_

    f. $T(n) = 7T(n/2) + n^2\log~n$

5. _4-3.f (page 121)_

    Solve the following recurrences by changing variables:

    f. $T(n) = 3T(\sqrt[3]{n}) + \Theta(n)$

6. _4-4.f (page 121)_

    Give asymptotically tight upper and lower bounds for $T(n)$ in each of the following recurrences. Justify your answers.

    f. $T(n) = T(n/2) + T(n/4) + T(n/8) + n$

7. _12.2-2 (page 320)_

    Write recursive versions of _Tree Minimum_ and _Tree Maximum_.

8. _12.2-3 (page 320)_

    Write the _Tree Predecessor_ procedure.

9. What is the resulting RedBlake (RB) tree after adding a new node with $key = 36$, to _Figure 13.1.c (page 333)_?

10. Consider cuckoo hasing with multiple table components, $T_1$ and $T_2$.

    a. When there are two table components, $T_1$ and $T_2$, what is the simplest method (with lowest overhead) to deal with _failure insertion_ under such cuckoo hashing? What is (or are) the consequence (or consequences) of such a failure resolution method?

    b. What are the advantage(s) and disadvantage(s) for cuckoo hashing to have _three_ table components?