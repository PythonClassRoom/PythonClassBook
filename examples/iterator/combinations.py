import itertools

#Permutation (order matters):
print(list(itertools.permutations([1,2,3,4], 2)))
"""
[(1, 2), (1, 3), (1, 4),
(2, 1), (2, 3), (2, 4),
(3, 1), (3, 2), (3, 4),
(4, 1), (4, 2), (4, 3)]"""

#Combination (order does NOT matter):
print(list(itertools.combinations('123', 2)))
"""
[('1', '2'), ('1', '3'), ('2', '3')]
"""

#Cartesian product (with several iterables):
print(list(itertools.product([1,2,3], [4,5,6])))
"""
[(1, 4), (1, 5), (1, 6),
(2, 4), (2, 5), (2, 6),
(3, 4), (3, 5), (3, 6)]
"""

#Cartesian product (with one iterable and itself):
print(list(itertools.product([1,2], repeat=3)))
"""
[(1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2),
(2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2)]
"""