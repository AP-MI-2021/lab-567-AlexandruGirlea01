from Domain.cheltuieli import get_suma
from Logic.CRUD import adauga_cheltuiala
from Logic.functionalitati import adunare_valoare_by_data


def test_adunare_valoare_by_data():
    lista = []
    lista = adauga_cheltuiala(1, 300, "15.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(2, 350, "15.10.2021", "canal", lista)
    lista = adauga_cheltuiala(3, 1050, "17.10.2021", "alte cheltuieli", lista)
    lista = adunare_valoare_by_data("15.10.2021", 120, lista)
    assert get_suma(lista[0]) == 420
    assert get_suma(lista[1]) == 470

