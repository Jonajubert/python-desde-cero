# Python Desde Cero

## Capítulo 010 - Listas

Una lista permite almacenar varios elementos dentro de una misma variable.

Por ejemplo:

```python
frutas = ["Manzana", "Banana", "Naranja"]
```

En lugar de crear:

```python
fruta1 = "Manzana"
fruta2 = "Banana"
fruta3 = "Naranja"
```

podemos agrupar los valores dentro de una colección.

---

## ¿Qué aprenderás?

En este capítulo veremos:

- Cómo crear listas.
- Cómo acceder a sus elementos.
- Cómo modificar valores.
- Cómo agregar elementos.
- Cómo eliminar elementos.
- Cómo conocer la cantidad de elementos.
- Cómo utilizar índices negativos.
- Qué tipos de datos puede contener una lista.

---

# Crear una lista

Las listas se crean utilizando corchetes:

```python
frutas = ["Manzana", "Banana", "Naranja"]
```

Los elementos se separan mediante comas.

Podemos mostrar la lista:

```python
print(frutas)
```

Resultado:

```text
['Manzana', 'Banana', 'Naranja']
```

---

# Índices

Cada elemento posee una posición.

Python comienza a contar desde `0`.

```text
Índice       Elemento

0            Manzana
1            Banana
2            Naranja
```

Entonces:

```python
print(frutas[0])
```

devuelve:

```text
Manzana
```

Mientras que:

```python
print(frutas[2])
```

devuelve:

```text
Naranja
```

---

# Modificar elementos

Las listas son mutables.

Esto significa que podemos modificar sus elementos.

```python
frutas = ["Manzana", "Banana", "Naranja"]

frutas[1] = "Frutilla"

print(frutas)
```

Resultado:

```text
['Manzana', 'Frutilla', 'Naranja']
```

A diferencia de las cadenas de texto que vimos en el capítulo anterior, una lista puede modificarse directamente.

---

# Agregar elementos

Podemos agregar un elemento al final utilizando:

```python
append()
```

Ejemplo:

```python
frutas = ["Manzana", "Banana"]

frutas.append("Naranja")

print(frutas)
```

Resultado:

```text
['Manzana', 'Banana', 'Naranja']
```

---

# Insertar en una posición

También podemos utilizar:

```python
insert()
```

Por ejemplo:

```python
frutas = ["Manzana", "Naranja"]

frutas.insert(1, "Banana")

print(frutas)
```

Resultado:

```text
['Manzana', 'Banana', 'Naranja']
```

En:

```python
insert(1, "Banana")
```

el `1` indica la posición donde queremos insertar el elemento.

---

# Eliminar elementos

Podemos eliminar un elemento por su valor utilizando:

```python
remove()
```

Ejemplo:

```python
frutas = ["Manzana", "Banana", "Naranja"]

frutas.remove("Banana")

print(frutas)
```

Resultado:

```text
['Manzana', 'Naranja']
```

---

# pop()

También podemos eliminar utilizando:

```python
pop()
```

Por ejemplo:

```python
frutas = ["Manzana", "Banana", "Naranja"]

frutas.pop(1)

print(frutas)
```

Resultado:

```text
['Manzana', 'Naranja']
```

En este caso eliminamos el elemento ubicado en el índice `1`.

---

# Cantidad de elementos

Podemos utilizar:

```python
len()
```

Ejemplo:

```python
frutas = ["Manzana", "Banana", "Naranja"]

print(len(frutas))
```

Resultado:

```text
3
```

---

# Índices negativos

Python también permite acceder desde el final de una lista.

```python
frutas = ["Manzana", "Banana", "Naranja"]
```

Podemos utilizar:

```python
print(frutas[-1])
```

Resultado:

```text
Naranja
```

Tenemos:

```text
 Manzana    Banana    Naranja
    -3        -2         -1
```

Por lo tanto:

```python
frutas[-1]
```

representa el último elemento.

---

# Diferentes tipos de datos

Una lista puede contener diferentes tipos:

```python
datos = [
    "Jonatan",
    38,
    1.75,
    True
]
```

Tenemos:

```text
"Jonatan" → str
38        → int
1.75      → float
True      → bool
```

Python permite almacenar estos valores dentro de la misma lista.

En programas reales, sin embargo, muchas listas contienen elementos conceptualmente relacionados.

---

# ¿Una lista puede contener otra lista?

Sí.

Por ejemplo:

```python
datos = [
    ["Python", 10],
    ["C#", 9],
    ["JavaScript", 8]
]
```

Esto se conoce como una lista anidada.

Podemos acceder:

```python
print(datos[0])
```

Resultado:

```text
['Python', 10]
```

Y también:

```python
print(datos[0][0])
```

Resultado:

```text
Python
```

---

# Listas y bucles

Las listas se vuelven especialmente útiles cuando las combinamos con bucles.

Por ejemplo:

```python
frutas = ["Manzana", "Banana", "Naranja"]

for fruta in frutas:
    print(fruta)
```

Resultado:

```text
Manzana
Banana
Naranja
```

Esto nos permite procesar todos los elementos sin acceder manualmente a cada posición.

Más adelante profundizaremos en este tipo de recorridos.

---

# Métodos básicos

Algunos métodos importantes son:

```text
append()   → agregar al final

insert()   → insertar en una posición

remove()   → eliminar por valor

pop()      → eliminar por índice
```

Y una función que utilizaremos constantemente:

```text
len()      → cantidad de elementos
```

---

# Diferencia con una cadena

En el capítulo anterior vimos:

```python
texto = "Python"
```

Una cadena es inmutable.

En cambio:

```python
frutas = ["Manzana", "Banana"]
```

es una lista y puede modificarse.

Por ejemplo:

```python
frutas[0] = "Naranja"
```

es válido.

---

# Ejercicio

Creá una lista con tres lenguajes:

```python
lenguajes = [
    "Python",
    "C#",
    "JavaScript"
]
```

Después:

1. Mostrá el primer lenguaje.
2. Agregá `"SQL"`.
3. Eliminá `"JavaScript"`.
4. Mostrá la cantidad de elementos.
5. Mostrá la lista final.

---

# Desafío

Creá una lista vacía:

```python
nombres = []
```

Pedile al usuario tres nombres y agregalos utilizando:

```python
append()
```

Finalmente mostrá:

```text
Nombres ingresados:
[...]
```

Esto permite combinar conceptos de capítulos anteriores:

```text
input()
variables
listas
append()
```

---

# Dato importante

Las listas son:

```text
ORDENADAS
MODIFICABLES
INDEXADAS
```

Y sus índices comienzan en:

```text
0
```

Ejemplo:

```python
frutas = ["Manzana", "Banana", "Naranja"]
```

```text
0 → Manzana
1 → Banana
2 → Naranja
```

---

# Resumen

Crear:

```python
frutas = ["Manzana", "Banana"]
```

Acceder:

```python
frutas[0]
```

Agregar:

```python
frutas.append("Naranja")
```

Modificar:

```python
frutas[1] = "Frutilla"
```

Eliminar:

```python
frutas.remove("Manzana")
```

Cantidad:

```python
len(frutas)
```

Las listas son una de las estructuras de datos fundamentales de Python y las utilizaremos constantemente a medida que avancemos.
