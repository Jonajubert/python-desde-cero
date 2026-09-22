# ==========================================
# PYTHON DESDE CERO
# Capítulo 010 - Listas
# ==========================================


# Creamos una lista.
frutas = ["Manzana", "Banana", "Naranja"]

print("Lista original:")
print(frutas)


# Accedemos a elementos mediante su índice.
print("\nPrimer elemento:")
print(frutas[0])

print("\nSegundo elemento:")
print(frutas[1])


# Agregamos un elemento.
frutas.append("Pera")

print("\nDespués de agregar Pera:")
print(frutas)


# Modificamos un elemento.
frutas[1] = "Frutilla"

print("\nDespués de modificar:")
print(frutas)


# Eliminamos un elemento.
frutas.remove("Naranja")

print("\nDespués de eliminar Naranja:")
print(frutas)


# Cantidad de elementos.
print("\nCantidad de frutas:")
print(len(frutas))
