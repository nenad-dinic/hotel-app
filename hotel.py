import datetime

def red_u_recnik(red):
    red_r = red.split(',')
    hotel = {'id':red_r[0], 'ime_hotela':red_r[1], 'adresa':red_r[2], 'bazen':red_r[3], 'restoran':red_r[4], 'ocena':float(red_r[5])}
    return hotel

def prikaz_hotela():
    f = open('hoteli.txt', 'r')
    redovi = f.readlines()
    print("ID    |Ime hotela               |Adresa                   |Bazen|Restoran|Ocena")
    print("-------------------------------------------------------------------------------")
    for red in redovi:
        hotel = red_u_recnik(red)
        print(hotel['id'] + '|' + hotel['ime_hotela'].ljust(25) + '|' + hotel['adresa'].ljust(25) + '|' + hotel['bazen'].ljust(5) + '|' + hotel['restoran'].ljust(8) + '|' + str(hotel['ocena']))
    print("-------------------------------------------------------------------------------")

def pretrazi_hotele():
    while True:
        print("1) Pretraga po jednom kriterijumu")
        print("2) Pretraga po vise kriterijuma")
        print("0) Nazad")
        x = int(input("> "))
        if x == 1:
            f = open('hoteli.txt', 'r')
            redovi = f.readlines()
            print("1) ID hotela")
            print("2) Ime hotela")
            print("3) Adresa hotela")
            print("4) Da li hotel ima bazen")
            print("5) Da li hotel ima restoran")
            parametar = int(input("Unesite po cemu pretrazujete:"))
            if parametar == 1 or parametar == 2 or parametar == 3 or parametar == 4 or parametar == 5:
                pretraga = input("Unesite pretragu:")
                print("ID    |Ime hotela               |Adresa                   |Bazen|Restoran|Ocena")
                print("-------------------------------------------------------------------------------")
                for red in redovi:
                    hoteli = red.strip().split(',')
                    if pretraga.lower() in hoteli[parametar-1].lower():
                        hotel = red_u_recnik(red)
                        print(hotel['id'] + '|' + hotel['ime_hotela'].ljust(25) + '|' + hotel['adresa'].ljust(25) + '|' + hotel['bazen'].ljust(5) + '|' + hotel['restoran'].ljust(8) + '|' + str(hotel['ocena']))
                print("-------------------------------------------------------------------------------")
            else:
                print("Invalidan unos")
                break
        elif x == 2:
            f = open('hoteli.txt', 'r')
            redovi = f.readlines()
            print("1) ID hotela")
            print("2) Ime hotela")
            print("3) Adresa hotela")
            print("4) Da li hotel ima bazen")
            print("5) Da li hotel ima restoran")
            parametar1 = int(input("Unesite prvi kriterijum: "))
            parametar2 = int(input("Unesite drugi kriterijum: "))
            if (parametar1 == 1 or parametar1 == 2 or parametar1 == 3 or parametar1 == 4 or parametar1 == 5) and (parametar2 == 1 or parametar2 == 2 or parametar2 == 3 or parametar2 == 4 or parametar2 == 5):
                if parametar1 != parametar2:
                    pretraga1 = input("Unesite pretragu za prvi kriterijum: ")
                    pretraga2 = input("Unesite pretragu za drugi kriterijum: ")
                    print("ID    |Ime hotela          |Adresa                   |Bazen|Restoran|Ocena")
                    print("--------------------------------------------------------------------------")
                    for red in redovi:
                        hoteli = red.strip().split(',')
                        if (pretraga1.lower() in hoteli[parametar1-1].lower()) and (pretraga2.lower() in hoteli[parametar2-1].lower()):
                            hotel = red_u_recnik(red)
                            print(str(hotel['id']) + '|' + hotel['ime_hotela'].ljust(20) + '|' + hotel['adresa'].ljust(25) + '|' + hotel['bazen'].ljust(5) + '|' + hotel['restoran'].ljust(8) + '|' + str(hotel['ocena']))
                    print("-------------------------------------------------------------------------------")
                else:
                    print("Odabrali ste iste parametre")
                    break
            else:
                print("Uneli ste invalidne parametre")
                break
        elif x == 0:
            break
        else:
            print("Invalidan unos!")
            break


def dodaj_hotel():
    while True:
        f_a = open('hoteli.txt', 'a')
        f_r = open('hoteli.txt', 'r')
        redovi = f_r.readlines()
        poslednji_red = redovi[-1]
        poslednji_red_split = poslednji_red.split(',')
        id = int(poslednji_red_split[0])+1
        ime = input("Unesite naziv hotela: ")
        adresa = input("Unesite adresu hotela: ")
        bazen = input("Da li hotel ima bazen: ")
        restoran = input("Da li hotel ima restoran: ")
        ocena = input("Unesite ocenu hotela: ")
        f_a.write(str(id) + ',' + ime + ',' + adresa + ',' + bazen.lower() + ',' + restoran.lower() + ',' + ocena + '\n')
        print("Uspesno ste dodali hotel")
        break

