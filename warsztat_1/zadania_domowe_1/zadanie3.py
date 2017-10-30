# Stwórz listę 100 list, każda z liczbami od 1 do 100. Potem dla każdej j-tej
# z tych list wewnętrznych na jej końcu dodać sumę jej pierwszych elementów
# do j-tego włącznie.
# Spodziewany efekt: [ [1, 2, 3, ..., 100, 1], [1, 2, 3, ..., 100, 3],
# [1, 2, 3, ..., 100, 6], ..., [1, 2, 3, ..., 100, 5050] ]
# Wynikową listę przypisz na zmienną result

result = None
s = 0

l = []
for j in range(1, 101):
    a = [i for i in range(1, 101)]
    s += a[j - 1]
    a.append(s)
    l.append(a)
print(l)
result = l
assert result[-1][-1] == 5050
