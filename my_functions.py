import time
import os

def osszegzes(szamokat_tartalmazo_lista):
    '''ez a fg. visszatér a paraméterben kapott lista elemeinek összegével'''
    sum = 0
    for e in szamokat_tartalmazo_lista:
        sum += e
    return sum


def paros_elemek_szama(szamokat_tartalmazo_lista):
    '''ez a fg. vissziatér a paraméterben kapott lista páros elemeinek számával'''
    count = 0
    for e in szamokat_tartalmazo_lista:
        if e % 2 == 0:
            count += 1
    return count


def minimum_index(szamokat_tartalmazo_lista):
    '''ez a fg. visszatér a paraméterben kapott lista legkisebb elemének indexével'''
    minimum_index = 0
    for i in range(1, len(szamokat_tartalmazo_lista)):
        if szamokat_tartalmazo_lista[i] < szamokat_tartalmazo_lista[minimum_index]:
            minimum_index = i
    return minimum_index


def linearis_kereses(lista_amiben_keresek, keresett_elem):
    i = 0
    while i < len(lista_amiben_keresek) and lista_amiben_keresek[i] != keresett_elem:
        i += 1
    if i < len(lista_amiben_keresek): return i
    else: return -1


def exit():
    res = input('valóban ki akarsz lépni? (y / n): ')
    if res == 'y' or res == 'Y':
        for n in range(3):
            print(f'{n + 1}...')
            time.sleep(0.5)
        print('viszont látásra!')
        time.sleep(1)
        os.system('cls')