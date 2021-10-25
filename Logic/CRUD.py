from Domain.cheltuieli import creeaza_cheltuiala, get_numar


def adauga_cheltuiala(numar, suma, data, tip, lista):
    """
    Adauga o cheltuiala intr-o lista
    :param numar: int
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: lista de cheltuieli
    :return: O lista care contine cheltuielile
    """
    cheltuiala = creeaza_cheltuiala(numar, suma, data, tip)
    return lista + [cheltuiala]


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


def sterge_cheltuiala(numar, lista):
    """
    Sterge o cheltuiala
    :param numar: int
    :param lista: list
    :return: Lista fara cheltuiala stearsa
    """
    return [cheltuiala for cheltuiala in lista if get_numar(cheltuiala) != numar]


def modifica_cheltuiala(numar, suma, data, tip, lista):
    """
    Modifica datele unei cheltuieli
    :param numar: int
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: list
    :return: Cheltuiala cu datele modificate
    """
    lista_noua = []
    for cheltuiala in lista:
        if get_numar(cheltuiala) == numar:
            cheltuiala_noua = creeaza_cheltuiala(numar, suma, data, tip)
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)
    return lista_noua
