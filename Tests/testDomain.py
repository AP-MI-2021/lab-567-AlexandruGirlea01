from Domain.cheltuieli import creeaza_cheltuiala, get_numar, get_suma, get_data, get_tip, get_id


def test_cheltuiala():
    cheltuiala = creeaza_cheltuiala(1, 1, 300, "15.10.2021", "intretinere")
    assert get_id(cheltuiala) == 1
    assert get_numar(cheltuiala) == 1
    assert get_suma(cheltuiala) == 300
    assert get_data(cheltuiala) == "15.10.2021"
    assert get_tip(cheltuiala) == "intretinere"
