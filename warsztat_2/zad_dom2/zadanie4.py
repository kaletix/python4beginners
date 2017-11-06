# Zadanie 4
# Napisz funkcję factorial, która dla danego n obliczy rekurencyjnie silnię

def factorial(n):
    if n < 0:
        print("error")
        return None
    elif n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return factorial(n - 1) * n


assert factorial(5) == 120
