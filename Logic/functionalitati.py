from Domain.cheltuieli import get_data, creeaza_cheltuiala, get_numar, get_suma, get_tip


def adunare_valoare_by_data(data, valoare, lista):
    """
    Aduna o valoare citita la toate cheltuielile dintr-o anumita data
    :param data: string
    :param valoare: float
    :param lista: list
    :return: Lista cheltuielilor in urma procesarii
    """
    lista_noua = []
    for cheltuiala in lista:
        if get_data(cheltuiala) == data:
            cheltuiala_noua = creeaza_cheltuiala(
                get_numar(cheltuiala),
                get_suma(cheltuiala) + valoare,
                get_data(cheltuiala),
                get_tip(cheltuiala)
            )
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)
    return lista_noua
