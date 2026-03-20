dane = "Alice,28,Data Scientist,75000"
imie, wiek, zawod, zarobki = dane.split(',')
print(f'{imie} ma {wiek} lat, pracuje jako {zawod} i zarabia {zarobki} zł')

nazwa_pliku = 'model_results_2024_Q3.csv'
parts = nazwa_pliku.split('_')
parts[-1] = parts[-1].replace('.csv', '')
print(nazwa_pliku)


lista_elem = [23, 24, 22, 150, 23, 25, -10, 24, 23]
lista_elem = [x for x in lista_elem if x  >= 20 and x <= 30]
print(lista_elem)

ransactions = [
('food', 50),
('transport', 20),
('food', 30),
('entertainment', 40),
('transport', 15),
('food', 25)
]


result = {}

for category, amount in ransactions:
    if category in result:
        result[category] += amount
    else:
        result[category] = amount

print(result)

