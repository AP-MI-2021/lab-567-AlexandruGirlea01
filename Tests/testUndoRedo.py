from Domain.cheltuieli import get_id
from Logic.CRUD import adauga_cheltuiala


def test_undo_redo():
    lista = []
    undo_list = []
    redo_list = []

    undo_list.append(lista)
    redo_list.clear()

    lista = adauga_cheltuiala(1, 10, 300, "10.12.2000", "canal", lista)
    undo_list.append(lista)
    redo_list.clear()

    assert get_id(lista[0]) == 1
    assert len(lista) == 1

    lista = adauga_cheltuiala(2, 11, 312.15, "01.02.2001", "intretinere", lista)
    undo_list.append(lista)
    redo_list.clear()

    assert get_id(lista[0]) == 1
    assert get_id(lista[1]) == 2
    assert len(lista) == 2

    lista = adauga_cheltuiala(3, 12, 700, "10.02.2001", "alte cheltuieli", lista)

    assert get_id(lista[0]) == 1
    assert get_id(lista[1]) == 2
    assert get_id(lista[2]) == 3
    assert len(lista) == 3

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()

    assert get_id(lista[0]) == 1
    assert get_id(lista[1]) == 2
    assert len(lista) == 2

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()

    assert get_id(lista[0]) == 1
    assert len(lista) == 1

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()

    assert len(lista) == 0

    undo_list.append(lista)
    redo_list.clear()

    assert len(lista) == 0

    lista = adauga_cheltuiala(1, 13, 300, "10.12.2000", "canal", lista)
    undo_list.append(lista)
    redo_list.clear()

    lista = adauga_cheltuiala(2, 14, 605, "01.03.2020", "intretinere", lista)
    undo_list.append(lista)
    redo_list.clear()

    lista = adauga_cheltuiala(3, 15, 444, "14.05.2012", "intretinere", lista)

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()

    assert get_id(lista[0]) == 1
    assert get_id(lista[1]) == 2
    assert get_id(lista[2]) == 3
    assert len(lista) == 3

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()

    assert get_id(lista[0]) == 1
    assert get_id(lista[1]) == 2
    assert len(lista) == 2

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()

    assert get_id(lista[0]) == 1
    assert len(lista) == 1

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()

    assert get_id(lista[0]) == 1
    assert get_id(lista[1]) == 2
    assert len(lista) == 2

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()

    assert get_id(lista[0]) == 1
    assert get_id(lista[1]) == 2
    assert get_id(lista[2]) == 3
    assert len(lista) == 3

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()

    assert get_id(lista[0]) == 1
    assert get_id(lista[1]) == 2
    assert len(lista) == 2

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()

    assert get_id(lista[0]) == 1
    assert len(lista) == 1

    undo_list.append(lista)
    redo_list.clear()

    lista = adauga_cheltuiala(4, 16, 546, "10.12.2000", "alte cheltuieli", lista)

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()

    assert get_id(lista[0]) == 1
    assert get_id(lista[1]) == 4
    assert len(lista) == 2

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()

    assert get_id(lista[0]) == 1
    assert len(lista) == 1

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()

    assert len(lista) == 0

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()

    assert get_id(lista[0]) == 1
    assert len(lista) == 1

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()

    assert get_id(lista[0]) == 1
    assert get_id(lista[1]) == 4
    assert len(lista) == 2

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()

    assert get_id(lista[0]) == 1
    assert get_id(lista[1]) == 4
    assert len(lista) == 2
