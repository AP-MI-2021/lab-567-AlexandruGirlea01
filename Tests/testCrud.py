from Domain.cheltuieli import get_tip, get_data, get_suma, get_numar
from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala, get_by_numar, modifica_cheltuiala


def test_adauga_cheltuiala():
    lista = []
    lista = adauga_cheltuiala(1, 300, "15.10.2021", "intretinere", lista)
    assert get_numar(lista[0]) == 1
    assert get_suma(lista[0]) == 300
    assert get_data(lista[0]) == "15.10.2021"
    assert get_tip(lista[0]) == "intretinere"
    assert len(lista) == 1


def test_sterge_cheltuiala():
    lista = []
    lista = adauga_cheltuiala(1, 300, "15.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(2, 250, "16.10.2021", "canal", lista)
    lista = sterge_cheltuiala(1, lista)
    assert len(lista) == 1
    assert get_by_numar(1, lista) is None
    assert get_by_numar(2, lista) is not None


def test_modifica_cheltuiala():
    lista = []
    lista = adauga_cheltuiala(1, 300, "15.10.2021", "intretinere", lista)
    lista = modifica_cheltuiala(1, 250, "15.10.2021", "canal", lista)
    assert len(lista) == 1
    assert get_numar(lista[0]) == 1
    assert get_suma(lista[0]) == 250
    assert get_data(lista[0]) == "15.10.2021"
    assert get_tip(lista[0]) == "canal"
