# VIDEO CURSO PYTHON 8 -> https://www.youtube.com/watch?v=S8lXefbGXRQ&list=PL_wRgp7nihybbJ2vZaVGI5TDdPaK_dFuC&index=8

texto = "Bienvenidos al curso de Python"

print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title())

print(texto.find("al")) # Posición donde encuentra la cadena
print(texto.count("e")) # Cuenta el número de veces que aparece la cadena

textoFinal = texto.replace("e", "3")
print(textoFinal)

valor = texto.isnumeric()
print(valor)

cadenaSeparada = texto.split(" ")
print(cadenaSeparada)