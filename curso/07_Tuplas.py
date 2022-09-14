# https://www.youtube.com/watch?v=f8E1A0wo7qg&list=PL_wRgp7nihybbJ2vZaVGI5TDdPaK_dFuC&index=9

"""
Tupla: Es una estructura de datos propia de Python que permite almacenar distintos valores,
son inmutables: no cambian una vez inicializadas.
"""

tupla = (1, 2, 3)
print(tupla)

tupla2 = (7, "carlos".title(), True, 450.1, 16 + 7j, 15, "Felicidad", False)
print(tupla2)

tupla3 = (9, 3, (4, 5, 6))
print(tupla3)

print(tupla2[1])
# tupla2[1] = "nada"
print(tupla2[-1]) # Acceder al último elemento.

print(tupla2[0:4])
print(tupla2[-2])

a, b, c = tupla
# a, b, c, d = tupla
print(a)
print(b)
print(c)
# print(d)

tuplaFinal = tupla + tupla3
print(tuplaFinal)

print(tuplaFinal.count(3))
print(tuplaFinal.index(3)) # Regresa el número donde aparece el argumento
