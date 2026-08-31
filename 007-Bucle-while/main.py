# ==========================================
# PYTHON DESDE CERO
# Capítulo 007 - Bucle while
# ==========================================


# EJEMPLO 1
# Contar del 1 al 5.

contador = 1

while contador <= 5:
    print(contador)
    contador += 1


# EJEMPLO 2
# Repetir hasta ingresar la opción correcta.

opcion = ""

while opcion != "salir":
    opcion = input("Escribí 'salir' para terminar: ")

print("Programa finalizado.")
