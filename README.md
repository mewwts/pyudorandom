# pyudorandom
The pyudorandom module lets you iterate over a list in a non-succsessive, yet deterministic way. 
It comes in handy when you want to mix up the items, but don't need any guarantees of randomness. 

If you have a iterable of length `n`, pyudorandom will first find a random number `m` between `0` and `n-1` such that the `gcd(m, n) == 1`. That number will then be used to generate `0` through `n-1` by using [integers modulo `n`](http://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n).

# API
```Python 
from pyudorandom import pyudorandom

ls = [ ... ]
randomly_ordered_ls = [ls[i] for i in pyudorandom(len(ls)):
```
