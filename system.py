import os
class System:
    def vypis_moznosti(self, nazev):
        print("-" * 24)
        print(nazev)
        print("-" * 24 + "\n")
        print("Vyberte si akci:")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")

    def data(self):
        input("Data byla uložena. Pokračuj libovolnou klávesou.\n")
        os.system("cls")
    def pokracuj(self):
        input("Pokračuj libovolnou klávesou.\n")
        os.system("cls")