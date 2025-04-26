categories = []
values = []
tros = 0
zar = input("Ukupna zarada: $")
print("Za odabir kalkulatora upišite broj 1")
broj = input("Za odabir automatske podjele novaca upišite broj 2\n")
if (int(broj) == 1):
    while True:
        category = input("\nUpišite kategorije (ili 'kraj' za kraj): ")
        if category.lower() == "kraj":
            break
        if category not in categories:
            categories.append(category)
        else:
            print("Kategorija već postoji.")

    while True:
        items = input("\nUpišite troškove kategorija (ili 'kraj' za kraj): $")
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

elif (int(broj) == 2):
    p = float(zar) * 0.5
    z = float(zar) * 0.3
    i = float(zar) * 0.2

    print("\n50-30-20 pravilo\n")
    print("50% na potrebe: $" + str(p))
    print("30% na želje: $" + str(z))
    print("20% na investiije: $" + str(i))

else:
    print("Netocan odabir!")
