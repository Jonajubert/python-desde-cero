# ==========================================
# PYTHON DESDE CERO
# Capítulo 012 - Diccionarios
# ==========================================


# Creamos un diccionario con pares clave: valor.
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Eldorado"
}


# Accedemos mediante las claves.
print("Datos iniciales:")

print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])


# len() indica la cantidad de pares clave-valor.
print("\nCantidad:")
print(len(persona))


# Una clave existente permite modificar su valor.
persona["edad"] = 26


# Una clave nueva permite agregar un dato.
persona["lenguaje"] = "Python"


# get() permite definir qué devolver si la clave no existe.
print("\nConsulta con get():")
print(persona.get("telefono", "No registrado"))


# in comprueba si existe una clave.
if "nombre" in persona:
    print("\nLa clave nombre existe.")


# Eliminamos un par mediante su clave.
del persona["ciudad"]


# items() permite recorrer las claves junto con sus valores.
print("\nDatos actualizados:")

for clave, valor in persona.items():
    print(f"{clave}: {valor}")


print("\nCantidad final:")
print(len(persona))
