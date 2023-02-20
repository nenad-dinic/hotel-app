import hotel
import recepcioner
import sobe
import rezervacije
def menu():
    print("Glavni meni")
    print("1) Registracija")
    print("2) Prijava")
    print("3) Izlaz")

def glavni_meni():
    while True:
        menu()
        odabir = input(">")
        if odabir == "1":
            registracija()
        elif odabir == "2":
            prijava()
        elif odabir == "3":
            break
        else:
            print("Invalidan odabir")

def registracija():
    f = open('korisnici.txt', 'a')
    while True:
        korisnicko_ime = input("Unesite korisnicko ime: ")
        lozinka = input("Unesite lozinku: ")
        ponovljena_lozinka = input("Ponovite lozinku: ")
        ime = input("Unesite ime: ")
        prezime = input("Unesite prezime: ")
        kontakt_telefon = input("Unesite kontakt telefon: ")
        email = input("Unesite email: ")
        if lozinka != ponovljena_lozinka:
            print("Lozinke se ne podudaraju")
            break
        else:
            f.write(korisnicko_ime + "," + lozinka + "," + ime + "," + prezime + "," + kontakt_telefon + "," + email + "," + "korisnik" + "," + "0\n")
            print("----------------------------")
            print("Uspesno ste se registrovali.")
            print("----------------------------")
            break
    
def prijava():
    while True:
        korisnicko_ime = input("Unesite korisnicko ime: ")
        lozinka = input("Unesite lozinku: ")
        f = open('korisnici.txt', 'r')
        data = f.readlines()
        for red in data:
            korisnici = red.strip().split(',')
            if korisnicko_ime == korisnici[0] and lozinka == korisnici[1]:
                print("------------------------")
                print("Uspesno ste se ulogovali")
                print("------------------------")
                if korisnici[6] == 'korisnik':
                    meni_korisnika(korisnicko_ime)
                    return False
                elif korisnici[6] == 'recepcioner':
                    id_hotela = korisnici[7]
                    meni_recepcionera(id_hotela)
                    return False
                elif korisnici[6] == "administrator":
                    meni_administratora()
                    return False
                else:
                    print("Nepoznata uloga")
                    return False
        print("--------------------------")
        print("Uneli ste pogresne podatke")
        print("--------------------------")
        return False

def meni_korisnika(korisnicko_ime):
    while True:
        print("Ulogovani ste kao korisnik")
        print("1) Prikazi hotele")
        print("2) Pretrazi hotele")
        print("3) Najbolji hoteli")
        print("4) Kreiraj rezervaciju")
        print("5) Prikazi rezervacije")
        print("6) Ocenite hotel")
        print("7) Odjavi se")
        opcija = input(">")
        if opcija == "1":
            hotel.prikaz_hotela()
        elif opcija == "2":
            hotel.pretrazi_hotele()
        elif opcija == "3":
            hotel.najbolji_hoteli()
        elif opcija == "4":
            rezervacije.kreiraj_rezervaciju(korisnicko_ime)
        elif opcija == "5":
            rezervacije.prikazi_rezervacije(korisnicko_ime)
            print("")
        elif opcija == "6":
            hotel.oceni_hotel(korisnicko_ime)
            print("")
        elif opcija == "7":
            break
        
def meni_recepcionera(id_hotela):
    while True:
        print("Ulogovani ste kao recepcioner")
        print("1) Pretrazi sobe")
        print("2) Pretrazi rezervacije")
        print("3) Izvestaj")
        print("4) Odjavi se")
        opcija = input(">")
        if opcija == "1":
            sobe.pretrazi_sobe(id_hotela)
        elif opcija == "2":
            rezervacije.pretrazi_rezervacije(id_hotela)
            print("")
        elif opcija == "3":
            #izvestaj(id_hotela)
            print("")
        elif opcija == "4":
            break

def meni_administratora():
    while True:
        print("Ulogovani ste kao administrator")
        print("1) Dodaj novi hotel")
        print("2) Dodaj novog recepcionera")
        print("3) Azuriraj hotel")
        print("4) Obrisi hotel")
        print("5) Obrisi recepcionera")
        print("6) Pretrazi recepcionere")
        print("7) Odjavi se")
        opcija = input(">")
        if opcija == "1":
            hotel.dodaj_hotel()
        elif opcija == "2":
            recepcioner.dodaj_recepcionera()
        elif opcija == "3":
            hotel.azuriraj_hotel()
        elif opcija == "4":
            hotel.obrisi_hotel()
        elif opcija == "5":
            recepcioner.obrisi_recepcionera()
        elif opcija == "6":
            recepcioner.pretrazi_recepcionere()
        elif opcija == "7":
            break

glavni_meni()