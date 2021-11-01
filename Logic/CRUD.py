from Domain.cheltuieli import creeaza_cheltuiala, get_numar, get_id


def adauga_cheltuiala(id, numar, suma, data, tip, lista):
    """
    Adauga o cheltuiala intr-o lista
    :param id: int
    :param numar: int
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: lista de cheltuieli
    :return: O lista care contine cheltuielile
    """
    if get_by_id(id, lista) is not None:
        raise ValueError("ID-ul exista deja!")
    cheltuiala = creeaza_cheltuiala(id, numar, suma, data, tip)
    return lista + [cheltuiala]


def get_by_id(id, lista):
    """
    Returneaza cheltuiala din lista cu id-ul dat
    :param id: int
    :param lista: list
    :return: Cheltuiala cu id-ul dat sau None in cazul in care nu exista
    """
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            return cheltuiala
    return None


def get_by_numar(numar, lista):
    """
    Returneaza cheltuiala din lista cu numarul dat
    :param numar: int
    :param lista: list
    :return: Cheltuiala cu numarul dat sau None in cazul in care nu exista
    """
    for cheltuiala in lista:
        if get_numar(cheltuiala) == numar:
            return cheltuiala
    return None


def sterge_cheltuiala(id, lista):
    """
    Sterge o cheltuiala
    :param id: int
    :param lista: list
    :return: Lista fara cheltuiala stearsa
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista cheltuiala cu ID-ul dat!")
    return [cheltuiala for cheltuiala in lista if get_id(cheltuiala) != id]


def modifica_cheltuiala(id, numar, suma, data, tip, lista):
    """
    Modifica datele unei cheltuieli
    :param id: int
    :param numar: int
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: list
    :return: Cheltuiala cu datele modificate
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista cheltuiala cu ID-ul dat!")
    lista_noua = []
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            cheltuiala_noua = creeaza_cheltuiala(id, numar, suma, data, tip)
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)
    return lista_noua
