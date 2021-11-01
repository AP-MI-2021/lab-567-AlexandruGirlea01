from Domain.cheltuieli import get_id, to_string
from Logic.CRUD import adauga_cheltuiala, get_by_id


def print_help():
    print("Comenzi implementate: ")
    print("1. Adaugare cheltuiala in lista: add,id,numar_ap,suma,data,tip")
    print("2. Stergere cheltuiala din lista: delete,id")
    print("3. Afisare toate cheltuielile: showall")
    print("4. Iesire")
    print("Pentru a apela o functionalitate introduceti numele functiei si parametrii separati prin virgula.")
    print("Pentru a apela mai multe functii introduceti numele acestora separate prin ;")


def adaugare(lista, parametrii):
    id = int(parametrii[1])
    numar = int(parametrii[2])
    suma = float(parametrii[3])
    data = parametrii[4]
    tip = parametrii[5]
    lista = adauga_cheltuiala(id, numar, suma, data, tip, lista)
    return lista


def stergere(lista, parametrii):
    id = int(parametrii[1])
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista cheltuiala cu ID-ul dat!")
    return [cheltuiala for cheltuiala in lista if get_id(cheltuiala) != id]


def afisare(lista):
    for cheltuiala in lista:
        print(to_string(cheltuiala))


def run_console(lista):
    run = True
    while run:
        optiuni = input("Introduceti optiunile: ")
        functionalitati = optiuni.split(";")
        for functie in functionalitati:
            parametrii = functie.split(",")
            if parametrii[0] == "help":
                print_help()
            elif parametrii[0] == "add":
                lista = adaugare(lista, parametrii)
            elif parametrii[0] == "delete":
                lista = stergere(lista, parametrii)
            elif parametrii[0] == "showall":
                print("Lista de cheltuieli este: ")
                afisare(lista)
            elif parametrii[0] == "exit":
                run = False
