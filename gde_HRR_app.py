from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    @abstractmethod
    def leiras(self):
        pass

class EgyagyasSzoba(Szoba):
    def leiras(self):
        return f"Egyágyas szoba, ár: {self.ar} Ft"

class KetagyasSzoba(Szoba):
    def leiras(self):
        return f"Kétagyas szoba, ár: {self.ar} Ft"

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def szoba_hozzaad(self, szoba):
        self.szobak.append(szoba)

    def __str__(self):
        return f"Szálloda neve: {self.nev}, szobák száma: {len(self.szobak)}"

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def __str__(self):
        return f"Foglalás: {self.szoba.leiras()}, Szobaszám: {self.szoba.szobaszam}, dátum: {self.datum.strftime('%Y-%m-%d')}"

#Foglalások kezelése
class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = []

    def szoba_foglal(self, szobaszam, datum):
        if datum < datetime.now():
            return "A választott dátum a múltban van."
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                return "Ez a szoba ezen a napon már foglalt."
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                uj_foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(uj_foglalas)
                return f"Foglalás rögzítve: {uj_foglalas}"
        return "Nem található ilyen szobaszám."

    def foglalas_lemond(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return "Foglalás lemondva."
        return "Nincs ilyen foglalás."

    def foglalasok_listaja(self):
        if not self.foglalasok:
            return "Nincsenek foglalások."
        return "\n".join(str(foglalas) for foglalas in self.foglalasok)

#GDH feltöltése a szobák adataival szobaszám, ár/nap
szalloda = Szalloda("Gábor Dénes Hotel")
szalloda.szoba_hozzaad(EgyagyasSzoba(101, 18000))
szalloda.szoba_hozzaad(EgyagyasSzoba(102, 18000))
szalloda.szoba_hozzaad(EgyagyasSzoba(103, 18000))
szalloda.szoba_hozzaad(EgyagyasSzoba(104, 18000))
szalloda.szoba_hozzaad(EgyagyasSzoba(105, 18000))
szalloda.szoba_hozzaad(EgyagyasSzoba(106, 18000))
szalloda.szoba_hozzaad(EgyagyasSzoba(107, 18000))
szalloda.szoba_hozzaad(EgyagyasSzoba(108, 18000))
szalloda.szoba_hozzaad(EgyagyasSzoba(109, 18000))
szalloda.szoba_hozzaad(EgyagyasSzoba(110, 18000))
szalloda.szoba_hozzaad(KetagyasSzoba(111, 20000))
szalloda.szoba_hozzaad(KetagyasSzoba(112, 20000))
szalloda.szoba_hozzaad(KetagyasSzoba(113, 20000))
szalloda.szoba_hozzaad(KetagyasSzoba(114, 20000))
szalloda.szoba_hozzaad(KetagyasSzoba(115, 20000))
szalloda.szoba_hozzaad(KetagyasSzoba(116, 20000))
szalloda.szoba_hozzaad(KetagyasSzoba(117, 20000))


kezelo = FoglalasKezelo(szalloda)

for i in range(5):
    kezelo.szoba_foglal(101 + i % 3, datetime.now() + timedelta(days=i + 1))

print(kezelo.szoba_foglal(101, datetime.now() + timedelta(days=1)))  # Foglalás létrehozása
print(kezelo.foglalas_lemond(101, datetime.now() + timedelta(days=1)))  # Foglalás lemondása
print(kezelo.foglalasok_listaja())  # Foglalások listázása

#Felhasználói interfész létrehozása
def UI():
    while True:
        print("\nVálassza ki a kívánt műveletet:")
        print("1. Szoba foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        
        valasztas = input("Adja meg a választott művelet számát: ")
        
        if valasztas == '1':
            szobaszam = int(input("Adja meg a szoba számát: "))
            ev = int(input("Adja meg az évet: "))
            honap = int(input("Adja meg a hónapot: "))
            nap = int(input("Adja meg a napot: "))
            datum = datetime(ev, honap, nap)
            print(kezelo.szoba_foglal(szobaszam, datum))
        elif valasztas == '2':
            szobaszam = int(input("Adja meg a szoba számát, amelyik foglalást le szeretné mondani: "))
            ev = int(input("Adja meg a lemondani kívánt foglalás évét: "))
            honap = int(input("Adja meg a hónapot: "))
            nap = int(input("Adja meg a napot: "))
            datum = datetime(ev, honap, nap)
            print(kezelo.foglalas_lemond(szobaszam, datum))
        elif valasztas == '3':
            print("Foglalások listája:")
            print(kezelo.foglalasok_listaja())
        elif valasztas == '4':
            print("Kilépés a programból.")
            break
        else:
            print("Érvénytelen választás. Kérjük, próbálja újra.")

# Felhasználói interfész indítása
UI()
