# Stwórz listę liczb od 0 do 999.
# Liczby podzielne przez 3 zastąp słowem 'trzy'.
# Liczby podzielne przez 5 zastąp słowem 'pięć'.
# Liczby podzielne jednocześnie przez 3 i 5 zastąp słowem 'trzypięć'.
# Wynikową listę przypisz zmiennej result.

result = None

l = []
for x in range(1000):
    if x % 15 == 0:
        l.append('trzypięć')
    elif x % 3 == 0:
        l.append('trzy')
    elif x % 5 == 0:
        l.append('pięć')
    else:
        l.append(x)

print(l)
result = l
assert result[15] == 'trzypięć'
