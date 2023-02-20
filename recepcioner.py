def red_u_recnik(red):
    red_r = red.split(',')
    recepcioner = {'korisnicko_ime':red_r[0], 'lozinka':red_r[1], 'ime':red_r[2], 'prezime':red_r[3], 'br_telefona':red_r[4], 'email':(red_r[5]), 'uloga':(red_r[6]), 'id_hotela':(red_r[7])}
    return recepcioner

def dodaj_recepcionera():
    while True:
        korisnicko_ime = input("Unesite korisnicko ime recepcionera: ")
        lozinka = input("Unesite lozinku za recepcionera: ")
        ime = input("Unesite ime recepcionera: ")
        prezime = input("Unesite prezime recepcionera: ")
        broj_telefona = input("Unesite broj telefona recepcionera: ")
        email = input("Unesite email recepcionera: ")
        ime_hotela = input("Unesite naziv hotela u kome radi recepcioner: ")
        f_h = open('hoteli.txt', 'r')
        f_k = open('korisnici.txt', 'a')
        redovi = f_h.readlines()
        for red in redovi:
            hoteli = red.strip().split(',')
            if ime_hotela.lower() in hoteli[1].lower():
                id_hotela = hoteli[0]
                break
        f_k.write(korisnicko_ime + ',' + lozinka + ',' + ime + ',' + prezime + ',' + broj_telefona + ',' + email + ',' + 'recepcioner' + ',' + id_hotela + '\n')
        print("Uspesno ste dodali recepcionera")
        break

def pretrazi_recepcionere():
    while True:
        print("1) Pretraga po jednom kriterijumu")
        print("2) Pretraga po vise kriterijuma")
        print("0) Nazad")
        x = int(input("> "))
        if x == 1:
            f = open('korisnici.txt', 'r')
            h = open('hoteli.txt', 'r')
            redovi_f = f.readlines()
            redovi_h = h.readlines()
            print("1) Korisnicko ime recepcionera")
            print("2) Ime recepcionera")
            print("3) Prezime recepcionera")
            print("4) Broj telefona")
            print("5) Email")
            parametar = int(input("Unesite po cemu pretrazujete:"))
            if parametar > 0 and parametar < 6:
                pretraga = input("Unesite pretragu:")
                print("Korisnicko ime |Ime            |Prezime        |Broj telefona|Email                    |Ime hotela               |")
                print("------------------------------------------------------------------------------------------------------------------")
                for red in redovi_f:
                    recepcioner = red.strip().split(',')
                    for red1 in redovi_h:
                        hotel = red1.strip().split(',')
                        if hotel[0] == recepcioner[7]:
                            if recepcioner[6] == 'recepcioner':
                                if parametar == 1:
                                    if pretraga.lower() in recepcioner[parametar-1].lower():
                                        print(recepcioner[0].ljust(15) + '|' + recepcioner[2].ljust(15) + '|' + recepcioner[3].ljust(15) + '|' + recepcioner[4].ljust(13) + '|' + recepcioner[5].ljust(25) + '|' + hotel[1].ljust(25) + '|')
                                else:
                                    if pretraga.lower() in recepcioner[parametar].lower():
                                        print(recepcioner[0].ljust(15) + '|' + recepcioner[2].ljust(15) + '|' + recepcioner[3].ljust(15) + '|' + recepcioner[4].ljust(13) + '|' + recepcioner[5].ljust(25) + '|' + hotel[1].ljust(25) + '|')
            else:
                print("Invalidan unos")
                break

        elif x == 2:
            f = open('korisnici.txt', 'r')
            h = open('hoteli.txt', 'r')
            redovi_f = f.readlines()
            redovi_h = h.readlines()
            print("1) Korisnicko ime recepcionera")
            print("2) Ime recepcionera")
            print("3) Prezime recepcionera")
            print("4) Broj telefona")
            print("5) Email")
            parametar1 = int(input("Unesite prvi kriterijum: "))
            parametar2 = int(input("Unesite drugi kriterijum: "))
            if (parametar1 == 1 or parametar1 == 2 or parametar1 == 3 or parametar1 == 4 or parametar1 == 5) and (parametar2 == 1 or parametar2 == 2 or parametar2 == 3 or parametar2 == 4 or parametar2 == 5):
                if parametar1 != parametar2:
                    pretraga1 = input("Unesite pretragu za prvi kriterijum: ")
                    pretraga2 = input("Unesite pretragu za drugi kriterijum: ")
                    print("Korisnicko ime |Ime            |Prezime        |Broj telefona|Email                    |Ime hotela               |")
                    print("------------------------------------------------------------------------------------------------------------------")
                    for red in redovi_f:
                        recepcioner = red.strip().split(',')
                        for red1 in redovi_h:
                            hotel = red1.strip().split(',')
                            if hotel[0] == recepcioner[7]:
                                if recepcioner[6] == 'recepcioner':
                                    if parametar1 == 1:
                                        if pretraga1.lower() in recepcioner[parametar1-1].lower() and pretraga2.lower() in recepcioner[parametar2].lower():
                                            print(recepcioner[0].ljust(15) + '|' + recepcioner[2].ljust(15) + '|' + recepcioner[3].ljust(15) + '|' + recepcioner[4].ljust(13) + '|' + recepcioner[5].ljust(25) + '|' + hotel[1].ljust(25) + '|')
                                    elif parametar2 == 2:
                                        if pretraga1.lower() in recepcioner[parametar1].lower() and pretraga2.lower() in recepcioner[parametar2-1].lower():
                                            print(recepcioner[0].ljust(15) + '|' + recepcioner[2].ljust(15) + '|' + recepcioner[3].ljust(15) + '|' + recepcioner[4].ljust(13) + '|' + recepcioner[5].ljust(25) + '|' + hotel[1].ljust(25) + '|')
                                    else:
                                        if pretraga1.lower() in recepcioner[parametar1].lower() and pretraga2.lower() in recepcioner[parametar2].lower():
                                            print(recepcioner[0].ljust(15) + '|' + recepcioner[2].ljust(15) + '|' + recepcioner[3].ljust(15) + '|' + recepcioner[4].ljust(13) + '|' + recepcioner[5].ljust(25) + '|' + hotel[1].ljust(25) + '|')
                else:
                    print("Uneli ste iste kriterijume")
        elif x == 0:
            break
        else:
            print("Invalidan unos!")
            break
    
def obrisi_recepcionera():
    f_r = open('korisnici.txt', 'r')
    redovi = f_r.readlines()
    f_w = open('korisnici.txt', 'w')
    korisnicko_ime = input("Unesite korisnicko ime recepcionera kojeg zelite da obrisete: ")
    poklapanje = False
    for i in range(len(redovi)):
            recepcioner = red_u_recnik(redovi[i])
            if korisnicko_ime == recepcioner['korisnicko_ime'] and recepcioner['uloga'] == "recepcioner":
                poklapanje = True
                redovi.remove(redovi[i])
                break
    if poklapanje == False:
        print("Niko nije obrisan")
    elif poklapanje == True:
        print("Uspesno obrisan")
    f_w.writelines(redovi)