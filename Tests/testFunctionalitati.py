from Domain.cheltuieli import get_suma
from Logic.CRUD import adauga_cheltuiala, get_by_numar
from Logic.functionalitati import adunare_valoare_by_data, suma_maxima_by_tip, sterge_cheltuiala_by_numar


def test_adunare_valoare_by_data():
    lista = []
    lista = adauga_cheltuiala(1, 1, 300, "15.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(2, 2, 350, "15.10.2021", "canal", lista)
    lista = adauga_cheltuiala(3, 3, 1050, "17.10.2021", "alte cheltuieli", lista)
    lista = adunare_valoare_by_data("15.10.2021", 120, lista)
    assert get_suma(lista[0]) == 420
    assert get_suma(lista[1]) == 470


def test_suma_maxima_by_tip():
    lista = []
    lista = adauga_cheltuiala(1, 25, 300, "15.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(2, 16, 350, "15.10.2021", "canal", lista)
    lista = adauga_cheltuiala(3, 19, 1050, "17.10.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(4, 28, 516, "10.10.2021", "canal", lista)
    rezultat = suma_maxima_by_tip(lista)
    assert rezultat[0] == 300
    assert rezultat[1] == 516
    assert rezultat[2] == 1050


def test_sterge_cheltuiala_by_numar():
    lista = []
    lista = adauga_cheltuiala(1, 25, 300, "15.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(2, 25, 350, "15.10.2021", "canal", lista)
    lista = adauga_cheltuiala(3, 19, 1050, "17.10.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(4, 28, 516, "10.10.2021", "canal", lista)
    lista = sterge_cheltuiala_by_numar(25, lista)
    assert len(lista) == 2
    assert get_by_numar(25, lista) is None
    assert get_by_numar(19, lista) is not None
