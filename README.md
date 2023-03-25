# 30 useful functions in [Python](https://www.python.org/ "Python")

- **Ascending OR Descending**
- **Riffle**
- **Only odd digits**
- **Three summers ago**
- **Count all sums and products**
- ** Group equal consecutive elements into sublists**
- **Try a spatula**
- **First missing positive integer**
- **Check your permutation**
- **Tribonacci**
- **Keep doubling**
- **Remove item after its k:th occurrence**
- **And sometimes why**
- **Sort array by element frequency**
- **What do you hear, what do you say?**
- **Giving back change**
- **Sort integers by their digit counts**
- **Scrabble value of a word**
- **Create zigzag array**
- **All cyclic shifts**
- **Postfix interpreter**
- **Count consecutive summers**
- **Running median of three**
- **Reverse every ascending sublist**
- **Longest palindrome substring**
- **Iterated removal of consecutive pairs**
- **Brangelina**
- **Collapse positive integer intervals**
- **Fulcrum**
- **Expand positive integer intervals**

------------
### Riffle-function-in-python
Given a list of items that is guaranteed to contain an even number of elements (note that the integer zero is an even number), create and return a list produced by performing a perfect riffle to the items by interleaving the items of the two halves of the list in an alternating fashion. When performing a perfect riffle, also known as the Faro shuffle, the list of items is split in two equal sized halves, either conceptually or in actuality. The first two elements of the result are then the first elements of those halves. The next two elements of the result are the second elements of those halves, followed by the third elements of those halves, and so on up to the last elements of those halves. The parameter out determines whether this function performs an out shuffle or an in shuffle, that is, from which half of the list the alternating card is taken first.

------------

# Tribonacci-with-python
The famous and important Fibonacci series is deϐined to start with values (1, 1) and from there, each element in the sequence equals the sum of the previous two elements. However, a cute variation aptly called the Tribonacci series works otherwise the same way, but starts with a triple of values (1, 1, 1) and from there, each element equals the sum of the previous three elementsThe famous and important Fibonacci series is deϐined to start with values (1, 1) and from there, each element in the sequence equals the sum of the previous two elements. 
However, a cute variation aptly called the Tribonacci series works otherwise the same way, but starts with a triple of values (1, 1, 1) and from there, each element equals the sum of the previous three elements.
Tribonacci numbers grow quite a bit faster than Fibonacci numbers, the ϐirst twenty being 1, 1, 1, 3,5, 9, 17, 31, 57, 105, 193, 355, 653, 1201, 2209, 4063, 7473, 13745, 25281, and 46499.
Given the element position n and optionally some other starting triple of values than (1, 1, 1), compute and return the element in the position n of the resulting Tribonacci series. As usual, the position numbering in a sequence starts from zero. Since n can get pretty large, you can't solve this problem with recursion, since your function would crash with a stack overϐlow once the recursion
limit is exceeded. Instead, you need to remember the three most recent values, and in a loop, use them to compute the next value of the sequence .

|    n   |   start   |     Expected result                  |
| ------ |---------- | -----------------------------------  |
|    0   | (1, 1, 1) |     1                                |
|    10  | (1, 1, 1) |     193                              |
|    10  | (4, 3, 2) |     542                              |
|    100 | (2, 2, 2) |     254143235774005504298869962      |