def azuriraj_hotel():
    f_r = open('hoteli.txt', 'r')
    redovi = f_r.readlines()
    f_w = open('hoteli.txt', 'w')
    id_hotela = input("Unesite id hotela kojeg zelite da editujete: ")
    print("1) Ime hotela")
    print("2) Adresa hotela")
    print("3) Da li hotel ima bazen")
    print("4) Da li hotel ima restoran")
    izbor = int(input("Sta zelite da azurirate: "))
    poklapanje = False
    if izbor > 0 and izbor < 5:
        for i in range(len(redovi)):
            hotel = red_u_recnik(redovi[i])
            if id_hotela == hotel['id']:
                poklapanje = True
                if izbor == 1:
                    novo = input("Unesite novo ime hotela: ")
                    hotel['ime_hotela'] = novo
                elif izbor == 2:
                    novo = input("Unesite novu adresu hotela: ")
                    hotel['adresa'] = novo
                elif izbor == 3:
                    novo = input("Da li hotel ima bazen: ")
                    hotel['bazen'] = novo.lower()
                elif izbor == 4:
                    novo = input("Da li hotel ima restoran: ")
                    hotel['restoran'] = novo.lower()
                redovi[i] = hotel['id'] + "," + hotel['ime_hotela'] + "," + hotel['adresa'] + "," + hotel['bazen'] + ',' +  hotel['restoran'] + ',' + str(hotel['ocena']) + '\n'
        f_w.writelines(redovi)
        if poklapanje == False:
            print("-----------------------------")
            print("Ne postoji hotel sa tim ID-em")
            print("-----------------------------")

    else:
        print("invalidan odabir")

def obrisi_hotel():
    f_r = open('hoteli.txt', 'r')
    redovi = f_r.readlines()
    f_w = open('hoteli.txt', 'w')
    id_hotela = input("Unesite id hotela kojeg zelite da obrisete: ")
    poklapanje = False
    for i in range(len(redovi)):
            hotel = red_u_recnik(redovi[i])
            if id_hotela == hotel['id']:
                poklapanje = True
                redovi.remove(redovi[i])
                break
    f_w.writelines(redovi)
    if poklapanje == False:
        print("-----------------------------")
        print("Ne postoji hotel sa tim ID-em")
        print("-----------------------------")

def najbolji_hoteli():
    f = open('hoteli.txt', 'r')
    redovi = f.readlines()
    print("ID    |Ime hotela               |Adresa                   |Bazen|Restoran|Ocena")
    print("-------------------------------------------------------------------------------")
    for i in range(0, len(redovi)-1):
        for j in range(i, len(redovi)):
            if red_u_recnik(redovi[i])['ocena'] < red_u_recnik(redovi[j])['ocena']:
                x = redovi[i]
                redovi[i] = redovi[j]
                redovi[j] = x
    for i in range(5):
        hotel = red_u_recnik(redovi[i])
        print(hotel['id'] + '|' + hotel['ime_hotela'].ljust(25) + '|' + hotel['adresa'].ljust(25) + '|' + hotel['bazen'].ljust(5) + '|' + hotel['restoran'].ljust(8) + '|' + str(hotel['ocena']))

def oceni_hotel(korisnicko_ime):
    today = datetime.datetime.now()
    ime_hotela = input("Unesite ime hotela koji zelite da ocenite: ")
    f_r = open('rezervacije.txt', 'r')
    f_h = open('hoteli.txt', 'r')
    f_o = open('ocene.txt', 'r')
    redovi_r = f_r.readlines()
    redovi_h = f_h.readlines()
    redovi_o = f_o.readlines()
    f_o.close()
    f_o = open('ocene.txt', 'a')
    mozeoceniti = False
    for red in redovi_h:
        hoteli = red.strip().split(',')
        if ime_hotela.lower() in hoteli[1].lower():
            id_hotela = hoteli[0]
    for red in redovi_r:
        rezervacije = red.strip().split(',')
        if rezervacije[0] == id_hotela and rezervacije[5] == korisnicko_ime and datetime.datetime.strptime(rezervacije[4], "%Y-%m-%d") < today:
            mozeoceniti = True
            break

    if mozeoceniti == True:
        vec_ocenjeno = False
        for red in redovi_o:
            ocene = red.strip().split(',')
            if ocene[0] == id_hotela and ocene[1] == korisnicko_ime:
                vec_ocenjeno = True

        if vec_ocenjeno == True:
            print("--------------------------")
            print("Vec ste ocenili ovaj hotel")
            print("--------------------------")
        else:
            ocena = float(input("Ocenite hotel (1.0-10.0): "))
            f_o.write(id_hotela + ',' + korisnicko_ime + ',' + str(ocena) + '\n')
    else:
        print("----------------------------------------")
        print("Nemate isteklu rezervaciju u ovom hotelu")
        print("----------------------------------------")