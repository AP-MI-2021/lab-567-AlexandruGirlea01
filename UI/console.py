from Domain.cheltuieli import to_string
from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala
from Logic.functionalitati import adunare_valoare_by_data, suma_maxima_by_tip, sterge_cheltuiala_by_numar, \
    ordonare_desc_by_suma, afisare_sume_lunare


def print_meniu():
    print("1. Adauga cheltuiala")
    print("2. Sterge cheltuiala")
    print("3. Modifica cheltuiala")
    print("4. Adaugare valoare dupa data")
    print("5. Maximul cheltuielilor dupa tip")
    print("6. Sterge toate cheltuielile pentru un apartament")
    print("7. Ordoneaza descrescator dupa suma")
    print("8. Afisare sume lunare pentru fiecare apartament")
    print("a. Afisare cheltuiala")
    print("u. Undo")
    print("r. Redo")
    print("x. Iesire")


def ui_adauga_cheltuiala(lista, undo_list, redo_list):
    try:
        id = int(input("Introduceti ID-ul cheltuielii: "))
        numar = int(input("Introduceti numarul apartamentului: "))
        suma = float(input("Introduceti valoarea cheltuielii: "))
        data = input("Introduceti data cheltuielii in format DD.MM.YYYY: ")
        tip = input("Introduceti tipul cheltuielii(intretinere, canal, alte cheltuieli): ")
        rezultat = adauga_cheltuiala(id, numar, suma, data, tip, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_sterge_cheltuiala(lista, undo_list, redo_list):
    try:
        id = int(input("Introduceti id-ul apartamentului: "))
        rezultat = sterge_cheltuiala(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modifica_cheltuiala(lista, undo_list, redo_list):
    try:
        id = int(input("Introduceti ID-ul cheltuielii pe care doriti sa o modificati: "))
        numar = int(input("Introduceti noul numar al apartamentului: "))
        suma = float(input("Introduceti noua valoare a cheltuielii: "))
        data = input("Introduceti noua data a cheltuielii: ")
        tip = input("Introduceti noul tip al cheltuielii: ")
        rezultat = modifica_cheltuiala(id, numar, suma, data, tip, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_adaugare_valoare_by_data(lista, undo_list, redo_list):
    try:
        data = input("Introduceti data, in formatul DD.MM.YYYY: ")
        valoare = float(input("Introduceti valoarea ce va fi adaugata: "))
        rezultat = adunare_valoare_by_data(data, valoare, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_suma_maxima_by_tip(lista):
    rezultat = suma_maxima_by_tip(lista)
    if rezultat[0] != 0:
        print("Maximul cheltuielilor pentru intretinere este de " + str(rezultat[0]) + " lei")
    else:
        print("Nu exista cheltuiala de tip intretinere")
    if rezultat[1] != 0:
        print("Maximul cheltuielilor pentru canalizare este de " + str(rezultat[1]) + " lei")
    else:
        print("Nu exista cheltuiala de tip canal")
    if rezultat[2] != 0:
        print("Maximul altor cheltuieli este de " + str(rezultat[2]) + " lei")
    else:
        print("Nu exista cheltuiala de tip alte cheltuieli")


def ui_sterge_cheltuiala_by_numar(lista, undo_list, redo_list):
    try:
        numar = int(input("Introduceti numarul apartamentului: "))
        rezultat = sterge_cheltuiala_by_numar(numar, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_ordonare_desc_by_suma(lista):
    rezultat = ordonare_desc_by_suma(lista)
    print("Lista ordonata descrescator dupa sume este: ")
    afiseaza(rezultat)


def afiseaza(lista):
    if not lista:
        print("Lista este goala!")
    else:
        for cheltuiala in lista:
            print(to_string(cheltuiala))


def ui_afisare_sume_lunare(lista):
    luna = input("Introduceti luna: ")
    rezultat = afisare_sume_lunare(lista, luna)
    print("In luna a " + luna + "-a cheltuielile au fost: ")
    print(rezultat)


def run_ui(lista):
    undo_list = []
    redo_list = []
    while True:
        print_meniu()
        optiune = input("Introduceti optiunea: ")
        if optiune == "1":
            lista = ui_adauga_cheltuiala(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = ui_sterge_cheltuiala(lista, undo_list, redo_list)
        elif optiune == "3":
            lista = ui_modifica_cheltuiala(lista, undo_list, redo_list)
        elif optiune == "4":
            lista = ui_adaugare_valoare_by_data(lista, undo_list, redo_list)
        elif optiune == "5":
            ui_suma_maxima_by_tip(lista)
        elif optiune == "6":
            lista = ui_sterge_cheltuiala_by_numar(lista, undo_list, redo_list)
        elif optiune == "7":
            ui_ordonare_desc_by_suma(lista)
        elif optiune == "8":
            ui_afisare_sume_lunare(lista)
        elif optiune == "a":
            afiseaza(lista)
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "x":
            break
        else:
            print("Optiune gresita, incercati din nou")
