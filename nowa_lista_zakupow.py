lista_zakupow = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
print("Lista zakupów")
for keys, values in lista_zakupow.items():
  if keys == "piekarnia":
    print(f"Idę do {keys.title()}, kupuję tu następujące rzeczy: {str(values).title()}.")
    

for keys, values in lista_zakupow.items():
  if keys == "warzywniak":
    print (f"Idę do {keys.title()}, kupuję tu następujące rzeczy: {str(values).title()}.")

number = []
for x in lista_zakupow.values():
  y = len(x)
  number.append(y)
print(f"W sumie kupuję {sum(number)} produktów.")