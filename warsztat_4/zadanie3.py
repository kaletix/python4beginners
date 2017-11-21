


# Chcemy napisać kod, który dla danego pliku z listą stolic wygeneruje number_of_sets zestawów pytań po number_of_questions_per_set pytań
# - Format listy stolic taki jak w stolice.csv
# - Format oczekiwanego pojedynczego zestawu pytań taki jak w pliku pytania.csv - prosimy pamiętać o nagłówkach
# - Każdy zestaw powinien znaleźć się w osobnym pliku - pierwszy w zestaw1.csv, drugi w zestaw2.csv itd (nie ma czegoś takiego jak zestaw 0)
# - pliki zestaw1.csv, zestaw2.csv itd. powinny się stworzyć w folderze z rozwiązaniem zadania (tzn. przy otwieraniu pliku nie podawać żadnej ścieżki, tylko samą nazwę pliku)
#
# Dodatkowe założenia:
# Pytanie o jeden kraj nie może wystąpić więcej niż raz (biorąc pod uwagę wszystkie zestawy)
# W przypadku, gdy ktoś poda nam dane, dla których musielibyśmy wygenerować więcej niż 48 pytań (tyle mamy stolic w pliku stolice.csv) - rzućmy ValueError
# Poprawna odpowiedź powinna znajdować się w losowej kolumnie - tzn. losowo powinna być odpowiedzią A, B, C lub D
# Do losowania należy skorzystać z modułu random https://docs.python.org/3/library/random.html

import csv
import random

def create_sets_of_question(capitals_csv, number_of_sets, number_of_questions_per_set):
    opcje_odpowiedzi = set()
    dane_państwa = []
    dane_stolice = []
    wariacje = {}
    tablica = []
    ograniczone_odpowiedzi = set()

    group_of_items = {1, 2, 3, 4}  # a sequence or set will work here.
    num_to_select = 2  # set the number to select here.
    list_of_random_items = random.sample(group_of_items, num_to_select)

    with open(capitals_csv, encoding='utf8') as stolice:
        dane = {}
        reader = csv.reader(stolice, delimiter=';')
        next(reader)  # pominięcie nagłówka
        for row in reader:
            dane[row[0]] = row[1]
        print(dane)

    def clear(x):
        return type(x)()

    for k, v in dane.items():
        dane_państwa.append(k)
        dane_stolice.append(v)
        opcje_odpowiedzi.add(v) #set ze wszystkimi stolicami


    for k, v in dane.items():
        ograniczone_odpowiedzi = set(opcje_odpowiedzi)
        ograniczone_odpowiedzi.remove(v)
        tablica = random.sample(ograniczone_odpowiedzi, 3)
        tablica.append(v)
        random.shuffle(tablica)
        wariacje[k]=tablica
        tablica = clear(tablica)
        ograniczone_odpowiedzi= clear(ograniczone_odpowiedzi)
    print(wariacje)

    if number_of_sets*number_of_questions_per_set>48:
        raise ValueError
    else:
        for i in range(1, number_of_sets+1):
            nazwa='zestaw'+str(i)+'.csv'
            f = open(nazwa, 'w')
            f.write('Państwo;A;B;C;D\n')
            for j, k in enumerate(wariacje):
                if j>=((i-1)*number_of_questions_per_set) and j<(i*number_of_questions_per_set):
                    w=wariacje[k]
                    f.write(k+';'+w[0]+';'+w[1]+';'+w[2]+';'+w[3]+'\n')
                    w = clear(w)
            f.close()


#
create_sets_of_question('stolice.csv', 1, 8)

with open('zestaw1.csv') as zestaw1:
    reader = csv.reader(zestaw1, delimiter=';')
    lines_count = 0
    for row in reader:
        print(row)
        assert len(row) == 5  # 5 kolumn - Państwo + propozycje odpowiedzi A, B, C, D
        lines_count += 1
    assert lines_count == 9  # 8 pytan + naglowek

try:
    create_sets_of_question('stolice.csv', 5, 10)
except ValueError:
    print('Błąd wyrzucony tak jak trzeba')
else:
    print('Bez błędu, a trzeba było :(')
