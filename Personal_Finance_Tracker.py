categories = []
values = []
tros = 0
zar = input("Ukupna zarada: $")


while True:
    category = input("Upišite kategorije (ili 'kraj' za kraj): ")
    if category.lower() == "kraj":
        break
    if category not in categories:
        categories.append(category)
    else:
        print("Kategorija već postoji.")

while True:
    items = input("Upišite troškove kategorija (ili 'kraj' za kraj): $")
    if items.lower() == "kraj":
        break
    if items not in values:
        values.append(items)
    else:
        values.append(items)

item_values = dict(zip(categories, values))
print("\nKategorije:")
for cat in categories:
    print(cat+":") 
    print("$"+item_values[cat])  
    tros = float(tros) + float(item_values[cat])

print("Zarada je $" + str(zar) + " , a trošak $" + str(tros) + "   Ostalo je $" + str(float(zar)-float(tros)))