animal_type = input("Ievadiet mājdzīvnieka tipu (piemēram, kaķis vai suns): ")
age = int(input("Ievadiet mājdzīvnieka vecumu: "))
breed = input("Ievadiet mājdzīvnieka šķirni: ")
weight = float(input("Ievadiet mājdzīvnieka svaru: "))

while True:
    print("Lūdzu, izvēlieties no saraksta:")
    print("1. Bariba")
    print("2. Higēna")
    print("3. Labierīcības")

    choice = int(input("Ievadiet savu izvēli (1-3): "))

    if choice == 1:
        print("Bariba ir izvēlēta.")
        while True:
            print("Lūdzu, izvēlieties no saraksta:")
            print("1. Cik bieži jābaro?")
            print("2. Kas jābaro?")
            print("3. Cik daudz jābaro?")
            print("4. Atgriezties atpakaļ")

            inner_choice = int(input("Ievadiet savu izvēli (1-4): "))

            if inner_choice == 1:
                print("Mājdzīvnieku jābaro vismaz divas reizes dienā.")
            elif inner_choice == 2:
                print("Atkarīgs no mājdzīvnieka tipa un veselības stāvokļa, bet parasti tiek barots ar speciāliem mājdzīvnieku barības maisījumiem.")
            elif inner_choice == 3:
                print("Dažādiem mājdzīvniekiem var būt atšķirīgs barības daudzums un biežums, tāpēc ir ieteicams konsultēties ar veterinārārstu.")
            elif inner_choice == 4:
                break
            else:
                print("Nepareiza izvēle. Lūdzu, izvēlieties atkārtoti.")
              
    elif choice == 2:
      print("Higēna ir izvēlēta.")
    print("Lūdzu, izvēlieties no saraksta:")
    print("1. Kads shampuns?")
    print("2. Cik biezi?")
    print("3. Mazgāšanas tehnika?")

    inner_choice = int(input("Ievadiet savu izvēli (1-3): "))

    if inner_choice == 1:
        print("Ieteicams izmantot speciālu šampūnu dzīvniekiem.")
    elif inner_choice == 2:
        print("Biežums atkarīgs no dzīvnieka sugas un garuma. Parasti reizi mēnesī vai retāk.")
    elif inner_choice == 3:
        print("Ieteicams izmantot silto ūdeni, piemērotu šampūnu, masējošus kustības un rūpīgi noskalojot matus.")
    else:
        print("Nepareiza izvēle. Lūdzu, izvēlieties atkārtoti.")

    elif choice == 3:
      print("Labierīcības ir izvēlētas.")
      print("Lūdzu, izvēlieties no saraksta:")
      print("1. Cik bieži jātīra kaste?")
      print("2. Kā jātīra kaste?")
      print("3. Kas vajadzīgs?")
      inner_choice = int(input("Ievadiet savu izvēli (1-3): "))                          
      if inner_choice == 1:
          print("Kaste jātīra vismaz reizi dienā.")
      elif inner_choice == 2:
          print("Kasti var tīrīt ar sūkli un dezinfekcijas līdzekli.")
      elif inner_choice == 3:
          print("Lai notīrītu kasti, jums var būt vajadzīgs sūklis, dezinfekcijas līdzeklis, cimdus.")
      else:
          print("Nepareiza izvēle. Lūdzu, izvēlieties atkārtoti.")
  else:
      print("Nepareiza izvēle. Lūdzu, izvēlieties atkārtoti.")

                    
  