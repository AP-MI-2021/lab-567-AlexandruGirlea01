from Domain.cheltuieli import get_data, creeaza_cheltuiala, get_numar, get_suma, get_tip, get_id


def adunare_valoare_by_data(data, valoare, lista):
    """
    Aduna o valoare citita la toate cheltuielile dintr-o anumita data
    :param data: string
    :param valoare: float
    :param lista: list
    :return: Lista cheltuielilor in urma procesarii
    """
    if valoare < 0:
        raise ValueError("Valoarea trebuie sa fie pozitiva")
    lista_noua = []
    for cheltuiala in lista:
        if get_data(cheltuiala) == data:
            cheltuiala_noua = creeaza_cheltuiala(
                get_id(cheltuiala),
                get_numar(cheltuiala),
                get_suma(cheltuiala) + valoare,
                get_data(cheltuiala),
                get_tip(cheltuiala)
            )
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)
    return lista_noua


def suma_maxima_by_tip(lista):
    """
    Determina cea mai mare cheltuiala pentru fiecare tip
    :param lista: list
    :return: O lista ce contine maximul pentru fiecare tip de cheltuiala
    """
    maxim_intretinere = 0
    maxim_canal = 0
    maxim_altele = 0
    for cheltuiala in lista:
        if get_tip(cheltuiala) == "intretinere" and get_suma(cheltuiala) > maxim_intretinere:
            maxim_intretinere = get_suma(cheltuiala)
        elif get_tip(cheltuiala) == "canal" and get_suma(cheltuiala) > maxim_canal:
            maxim_canal = get_suma(cheltuiala)
        elif get_tip(cheltuiala) == "alte cheltuieli" and get_suma(cheltuiala) > maxim_altele:
            maxim_altele = get_suma(cheltuiala)
    rezultat = [maxim_intretinere, maxim_canal, maxim_altele]
    return rezultat


def sterge_cheltuiala_by_numar(numar, lista):
    """
    Sterge toate cheltuielile pentru un apartament dat
    :param numar: int
    :param lista: list
    :return: Lista de cheltuieli ramase in urma stergerii
    """
    return [cheltuiala for cheltuiala in lista if get_numar(cheltuiala) != numar]
