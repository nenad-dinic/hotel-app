import datetime

def date_to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day


def kreiraj_rezervaciju(korisnicko_ime):
    today = datetime.datetime.now()
    hotel = input("U kom hotelu zelite da napravite rezervaciju: ")
    soba = input("Unesite broj sobe u kojoj zelite da rezervisete: ")
    f_h = open('hoteli.txt', 'r')
    f_s = open('sobe.txt', 'r')
    f_r = open('rezervacije.txt', 'r')
    redovi_h = f_h.readlines()
    redovi_s = f_s.readlines()
    redovi_r = f_r.readlines()
    for red in redovi_h:
        hoteli = red.strip().split(',')
        if hotel.lower() in hoteli[1].lower():
            id_hotela = hoteli[0]
    for red in redovi_s:
        sobe = red.strip().split(',')
        if soba == sobe[1] and id_hotela == sobe[0]:
            br_sobe = sobe[1]
    datumPocetka = datetime.datetime.strptime(input("Unesite datum pocetka rezervacije (YYYY-MM-DD): "), "%Y-%m-%d")
    datumKraja = datetime.datetime.strptime(input("Unesite datum kraja rezervacije (YYYY-MM-DD): "), "%Y-%m-%d")
    mogucaRezervacija = False
    if datumKraja > datumPocetka:
        mogucaRezervacija = True

    for red in redovi_r:
        rezervacije = red.strip().split(',')
        if br_sobe == rezervacije[1] and id_hotela == rezervacije[0]:
            for day in range(date_to_integer(datumPocetka), date_to_integer(datumKraja)):
                if date_to_integer(datetime.datetime.strptime(rezervacije[3], "%Y-%m-%d")) < day < date_to_integer(datetime.datetime.strptime(rezervacije[4], "%Y-%m-%d")):
                    mogucaRezervacija = False

    if mogucaRezervacija == True:
        f = open('rezervacije.txt', 'a')
        f.write(id_hotela + "," + str(br_sobe) + "," + (str(today.year) + "-" + str(today.month) + "-" + str(today.day) + " " + str(today.hour) + ":" + str(today.minute)) + "," + datumPocetka.strftime("%Y-%m-%d") + "," + datumKraja.strftime("%Y-%m-%d") + "," + korisnicko_ime + "\n")
    else:
        print("Ne mozete izvrsiti rezervaciju za ovaj datum")


