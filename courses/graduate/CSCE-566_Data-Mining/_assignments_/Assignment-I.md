# <p style="text-align:center; font-family: Times New Roman">CSCE 566 - 001 - Assignment I</p>
<p style="text-align:center;">Gabriel C. Trahan - C00058009</p>

## Task 1: 

**Consider the following six transactions:**

| | | | | | | |
|-|-|-|-|-|-|-|
| $T_1$ | Pringles  | Oreo      | Coke              | Ham               |       |       |
| $T_2$ | Ruffles   | Pringles  | Ham               | Boneless Chicken  | Pepsi |       |
| $T_3$ | Ruffles   | Lays      | Ham               | Boneless Chicken  | Pepsi | Coke  |
| $T_4$ | Lays      | Bacon     | Boneless Chicken  |                   |       |       |
| $T_5$ | Ruffles   | Ham       | Bacon             | Whole Chicken     | Pepsi |       |
| $T_6$ | Ruffles   | Oreo      | Pepsi             | Boneless Chicken  |       |       |

### Questions:
1. Define what a frequent itemset is and explain the significance of the minimum support threshold in identifying frequent itemset.
2. Without detailed calculations, based on the transactional dataset provided, discuss which itemset you expect to be frequent if the minimum support threshold is set to 50%, and explain why.

## Task 2: 

**Given the frequent itemsets $\{Tea, Sugar\}$, $\{Tea, Lemon\}$, and $\{Sugar, Honey\}$ with a minimum support of 50%, generate all possible association rules.**

### Questions:
1. Calculate the confidence for each rule if the following support counts are given:
    * Support($\{Tea, Sugar\}$) = 50%
    * Support($\{Tea, Lemon\}$) = 50%
    * Support($\{Sugar, Honey\}$) = 50%
    * Support($\{Tea\}$) = 70%
    * Support($\{Sugar\}$) = 65%
    * Support($\{Lemon\}$) = 60%
    * Support($\{Honey\}$) = 60%
2. Identify the rules that have a confidence level of at least 60%.

## Task 3:

**Consider the following scnearios:**

* S1: An online bookstore analyzing the co-purchase patterns of books.
* S2: A grocery store analyzing the purchase patterns of perishable goods.
* S3: A streaming service analyzing the co-watching patterns of movies.

### Questions:

1. For each scenario, provide an example of an association rule that might be discovered through data analysis. Use the following hypothetical support and confidence values to calculate the lift:
    * **Scenario 1 (Online Bookstore)**: 
        * Support for $\{Fantasy, Science Fiction\}$ = 0.05
        * Support for $\{Science Fiction\}$ = 0.20
        * Confidence = 0.25
    * **Scenario 2 (Grocery Store)**:
        * Support for $\{Apples, Cinnamon\}$ = 0.10
        * Support for $\{Cinnamon\}$ = 0.15
        * Confidence = 0.67
    * **Scenario 3 (Streaming Service)**:
        * Support for $\{Horror, Thriller\}$ = 0.08
        * Support for $\{Thriller\}$ = 0.30
        * Confidence = 0.27
    
    Calculate the lift for each rule and discuss the results, specifically:
    * For the bookstore, what does the lift suggest about the relationship between Fantasy and Science Fiction books?
    * For the grocery store, how does the lift value inform you about the association between Apples and Cinnamon, particularly in the context of seasonal shopping?
    * For the streaming service, what insights can you draw from the lift value about the co-watching behavior of users?

2. Dive deeper into how the interpretation of lift might differ across these contexts:
    * What does a high lift value suggest for the online bookstore compared to the grocery store? How might customer intent differ when buying books versus groceries?
    * In the case of the streaming service, how could lift reveal insights about viewer behavior, such as binge-wtching habits or preferences for certain content pairings? Discuss how the continuous and often impulsive nature of streaming might influence lift interpretation.

## Task 4:

**You are tasked with critically analyzing the Apriori algorithm, focusing on its conceptual foundations, efficiency, and potential limitations in frequent itemset mining:**

### Dataset:

| | | | | |
|-|-|-|-|-|
| $T_1$ | Laptop    | Mouse         | USB Drive     |           |
| $T_2$ | Laptop    | Headphones    | USB Drive     |           |
| $T_3$ | Mouse     | Headphones    | USB Drive     |           |
| $T_4$ | Laptop    | USB Drive     |               |           |
| $T_5$ | Laptop    | Mouse         | Headphones    | USB Drive |

### Questions:

1. Apply the Apriori algorithm to the given dataset with a minimum support threshold of 60%. Detail each step including the generation of candidate itemsets, pruning decisions, and the final frequent itemsets.

2. Discuss the theoretical implications of this principle for reducing the computational complexity in large datasets. What assumptions does te Apriori algorithm make about the dataset?

3. As you proceed, critically evaluate each step: How does the algorithm leverage the Apriori principle to optimize the process? What potential inefficiences or challenges might arise at each stage?