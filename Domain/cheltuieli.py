def creeaza_cheltuiala(id, numar, suma, data, tip):
    """
    Creeaza un dictionar pentru cheltuiala
    :param id: int
    :param numar: int
    :param suma: float
    :param data: string
    :param tip: string
    :return:
    """
    return {
        "id": id,
        "numar": numar,
        "suma": suma,
        "data": data,
        "tip": tip
    }


def get_id(cheltuiala):
    """
    Returneaza id-ul unei cheltuieli
    :param cheltuiala: Dictionar ce retine o cheltuiala
    :return: ID-ul cheltuielii
    """
    return cheltuiala["id"]


def get_numar(cheltuiala):
    """
    Returneaza numarul apartamentuilui unei cheltuieli
    :param cheltuiala: Dictionar ce retine o cheltuiala
    :return: Numarul apartamentului cheltuielii
    """
    return cheltuiala["numar"]


def get_suma(cheltuiala):
    """
    Returneaza suma unei cheltuieli
    :param cheltuiala: Dictionar ce retine o cheltuiala
    :return: Suma cheltuielii
    """
    return cheltuiala["suma"]


def get_data(cheltuiala):
    """
    Returneaza data unei cheltuieli
    :param cheltuiala: Dictionar ce retine o cheltuiala
    :return: Data cheltuielii
    """
    return cheltuiala["data"]


def get_tip(cheltuiala):
    """
    Returneaza tipul unei cheltuieli
    :param cheltuiala: Dictionar ce retine o cheltuiala
    :return: Tipul cheltuielii
    """
    return cheltuiala["tip"]


def to_string(cheltuiala):
    return "ID : {}, Numar : {}, Suma: {}, Data: {}, Tip: {}".format(
        get_id(cheltuiala),
        get_numar(cheltuiala),
        get_suma(cheltuiala),
        get_data(cheltuiala),
        get_tip(cheltuiala)
    )
