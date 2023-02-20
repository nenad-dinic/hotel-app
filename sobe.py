def pretrazi_sobe(id_hotela):
    while True:
        print("1) Pretraga po jednom kriterijumu")
        print("2) Pretraga po vise kriterijuma")
        print("0) Nazad")
        x = int(input("> "))
        if x == 1:
            f = open('sobe.txt', 'r')
            redovi = f.readlines()
            print("1) Broj sobe")
            print("2) Broj kreveta")
            print("3) Tip sobe (apartman ili jedna soba)")
            print("4) Da li ima klimu")
            print("5) Da li ima TV")
            parametar = int(input("Unesite po cemu pretrazujete:"))
            if parametar == 1 or parametar == 2 or parametar == 3 or parametar == 4 or parametar == 5:
                pretraga = input("Unesite pretragu:")
                print("Broj sobe|Broj kreveta|Tip sobe  |Klima|TV|")
                print("-------------------------------------------")
                for red in redovi:
                    sobe = red.strip().split(',')
                    if pretraga.lower() in sobe[parametar].lower():
                        if sobe[0] == id_hotela:
                            print(sobe[1].ljust(9) + '|' + sobe[2].ljust(12) + '|' + sobe[3].ljust(10) + '|' + sobe[4].ljust(5) + '|' + sobe[5].ljust(2) + '|')
            else:
                print("Invalidan unos")
                break
        elif x == 2:
            f = open('sobe.txt', 'r')
            redovi = f.readlines()
            print("1) Broj sobe")
            print("2) Broj kreveta")
            print("3) Tip sobe (apartman ili jedna soba)")
            print("4) Da li ima klimu")
            print("5) Da li ima TV")
            parametar1 = int(input("Unesite prvi kriterijum: "))
            parametar2 = int(input("Unesite drugi kriterijum: "))
            if (parametar1 == 1 or parametar1 == 2 or parametar1 == 3 or parametar1 == 4 or parametar1 == 5) and (parametar2 == 1 or parametar2 == 2 or parametar2 == 3 or parametar2 == 4 or parametar2 == 5):
                if parametar1 != parametar2:
                    pretraga1 = input("Unesite pretragu za prvi kriterijum: ")
                    pretraga2 = input("Unesite pretragu za drugi kriterijum: ")
                    print("Broj sobe|Broj kreveta|Tip sobe  |Klima|TV|")
                    print("-------------------------------------------")
                    for red in redovi:
                        sobe = red.strip().split(',')
                        if (pretraga1.lower() in sobe[parametar1].lower()) and (pretraga2.lower() in sobe[parametar2].lower()):
                            if sobe[0] == id_hotela:
                                print((sobe[1].ljust(9)) + '|' + (sobe[2].ljust(12)) + '|' + sobe[3].ljust(10) + '|' + sobe[4].ljust(5) + '|' + sobe[5].ljust(2) + '|')
                else:
                    print("Odabrali ste iste parametre")
                    break
            else:
                print("Uneli ste invalidan parametar")
                break
        elif x == 0:
            break
        else:
            print("Invalidan unos!")
            break