def pretrazi_rezervacije(id_hotela):
    f_r = open('rezervacije.txt', 'r')
    redovi = f_r.readlines()
    today = datetime.datetime.now()
    print("1) Pretrazi po datumu i vremenu kreiranja")
    print("2) Pretrazi po datumu prijave/odjave")
    print("3) Pretrazi po korisniku koji je kreirao")
    print("4) Pretrazi po statusu rezervacije")
    kriterijum = int(input("Unesite po cemu pretrazujete: "))
    if kriterijum == 1:
        datum_kreiranja = datetime.datetime.strptime(input("Unesite datum za koji zelite da vidite kreirane rezervacije (YYYY-MM-DD): "), "%Y-%m-%d")
        print("------------------------------------------------------------------------------------------------")
        print("Id hotela|Broj sobe|Datum kreiranja|Datum prijave|Datum odjave|Rezervaciju kreirao |Status      ")
        print("------------------------------------------------------------------------------------------------")
        for red in redovi:
            rezervacija = red.strip().split(',')
            if datum_kreiranja.date() == datetime.datetime.strptime(rezervacija[2], "%Y-%m-%d %H:%M").date():
                if datetime.datetime.strptime(rezervacija[3], "%Y-%m-%d") < today < datetime.datetime.strptime(rezervacija[4], "%Y-%m-%d"):
                    print(rezervacija[0].ljust(9) + '|' + rezervacija[1].ljust(9) + '|' + rezervacija[2].ljust(15) + '|' + rezervacija[3].ljust(13) + '|' + rezervacija[4].ljust(12) + '|' + rezervacija[5].ljust(20) + '|' + "U toku")
                elif  today < datetime.datetime.strptime(rezervacija[3], "%Y-%m-%d"):
                    print(rezervacija[0].ljust(9) + '|' + rezervacija[1].ljust(9) + '|' + rezervacija[2].ljust(15) + '|' + rezervacija[3].ljust(13) + '|' + rezervacija[4].ljust(12) + '|' + rezervacija[5].ljust(20) + '|' + "Nije pocela")
                elif today > datetime.datetime.strptime(rezervacija[4], "%Y-%m-%d"):
                    print(rezervacija[0].ljust(9) + '|' + rezervacija[1].ljust(9) + '|' + rezervacija[2].ljust(15) + '|' + rezervacija[3].ljust(13) + '|' + rezervacija[4].ljust(12) + '|' + rezervacija[5].ljust(20) + '|' + "Zavrsena")
    if kriterijum == 2:
        datum_po = datetime.datetime.strptime(input("Unesite datum za koji zelite da vidite da li postoje prijave/odjave (YYYY-MM-DD): "), "%Y-%m-%d")
        print("------------------------------------------------------------------------------------------------")
        print("Id hotela|Broj sobe|Datum kreiranja|Datum prijave|Datum odjave|Rezervaciju kreirao |Status      ")
        print("------------------------------------------------------------------------------------------------")
        for red in redovi:
            rezervacija = red.strip().split(',')
            if datum_po == datetime.datetime.strptime(rezervacija[3], "%Y-%m-%d") or datum_po == datetime.datetime.strptime(rezervacija[4], "%Y-%m-%d"):
                if datetime.datetime.strptime(rezervacija[3], "%Y-%m-%d") < today < datetime.datetime.strptime(rezervacija[4], "%Y-%m-%d"):
                    print(rezervacija[0].ljust(9) + '|' + rezervacija[1].ljust(9) + '|' + rezervacija[2].ljust(15) + '|' + rezervacija[3].ljust(13) + '|' + rezervacija[4].ljust(12) + '|' + rezervacija[5].ljust(20) + '|' + "U toku")
                elif  today < datetime.datetime.strptime(rezervacija[3], "%Y-%m-%d"):
                    print(rezervacija[0].ljust(9) + '|' + rezervacija[1].ljust(9) + '|' + rezervacija[2].ljust(15) + '|' + rezervacija[3].ljust(13) + '|' + rezervacija[4].ljust(12) + '|' + rezervacija[5].ljust(20) + '|' + "Nije pocela")
                elif today > datetime.datetime.strptime(rezervacija[4], "%Y-%m-%d"):
                    print(rezervacija[0].ljust(9) + '|' + rezervacija[1].ljust(9) + '|' + rezervacija[2].ljust(15) + '|' + rezervacija[3].ljust(13) + '|' + rezervacija[4].ljust(12) + '|' + rezervacija[5].ljust(20) + '|' + "Zavrsena")
    if kriterijum == 3:
        korisnik = input("Unesite korisnicko ime za koga proveravate rezervacije: ")
        print("------------------------------------------------------------------------------------------------")
        print("Id hotela|Broj sobe|Datum kreiranja|Datum prijave|Datum odjave|Rezervaciju kreirao |Status      ")
        print("------------------------------------------------------------------------------------------------")
        for red in redovi:
            rezervacija = red.strip().split(',')
            if korisnik == rezervacija[5]:
                if datetime.datetime.strptime(rezervacija[3], "%Y-%m-%d") < today < datetime.datetime.strptime(rezervacija[4], "%Y-%m-%d"):
                    print(rezervacija[0].ljust(9) + '|' + rezervacija[1].ljust(9) + '|' + rezervacija[2].ljust(15) + '|' + rezervacija[3].ljust(13) + '|' + rezervacija[4].ljust(12) + '|' + rezervacija[5].ljust(20) + '|' + "U toku")
                elif  today < datetime.datetime.strptime(rezervacija[3], "%Y-%m-%d"):
                    print(rezervacija[0].ljust(9) + '|' + rezervacija[1].ljust(9) + '|' + rezervacija[2].ljust(15) + '|' + rezervacija[3].ljust(13) + '|' + rezervacija[4].ljust(12) + '|' + rezervacija[5].ljust(20) + '|' + "Nije pocela")
                elif today > datetime.datetime.strptime(rezervacija[4], "%Y-%m-%d"):
                    print(rezervacija[0].ljust(9) + '|' + rezervacija[1].ljust(9) + '|' + rezervacija[2].ljust(15) + '|' + rezervacija[3].ljust(13) + '|' + rezervacija[4].ljust(12) + '|' + rezervacija[5].ljust(20) + '|' + "Zavrsena")
    if kriterijum == 4:
        status = input("Unesite status koji vas interesuje ('U toku'/'Nije pocela'/'Zavrsena'):")
        print("------------------------------------------------------------------------------------------------")
        print("Id hotela|Broj sobe|Datum kreiranja|Datum prijave|Datum odjave|Rezervaciju kreirao |Status      ")
        print("------------------------------------------------------------------------------------------------")
        for red in redovi:
            rezervacija = red.strip().split(',')
            if (status.lower() == "u toku") and (datetime.datetime.strptime(rezervacija[3], "%Y-%m-%d") < today < datetime.datetime.strptime(rezervacija[4], "%Y-%m-%d")):
                print(rezervacija[0].ljust(9) + '|' + rezervacija[1].ljust(9) + '|' + rezervacija[2].ljust(15) + '|' + rezervacija[3].ljust(13) + '|' + rezervacija[4].ljust(12) + '|' + rezervacija[5].ljust(20) + '|' + "U toku")
            if (status.lower() == "nije pocela") and (today < datetime.datetime.strptime(rezervacija[3], "%Y-%m-%d")):
                print(rezervacija[0].ljust(9) + '|' + rezervacija[1].ljust(9) + '|' + rezervacija[2].ljust(15) + '|' + rezervacija[3].ljust(13) + '|' + rezervacija[4].ljust(12) + '|' + rezervacija[5].ljust(20) + '|' + "Nije pocela")
            if (status.lower() == "zavrsena") and (today > datetime.datetime.strptime(rezervacija[4], "%Y-%m-%d")):
                print(rezervacija[0].ljust(9) + '|' + rezervacija[1].ljust(9) + '|' + rezervacija[2].ljust(15) + '|' + rezervacija[3].ljust(13) + '|' + rezervacija[4].ljust(12) + '|' + rezervacija[5].ljust(20) + '|' + "Zavrsena")

