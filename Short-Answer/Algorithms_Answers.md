#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) - Linear

> The runtime/ space grows at same rate, runs n times

```
for n = 2, runs 2 times, for a = 0, 4

for n = 3, runs 3 times, for a = 0, 9, 18
```

b) O(n log n) - Linearthmetic

> First loop grows with n but second loop grows slower

c) O(n) - Linear

> Runtime and space grows at same rate as `bunnies`

## Exercise II

> 1. I would conduct a binary search:
>    First I would find the midpoint - `n // 2` and drop an egg
> 2. Depending on the result, I would eliminate half
>    `if egg breaks, eliminate bottom half and search in top half else, search bottom half`
> 3. Continue until I find floor `f`
