# ==========================================
# PYTHON DESDE CERO
# Capítulo 006 - Condicional elif y else
# ==========================================


# Solicitamos los datos.
print("Escribí tu nombre:")
nombre = input()

print("Ingresá tu nota:")
nota = int(input())


# Evaluamos la nota.
if nota >= 9:
    print(f"Excelente, {nombre}.")

elif nota >= 6:
    print(f"Aprobaste, {nombre}.")

else:
    print(f"Desaprobaste, {nombre}.")