def prikazi_rezervacije(korisnicko_ime):
    f_r = open('rezervacije.txt', 'r')
    redovi = f_r.readlines()
    today = datetime.datetime.now()
    print("------------------------------------------------------------------------------------------------")
    print("Id hotela|Broj sobe|Datum kreiranja|Datum prijave|Datum odjave|Rezervaciju kreirao |Status      ")
    print("------------------------------------------------------------------------------------------------")
    for red in redovi:
        rezervacija = red.strip().split(',')
        if korisnicko_ime == rezervacija[5]:
            if datetime.datetime.strptime(rezervacija[3], "%Y-%m-%d") < today < datetime.datetime.strptime(rezervacija[4], "%Y-%m-%d"):
                print(rezervacija[0].ljust(9) + '|' + rezervacija[1].ljust(9) + '|' + rezervacija[2].ljust(15) + '|' + rezervacija[3].ljust(13) + '|' + rezervacija[4].ljust(12) + '|' + rezervacija[5].ljust(20) + '|' + "U toku")
            elif  today < datetime.datetime.strptime(rezervacija[3], "%Y-%m-%d"):
                print(rezervacija[0].ljust(9) + '|' + rezervacija[1].ljust(9) + '|' + rezervacija[2].ljust(15) + '|' + rezervacija[3].ljust(13) + '|' + rezervacija[4].ljust(12) + '|' + rezervacija[5].ljust(20) + '|' + "Nije pocela")
            elif today > datetime.datetime.strptime(rezervacija[4], "%Y-%m-%d"):
                print(rezervacija[0].ljust(9) + '|' + rezervacija[1].ljust(9) + '|' + rezervacija[2].ljust(15) + '|' + rezervacija[3].ljust(13) + '|' + rezervacija[4].ljust(12) + '|' + rezervacija[5].ljust(20) + '|' + "Zavrsena")