# ==========================================
# PYTHON DESDE CERO
# Capítulo 011 - Tuplas
# ==========================================


# Creamos una tupla.
colores = ("Rojo", "Verde", "Azul")

print("Tupla:")
print(colores)


# Accedemos mediante índices.
print("\nElementos:")

print(colores[0])
print(colores[1])
print(colores[2])


# Cantidad de elementos.
print("\nCantidad:")
print(len(colores))


# También podemos recorrerla.
print("\nRecorriendo la tupla:")

for color in colores:
    print(color)


# Una tupla puede contener distintos tipos.
datos = ("Jonatan", 38, True)

print("\nDatos:")
print(datos)
