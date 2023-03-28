# Ievada informāciju par mājdzīvnieku
animal_type = input("Ievadiet mājdzīvnieka tipu (piemēram, kaķis vai suns): ")
age = int(input("Ievadiet mājdzīvnieka vecumu: "))
breed = input("Ievadiet mājdzīvnieka šķirni: ")
weight = float(input("Ievadiet mājdzīvnieka svaru: "))

# Piedāvā izvēlēties no saraksta
print("Lūdzu, izvēlieties no saraksta:")
print("1. Bariba")
print("2. Higēna")
print("3. Labierīcības")

# Ievada izvēli
choice = int(input("Ievadiet savu izvēli (1-3): "))

# Pārbauda lietotāja izvēli un izpilda atbilstošas darbības
if choice == 1:
    print("Bariba ir izvēlēta.")
    # Veic darbības saistībā ar barību
elif choice == 2:
    print("Higēna ir izvēlēta.")
    # Veic darbības saistībā ar higiēnu
elif choice == 3:
    print("Labierīcības ir izvēlētas.")
    # Veic darbības saistībā ar labierīcībām
else:
    print("Nepareiza izvēle. Lūdzu, izvēlieties atkārtoti.")
