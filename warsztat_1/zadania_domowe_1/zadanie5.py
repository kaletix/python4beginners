# Powerset - Napisz kod tworzęcy ze zbioru A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# zbiór zawierający wszystkie podzbiory A (włącznie z pustym i A).
# UWAGA: w python zbiory (set) nie mogą być elementami innych zbiorów,
# proszę użyć frozenset jako zbiorów wewnętrznych.
# Wynik przypisz na zmienną result
import random
import itertools

# random.sample(set([1, 2, 3, 4, 5, 6]), 2)
result = None
t = list()

A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

for i in range(len(A) + 1):
    t += tuple(itertools.combinations(A, i))

s = list()

for x in t:
    s.append(frozenset(x))

print(s)
result = s
assert frozenset((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)) in result
