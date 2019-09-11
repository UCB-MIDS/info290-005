---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.3
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Some Probability Practice 



```python
import numpy as np
from scipy import special
```

# Problem 1 

Suppose you roll a die rolled repeatedly. Remember that in this class, dice are assumed fair unless the description says otherwise.

For $k = 1, 2, 3, \ldots, 6 $ let $D_k$ be the event that the first $k$ rolls all show different faces. 

## (a)  

For $k = 1, 2, 3, \ldots, 6 $ let $D_k$ be the event that the first $k$ rolls all show different faces. Note that $P(D_1) = 0$ because you can't have different faces with just one roll.

Without doing any calculations, draw a Venn diagram that shows the events $D_4$ and $D_5$. Make it clear which is which, and justify your answer. Then enter one of the symbols $\le$, $=$, and $\ge$ in the blank below.

$P(D_5) ~ \underline{~~~~~~~~~~} P(D_4)$

## (b) 

For $k = 2, 3, \ldots, 7$ let $F_k$ be the event that the $k$th roll is the first time you see a face that has already appeared. Write the event $F_k$ in terms of the events $D_1, D_2, \ldots, D_6$.

## (c) 

In the Venn diagram that you drew in Part **a**, there's a region that corresponds to one of the events $F_i$ for some $i$.  Say which $i$ it is, and shade that event $F_i$ in your diagram. There's no need to draw a new diagram. Just shade the appropriate region in the diagram you already drew.

## (d) 

Thus far, you haven't used any fractions – just logic. Now for some calculation. In the code cell below, define a function `prob_d` that takes $k$ as its argument and returns $P(D_k)$.

```python
def prob_d(k): 
    '''
    Define the docstring to tell me what you're doing.
    '''
    rolls = np.arange(k)
    
    return(something) 
```

Does this function produce what you anticipated it would produce from your Venn diagram for $P(D_4)$ and $P(D_5)$? 


# 2. Heads in Coin Tossing
 > This is one of the fundamental models of probability theory. Note that unless otherwise specified, coins in this course are assumed to be fair.

Suppose you toss a coin $n$ times and note down the sequence of heads (H) and tails (T). 

Fix an integer $k$ such that $0 \le k \le n$.

## (a) 

In total, how many possible sequences are there? How many sequences have $k$ heads? 

## (b) 

What is the chance that you get $k$ heads in your $n$ tosses? Why?

## (c)  

Does your answer in **b** make sense in the cases $k=0$ and $k=n$? Explain.

## (d) 

Use the `scipy` is a library for scientific computing. In particular, the `special` module of `SciPy` computes combinatorial terms and has been imported in this notebook. 

To calculate $\binom{n}{k}$, use `special.comb(n, k)`.

```python

```

Define a function `chance_of_heads` that takes `n` and `k` as its arguments and returns the chance of `k` heads in `n` tosses of a fair coin. Do not use any built-in `SciPy` probability functions; just use your answer to **b**.

We have started the code for you. Try to ignore the fact that we have converted the integer `n` to a `float`. It won't affect `special.comb` and it will help ensure that the calculation is accurate when `n` and `k` are large.

```python
def chance_of_heads(n, k):
    '''
    Returns the chance of k heads in n tosses of a fair coin
    '''
    n = float(n)
    return ...
```

To check whether your function is working correctly, list all possible outcomes of two tosses of a coin and hence calculate P(0 heads), P(1 head), and P(2 heads).

```python
chance_of_heads(2, 0)
chance_of_heads(2, 1)
chance_of_heads(2, 2)
```
