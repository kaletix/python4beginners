# Napisać kod tworzący listę list kolejnych elementów parzystych < 100 według
# schematu: [[0], [2], ... , [98]]. Wynikową listę przypisz na zmienną result.

result = None
l = []
for x in range(0, 100, 2):
    l.append([x])
result = l
assert result[1] == [2]


