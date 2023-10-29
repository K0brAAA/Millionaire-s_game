import json
import random


# Inicjalizacja bazy danych JSON
def inicjalizuj_baze_danych():
    produkty = {"produkty": []}
    with open("products.json", "w") as file:
        json.dump(produkty, file)


# Wczytywanie danych z bazy
def wczytaj_produkty():
    try:
        with open("products.json", "r") as file:
            dane = json.load(file)
            return dane.get("produkty", [])
    except FileNotFoundError:
        inicjalizuj_baze_danych()
        return []


# Zapisywanie danych do bazy
def zapisz_produkty(produkty):
    dane = {"produkty": produkty}
    with open("products.json", "w") as file:
        json.dump(dane, file, indent=4)


# Dodawanie produktu do bazy
def dodaj_produkt(nazwa, bialko, weglowodany, tluszcze):
    produkty = wczytaj_produkty()
    nowy_produkt = {
        "nazwa": nazwa,
        "bialko": bialko,
        "weglowodany": weglowodany,
        "tluszcze": tluszcze
    }
    produkty.append(nowy_produkt)
    zapisz_produkty(produkty)


# Usuwanie produktu z bazy
def usun_produkt(nazwa_produktu):
    produkty = wczytaj_produkty()
    nowa_lista_produktow = [produkt for produkt in produkty if produkt["nazwa"] != nazwa_produktu]
    zapisz_produkty(nowa_lista_produktow)


# Pobieranie listy produktów
def pobierz_produkty():
    return wczytaj_produkty()


# Generowanie planu diety
def generuj_plan_diety(produkty, ilosc_dni, ilosc_posilkow, zapotrzebowanie_kaloryczne):
    plan_diety = []

    for dzien in range(1, ilosc_dni + 1):
        posilki = []
        for _ in range(ilosc_posilkow):
            posilek = random.sample(produkty, 3)
            posilki.append(posilek)
        plan_diety.append({"Dzień {}".format(dzien): posilki})

    return plan_diety


if __name__ == "__main__":
    while True:
        print("1. Dodaj produkt")
        print("2. Usuń produkt")
        print("3. Wyświetl produkty")
        print("4. Generuj plan diety")
        print("5. Zakończ")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            nazwa = input("Podaj nazwę produktu: ")
            bialko = float(input("Podaj zawartość białka (w gramach): "))
            weglowodany = float(input("Podaj zawartość węglowodanów (w gramach): "))
            tluszcze = float(input("Podaj zawartość tłuszczu (w gramach): "))
            dodaj_produkt(nazwa, bialko, weglowodany, tluszcze)
            print("Produkt dodany do bazy danych.")

        elif wybor == "2":
            nazwa_produktu = input("Podaj nazwę produktu do usunięcia: ")
            usun_produkt(nazwa_produktu)
            print("Produkt usunięty z bazy danych.")

        elif wybor == "3":
            produkty = pobierz_produkty()
            if not produkty:
                print("Brak produktów w bazie danych.")
            else:
                print("Produkty w bazie danych:")
                for produkt in produkty:
                    print("Nazwa: {}, Białko: {}g, Węglowodany: {}g, Tłuszcze: {}g".format(produkt["nazwa"],
                                                                                           produkt["bialko"],
                                                                                           produkt["weglowodany"],
                                                                                           produkt["tluszcze"]))

        elif wybor == "4":
            produkty = pobierz_produkty()
            ilosc_dni = int(input("Podaj ilość dni w planie diety: "))
            ilosc_posilkow = int(input("Podaj ilość posiłków dziennie: "))
            zapotrzebowanie_kaloryczne = float(input("Podaj swoje zapotrzebowanie kaloryczne: "))
            plan_diety = generuj_plan_diety(produkty, ilosc_dni, ilosc_posilkow, zapotrzebowanie_kaloryczne)
            for i, dzien in enumerate(plan_diety, start=1):
                print("Dzień {}".format(i))
                for posilek in dzien["Dzień {}:".format(i)]:
                    print("Posiłek: ")
                    for produkt in posilek:
                        print("  - {}: Białko: {}g, Węglowodany: {}g, Tłuszcze: {}g".format(produkt["nazwa"],
                                                                                            produkt["bialko"],
                                                                                            produkt["weglowodany"],
                                                                                            produkt["tluszcze"]))

        elif wybor == "5":
            break

        else:
            print("Nieprawidłowa opcja. Wybierz ponownie.")
