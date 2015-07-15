import timeit
import random
import tabulate

ns = [10**(i+1) for i in range(7)]

rand_shuff = """random.shuffle(ls)"""
pyudo_shuf = """pyudorandom.shuffle(ls)"""
pyudo_it = """\
for i in pyudorandom.items(ls):
    pass
"""


print(ns)
results = [['rand'], ['pysh'], ['pyit']]
for n in ns:
    ls = list(range(n))
    name_space = {'ls': ls}
    results[0].append(
        timeit.timeit(rand_shuff, 'import random', number=10, globals=name_space) 
    )
    results[1].append(
        timeit.timeit(pyudo_shuf, 'import pyudorandom', number=10, globals=name_space)
    )
    results[2].append(
        timeit.timeit(pyudo_it, setup='import pyudorandom', number=10, globals=name_space)
    )

print(tabulate.tabulate(results, tablefmt='pipe'))
