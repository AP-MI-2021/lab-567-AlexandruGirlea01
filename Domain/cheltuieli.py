def creeaza_cheltuiala(numar, suma, data, tip):
    """
    Creeaza un dictionar pentru cheltuiala
    :param numar: int
    :param suma: float
    :param data: string
    :param tip: string
    :return:
    """
    cheltuiala = (numar, suma, data, tip)
    return cheltuiala


def get_numar(cheltuiala):
    """
    Returneaza numarul apartamentuilui unei cheltuieli
    :param cheltuiala: Dictionar ce retine o cheltuiala
    :return: Numarul apartamentului cheltuielii
    """
    return cheltuiala[0]


def get_suma(cheltuiala):
    """
    Returneaza suma unei cheltuieli
    :param cheltuiala: Dictionar ce retine o cheltuiala
    :return: Suma cheltuielii
    """
    return cheltuiala[1]


def get_data(cheltuiala):
    """
    Returneaza data unei cheltuieli
    :param cheltuiala: Dictionar ce retine o cheltuiala
    :return: Data cheltuielii
    """
    return cheltuiala[2]


def get_tip(cheltuiala):
    """
    Returneaza tipul unei cheltuieli
    :param cheltuiala: Dictionar ce retine o cheltuiala
    :return: Tipul cheltuielii
    """
    return cheltuiala[3]


def to_string(cheltuiala):
    return "Numar : {}, Suma: {}, Data: {}, Tip: {}".format(
        get_numar(cheltuiala),
        get_suma(cheltuiala),
        get_data(cheltuiala),
        get_tip(cheltuiala)
    )
