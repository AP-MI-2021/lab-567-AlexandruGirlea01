from Domain.cheltuieli import to_string
from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala
from Logic.functionalitati import adunare_valoare_by_data, suma_maxima_by_tip, sterge_cheltuiala_by_numar


def print_meniu():
    print("1. Adauga cheltuiala")
    print("2. Sterge cheltuiala")
    print("3. Modifica cheltuiala")
    print("4. Adaugare valoare dupa data")
    print("5. Maximul cheltuielilor dupa tip")
    print("6. Sterge toate cheltuielile pentru un apartament")
    print("a. Afisare cheltuiala")
    print("x. Iesire")


def ui_adauga_cheltuiala(lista):
    try:
        id = int(input("Introduceti ID-ul cheltuielii: "))
        numar = int(input("Introduceti numarul apartamentului: "))
        suma = float(input("Introduceti valoarea cheltuielii: "))
        data = input("Introduceti data cheltuielii in format DD.MM.YYYY: ")
        tip = input("Introduceti tipul cheltuielii(intretinere, canal, alte cheltuieli): ")
        return adauga_cheltuiala(id, numar, suma, data, tip, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_sterge_cheltuiala(lista):
    numar = int(input("Introduceti numarul apartamentului: "))
    return sterge_cheltuiala(numar, lista)


def ui_modifica_cheltuiala(lista):
    try:
        id = int(input("Introduceti ID-ul cheltuielii pe care doriti sa o modificati: "))
        numar = int(input("Introduceti noul numar al apartamentului: "))
        suma = float(input("Introduceti noua valoare a cheltuielii: "))
        data = input("Introduceti noua data a cheltuielii: ")
        tip = input("Introduceti noul tip al cheltuielii: ")
        return modifica_cheltuiala(id, numar, suma, data, tip, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_adaugare_valoare_by_data(lista):
    try:
        data = input("Introduceti data, in formatul DD.MM.YYYY: ")
        valoare = float(input("Introduceti valoarea ce va fi adaugata: "))
        return adunare_valoare_by_data(data, valoare, lista)
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


def ui_sterge_cheltuiala_by_numar(lista):
    try:
        numar = int(input("Introduceti numarul apartamentului: "))
        lista = sterge_cheltuiala_by_numar(numar, lista)
        return lista
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def afiseaza(lista):
    for cheltuiala in lista:
        print(to_string(cheltuiala))


def run_ui(lista):
    while True:
        print_meniu()
        optiune = input("Introduceti optiunea: ")
        if optiune == "1":
            lista = ui_adauga_cheltuiala(lista)
        elif optiune == "2":
            lista = ui_sterge_cheltuiala(lista)
        elif optiune == "3":
            lista = ui_modifica_cheltuiala(lista)
        elif optiune == "4":
            lista = ui_adaugare_valoare_by_data(lista)
        elif optiune == "5":
            ui_suma_maxima_by_tip(lista)
        elif optiune == "6":
            lista = ui_sterge_cheltuiala_by_numar(lista)
        elif optiune == "a":
            afiseaza(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita, incercati din nou")
