# Zaimplementuj klasę Date, która tworzona jest na podstawie trzech wartości - day, month i year.
# Obiekt klasy powinien zawierać atrybuty day, month i year

# Twoim zadaniem jest sprawdzenie w trakcie tworzenia obiektu, czy podane wartości są poprawne:
# jeśli year nie jest intem - rzucić InvalidYearError
# jeśli month nie jest intem lub nie zawiera się w przedziale od 1 do 12 - rzucić InvalidMonthError
# jeśli day nie jest intem lub nie zawiera się w przedziale o 1 do 28/30/31 (odpowiednio w zależności od miesiąca) - rzucić InvalidDayError

# Wszystkie opisane powyżej błędy powinny dziedziczyć z bazowego błędu - DateError

# W zadaniu dla uproszczenia zakładamy, że każdy luty ma 28 dni ;)

class InvalidYearError(Exception):
    pass

class InvalidMonthError(Exception):
    pass

class InvalidDayError(Exception):
    pass

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        thirties = [4, 6, 9, 11]
        try:
            print(int(self.year))
        except ValueError as e:
            print('nie int')
            raise e
        if not int(self.year):
            raise InvalidYearError
        if not int(self.month) or (self.month > 12 or self.month < 1):
            raise InvalidMonthError
        if not int(self.day):
            raise InvalidDayError
        if self.day < 1 or self.day > 31:
            raise InvalidDayError
        elif self.month == 2 and self.day > 28:
            raise InvalidDayError
        elif (self.month == i for i in thirties) and self.day > 30:
            raise InvalidDayError


date = Date(30, 5, 'j')
assert date.day == 30
assert date.month == 5
assert date.year == 2020

try:
    date2 = Date(6, 'y', 2020)
except InvalidDayError:
    print('Błąd wyrzucony tak jak trzeba')
else:
    print('Bez błędu, a trzeba było :(')
