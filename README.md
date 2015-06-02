# pyudorandom
The pyudorandom module lets you iterate over a list in a non-succsessive, yet deterministic way. 
It comes in handy when you want to mix up the items, but don't need any guarantees of randomness. Also, it makes sure that it only gives you the elements once.

If you have a iterable of length `n`, pyudorandom will first find a random number `m` between `0` and `n-1` such that the `gcd(m, n) == 1`. That number will then be used to generate `0` through `n-1` by using [integers modulo `n`](http://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n).

As such, it might be slow on small data, but shall be significantly faster
than random.shuffle for longer lists.

# API
Given a list `ls = [1, 5, 7, 3, ..., 321, 994]` and the imported module `import pyudorandom`.
##pyudorandom.items(ls)
Draw 'random' items from ls.
```Python 
>>> for i in pyudorandom.items(ls):
...     print(i)
...
7
321
...
...
5
```

##pyudorandom.shuffle(ls)
Get a new list with the elements of ls in a new order.
```Python
>>> new_order = pyudorandom.shuffle(ls)
>>> new_order == ls
False
>>> set(new_order) == set(ls)
True
```
##pyudorandom.indices(ls)
Get the indices of the list in a 'random' order.

