# Chcemy napisać sprawdzarkę do testu znajomości stolic europejskich.
# Format listy stolic taki jak w pliku stolice.csv
# Format pytań taki jak w pliku pytania.csv
# Format odpowiedzi taki jak w pliku odpowiedzi.csv

# Napisz funkcję check_homework, która przyjmuje trzy argumenty:
# - capitals_csv to ścieżka do pliku, który zawiera listę stolic europejskich
# - questions_csv to ścieżka pliku csv, który zawiera pytania
# - answers_csv to ścieżka pliku, który zawiera odpowiedzi
# Funkcja zwraca liczbę poprawnych odpowiedzi

import csv


def check_homework(capitals_csv, questions_csv, answers_csv):
    szablon = {}
    dobre_odpowiedzi = {}
    dobrze = 0

    with open(capitals_csv, 'r', encoding='utf8') as stolice:
        dane = {}
        reader = csv.reader(stolice, delimiter=';')
        next(reader)  # pominięcie nagłówka
        for row in reader:
            dane[row[0]] = row[1]
        # print(dane)


    with open(questions_csv, 'r', encoding='utf8') as pytania:
        pytanie = {}
        reader2 = csv.reader(pytania, delimiter=';')
        next(reader2)  # pominięcie nagłówka
        for row in reader2:
            # print(row[1:6])
            pytanie[row[0]] = row[1:6]
    # print(pytanie)

    for key in dane:
        if key in pytanie:
            szablon[key] = dane[key]

    for k in pytanie.keys():
        for i, j in enumerate(pytanie[k]):
            if j == szablon[k]:
                dobre_odpowiedzi[k] = i  # tutaj do słownika
    print(dobre_odpowiedzi)

    with open(answers_csv, 'r', encoding='utf8') as odpowiedzi:
        odpowiedź = {}
        reader3 = csv.reader(odpowiedzi)
        next(reader3)  # pominięcie nagłówka
        for i, j in enumerate(reader3): #zamiast odpowiedzi sa inty odpowienio 0=A, 1=B, 2=C, 3=D
            if j[0] == 'A':
                odpowiedź[i] = 0
            if j[0] == 'B':
                odpowiedź[i] = 1
            if j[0] == 'C':
                odpowiedź[i] = 2
            if j[0] == 'D':
                odpowiedź[i] = 3
    print(odpowiedzi)
    for v, w in zip(dobre_odpowiedzi.values(), odpowiedź.values()):
        if v == w:
            dobrze += 1

    return dobrze


# assert check_homework('stolice.csv', 'pytania.csv', 'odpowiedzi.csv') == 5
print(check_homework('stolice.csv', 'pytania.csv', 'odpowiedzi.csv'))
