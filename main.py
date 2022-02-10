import my_functions as f

lista = [11, 26, 7]

elemek_osszege = f.osszegzes(lista)
print(f'az elemek összege a listában: {elemek_osszege}')

paros = f.paros_elemek_szama(lista)
print(f'a páros elemek száma a listában: {paros}')

minimum_i = f.minimum_index(lista)

print(f'legkisebb elem indexe: {minimum_i}')
print(f'legkisebb elem: {lista[minimum_i]}')
print(f'legkisebb elem a lista {minimum_i + 1}. eleme')

keresett = int(input('melyik számot keresed? '))
index = f.linearis_kereses(lista, keresett)

if index == -1: print('nincs benne :(')
else: print(f'a keresett szám a lista {index}-es indexű ele')

f.exit()