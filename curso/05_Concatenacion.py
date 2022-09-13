# VIDEO CURSO PYTHON 7 -> https://www.youtube.com/watch?v=s5s37r2LK98&list=PL_wRgp7nihybbJ2vZaVGI5TDdPaK_dFuC&index=7

texto1 = "Hola"
texto2 = "Mundo"
textoFinal = texto1 + " " + texto2
print(textoFinal)

print("El saludo es: %s %s" % (texto1, texto2))

saludoFinal = "Saludo: {0} {1}".format(texto1, texto2) # MEDIANTE POSICIONES
print(saludoFinal)

saludoFinal = "Saludo: {} {}".format(texto1, texto2)
print(saludoFinal)

saludoFinal = "Saludo: {1} {0}".format(texto1, texto2)
print(saludoFinal)

saludoFinal = "Saludo: {x} {y}".format(x=texto1, y=texto2) # MEDIANTE ASIGNACIÓN DE VARIABLES
print(saludoFinal)

saludoFinal = "Saludo: {y} {x}".format(x=texto1, y=texto2) # MEDIANTE ASIGNACIÓN DE VARIABLES
print(saludoFinal)