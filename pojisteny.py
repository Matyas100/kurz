from data import Data
data = Data()
class Pojisteny:
    def __init__(self, jmeno, prijmeni, tcislo, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.tcislo = tcislo
        self.vek = vek

    def pridej(self):
        data.seznam.append(self)
    def ziskej(self):
        return data.seznam
    def ziskej_podle_jmena_a_prijmeni(self, jmeno, prijmeni):
        for pojisteny in data.seznam:
            if (pojisteny.vrat_jmeno() == jmeno) and (pojisteny.vrat_prijmeni() == prijmeni):
                return pojisteny
        return False

    def vrat_jmeno(self):
        return self.jmeno
    def vrat_prijmeni(self):
        return self.prijmeni


    def __str__(self):
        return "{0} {1} {2} {3}".format(self.jmeno, self.prijmeni, self.tcislo, self.vek)