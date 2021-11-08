from Domain.cheltuieli import get_suma
from Logic.CRUD import adauga_cheltuiala, get_by_numar
from Logic.functionalitati import adunare_valoare_by_data, suma_maxima_by_tip, sterge_cheltuiala_by_numar, \
    ordonare_desc_by_suma, afisare_sume_lunare


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


def test_ordonare_desc_by_suma():
    lista = []
    lista = adauga_cheltuiala(1, 25, 360, "14.05.2000", "intretinere", lista)
    lista = adauga_cheltuiala(2, 26, 400, "15.05.2002", "canal", lista)
    lista = adauga_cheltuiala(3, 28, 444, "16.05.2005", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(4, 29, 1500, "17.05.2005", "canal", lista)
    lista = adauga_cheltuiala(5, 30, 250, "18.05.2005", "intretinere", lista)
    lista = adauga_cheltuiala(6, 31, 400, "19.05.2005", "intretinere", lista)
    lista_ordonata = ordonare_desc_by_suma(lista)
    assert get_suma(lista_ordonata[0]) == 1500
    assert get_suma(lista_ordonata[1]) == 444
    assert get_suma(lista_ordonata[2]) == 400
    assert get_suma(lista_ordonata[3]) == 400
    assert get_suma(lista_ordonata[4]) == 360
    assert get_suma(lista_ordonata[5]) == 250


def test_afisare_sume_lunare():
    lista = []
    lista = adauga_cheltuiala(1, 25, 300, "15.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(2, 25, 350, "15.10.2021", "canal", lista)
    lista = adauga_cheltuiala(3, 19, 1050, "17.09.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(4, 28, 516, "10.03.2021", "canal", lista)
    lista = adauga_cheltuiala(5, 19, 529, "10.10.2021", "canal", lista)
    luna = "10"
    rezultat = afisare_sume_lunare(lista, luna)
    assert len(rezultat) == 2
    assert rezultat[25] == 650
    assert rezultat[19] == 529
