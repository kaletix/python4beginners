import csv

with open('conferences_data.csv')as f:
    d = {}
    reader = csv.reader(f, delimiter=';')
    next(reader)  # pominięcie nagłówka
    for row in reader:
        for conf, email in enumerate(row):
            if not email:
                continue
            try:
                conferences = d[email]
            except KeyError:
                conferences = set()
                d[email] = conferences
            conferences.add(conf)

def get_company_from_email(email):
    _, rest = email.split('@') #podłoga - wczesnijsze znaki nas nie interesują
    company, _ = rest.split('.')
    return company

def get_country_from_email(email):
    _, rest = email.split('@') #podłoga - wczesnijsze znaki nas nie interesują
    _, country = rest.split('.')
    return country

result1 = len([email for email in d if len(d[email])>1])
print(result1)
result2 = len([
    email for email in d
    if get_company_from_email(email) == 'wok'
])
print(result2)

result3 = len(set([get_country_from_email(email) for email in d]))
print(result3)

