from Domain.cheltuieli import to_string
from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala
from Logic.functionalitati import adunare_valoare_by_data


def print_meniu():
    print("1. Adauga cheltuiala")
    print("2. Sterge cheltuiala")
    print("3. Modifica cheltuiala")
    print("4. Adaugare valoare dupa data")
    print("a. Afisare cheltuiala")
    print("x. Iesire")


def ui_adauga_cheltuiala(lista):
    numar = int(input("Introduceti numarul apartamentului: "))
    suma = float(input("Introduceti valoarea cheltuielii: "))
    data = input("Introduceti data cheltuielii: ")
    tip = input("Introduceti tipul cheltuielii: ")
    return adauga_cheltuiala(numar, suma, data, tip, lista)


def ui_sterge_cheltuiala(lista):
    numar = int(input("Introduceti numarul apartamentului: "))
    return sterge_cheltuiala(numar, lista)


def ui_modifica_cheltuiala(lista):
    numar = int(input("Introduceti noul numar al apartamentului: "))
    suma = float(input("Introduceti noua valoare a cheltuielii: "))
    data = input("Introduceti noua data a cheltuielii: ")
    tip = input("Introduceti noul tip al cheltuielii: ")
    return modifica_cheltuiala(numar, suma, data, tip, lista)


def ui_adaugare_valoare_by_data(lista):
    data = input("Introduceti data, in formatul DD.MM.YYYY: ")
    valoare = float(input("Introduceti valoarea ce va fi adaugata: "))
    return adunare_valoare_by_data(data, valoare, lista)


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
        elif optiune == "a":
            afiseaza(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita, incercati din nou")
