from Tests.testCrud import test_modifica_cheltuiala, test_sterge_cheltuiala, test_adauga_cheltuiala
from Tests.testDomain import test_cheltuiala
from Tests.testFunctionalitati import test_adunare_valoare_by_data, test_suma_maxima_by_tip, \
    test_sterge_cheltuiala_by_numar, test_ordonare_desc_by_suma, test_afisare_sume_lunare
from Tests.testUndoRedo import test_undo_redo


def apeleaza_toate_testele():
    test_cheltuiala()
    test_adauga_cheltuiala()
    test_sterge_cheltuiala()
    test_modifica_cheltuiala()
    test_adunare_valoare_by_data()
    test_suma_maxima_by_tip()
    test_sterge_cheltuiala_by_numar()
    test_ordonare_desc_by_suma()
    test_afisare_sume_lunare()
    test_undo_redo()
