lista_zakupow = {
    "intersport": ["skarpety", "bluza", "gogle", "kijki"],
    "apteka": ["aspiryna", "multiwitamina", "rutinoscorbin"],
    "carrefour": ["wódka", "pepsi", "lód"]
}
print("Lista zakupów")
for keys, values in lista_zakupow.items():
  if keys == "intersport":
    print(f"Idę do {keys.title()}, kupuję tu następujące rzeczy: {str(values).title()}.")

for keys, values in lista_zakupow.items():
  if keys == "apteka":
    print (f"Idę do {keys.title()}, kupuję tu następujące rzeczy: {str(values).title()}.")

for keys, values in lista_zakupow.items():
    if keys == "carrefour":
        print(f"Idę do {keys.title()}, kupuję tu następujące rzeczy {str(values).title()}.")

number = []
for x in lista_zakupow.values():
  y = len(x)
  number.append(y)
print(f"W sumie kupuję {sum(number)} produktów.")

print("Ale to było dobre!")

list_of_shops = ["Wroclavia", "Magnolia", "Borek"]

for i in list_of_shops:
  print(i)