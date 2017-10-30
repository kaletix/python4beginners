# Napisz kod transformujący podany słownik:
# {
#     1: 'Poniedziałek',
#     2: 'Wtorek',
#     3: 'Środa',
#     4: 'Czwartek',
#     5: 'Piątek',
#     6: 'Sobota',
#     7: 'Niedziela'
# }
# do postaci:
# {
#     'Poniedziałek': 1,
#     'Środa': 3,
#     'Piątek': 5,
#     'Niedziela': 7
# }
# (Zamiana klucza z wartością i zostawienie tylko dni nieparzystych).
# Wynik przypisz na zmienną result

a = {}
result = {
    1: 'Poniedziałek',
    2: 'Wtorek',
    3: 'Środa',
    4: 'Czwartek',
    5: 'Piątek',
    6: 'Sobota',
    7: 'Niedziela'
}
for x in range(1, 8):
    if x % 2 == 0:
        del result[x]
for x, y in result.items():
    #print(x)
    a[y] = x
result = a
print(a)
assert 'Poniedziałek' in result
