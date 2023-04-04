animal_type = input("Ievadiet mājdzīvnieka tipu (piemēram, kaķis vai suns): ")
age = int(input("Ievadiet mājdzīvnieka vecumu: "))
breed = input("Ievadiet mājdzīvnieka šķirni: ")
weight = float(input("Ievadiet mājdzīvnieka svaru: "))

def my_function():
  print("Lūdzu, izvēlieties no saraksta:")
  print("1. Barība")
  print("2. Higiēna")
  print("3. Labierīcības")
  print("4. Beigt")
  choice = int(input("Ievadiet savu izvēli (1-4): "))

  if choice == 1:
    print("Barība ir izvēlēta.")
    print("Lūdzu, izvēlieties no saraksta:")
    print("1. Cik bieži jābaro?")
    print("2. Kas jābaro?")
    print("3. Cik daudz jābaro?")
    print("4. Atgriezties atpakaļ")

    inner_choice = int(input("Ievadiet savu izvēli (1-4): "))
    if inner_choice == 1:
      print("Mājdzīvnieku jābaro vismaz divas reizes dienā.")
      my_function()
    elif inner_choice == 2:
      print("Atkarīgs no mājdzīvnieka tipa un veselības stāvokļa, bet parasti tiek barots ar speciāliem mājdzīvnieku barības maisījumiem.")
      my_function()
    elif inner_choice == 3:
      print("Dažādiem mājdzīvniekiem var būt atšķirīgs barības daudzums un biežums, tāpēc ir ieteicams konsultēties ar veterinārārstu.")
      my_function()
    elif inner_choice == 4:
      my_function()
    else:
      print("Nepareiza izvēle. Lūdzu, izvēlieties atkārtoti.")
  elif choice == 2:
      print("Higiēna ir izvēlēta.")
      print("Lūdzu, izvēlieties no saraksta:")
      print("1. Kāds šampūns?")
      print("2. Cik bieži?")
      print("3. Mazgāšanas tehnika?")
      print("4. Atgriezties atpakaļ")
      inner_choice = int(input("Ievadiet savu izvēli (1-4): "))

      if inner_choice == 1:
        print("Ieteicams izmantot speciālu šampūnu dzīvniekiem.")
        my_function()
      elif inner_choice == 2:
        print("Biežums atkarīgs no dzīvnieka sugas un garuma. Parasti reizi mēnesī vai retāk.")
        my_function()
      elif inner_choice == 3:
        print("Ieteicams izmantot silto ūdeni, piemērotu šampūnu, masējošus kustības un rūpīgi noskalojot matus.")
        my_function()
      elif   inner_choice == 4:
        my_function()       
      else:
        print("Nepareiza izvēle. Lūdzu, izvēlieties atkārtoti.")

  elif choice == 3:
      print("Labierīcības ir izvēlētas.")
      print("Lūdzu, izvēlieties no saraksta:")
      print("1. Cik bieži jātīra kaste?")
      print("2. Kā jātīra kaste?")
      print("3. Kas vajadzīgs?")
      print("4. Atgriezties atpakaļ")
      inner_choice = int(input("Ievadiet savu izvēli (1-4): "))                          
      if inner_choice == 1:
          print("Kaste jātīra vismaz reizi dienā.")
          my_function()
      elif inner_choice == 2:
          print("Kasti var tīrīt ar sūkli un dezinfekcijas līdzekli.")
          my_function()
      elif inner_choice == 3:
          print("Lai notīrītu kasti, jums var būt vajadzīgs sūklis, dezinfekcijas līdzeklis, cimdus.")
          my_function()
      elif inner_choice == 4:
        my_function()
      else:
          print("Nepareiza izvēle. Lūdzu, izvēlieties atkārtoti.")
          my_function()
    
  elif choice == 4:
    print("Uz tikšanos!")
my_function()