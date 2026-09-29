# Python Desde Cero

## Capítulo 011 - Tuplas

En el capítulo anterior aprendimos a trabajar con listas:

```python
frutas = ["Manzana", "Banana", "Naranja"]
```

Ahora conoceremos otra estructura de datos de Python:

```text
TUPLAS
```

Una tupla permite almacenar varios elementos, pero tiene una diferencia fundamental con las listas:

**es inmutable.**

---

## Crear una tupla

Utilizamos normalmente paréntesis:

```python
colores = ("Rojo", "Verde", "Azul")
```

Podemos mostrarla:

```python
print(colores)
```

Resultado:

```text
('Rojo', 'Verde', 'Azul')
```

---

## Índices

Los elementos tienen posiciones que comienzan desde `0`.

```text
Índice     Elemento

0          Rojo
1          Verde
2          Azul
```

Por ejemplo:

```python
print(colores[0])
```

Resultado:

```text
Rojo
```

---

## Cantidad de elementos

También podemos utilizar:

```python
len()
```

Ejemplo:

```python
print(len(colores))
```

Resultado:

```text
3
```

---

## Las tuplas son inmutables

Esta es su característica principal.

Después de crear:

```python
colores = ("Rojo", "Verde", "Azul")
```

no podemos hacer:

```python
colores[0] = "Amarillo"
```

Python genera un error porque los elementos de una tupla no pueden modificarse de esa manera.

---

## Lista vs tupla

Una lista:

```python
colores = ["Rojo", "Verde", "Azul"]
```

es:

```text
MODIFICABLE
```

Una tupla:

```python
colores = ("Rojo", "Verde", "Azul")
```

es:

```text
INMUTABLE
```

Esta es una de las diferencias más importantes que debemos recordar.

---

## Recorrer una tupla

Podemos utilizar un `for`:

```python
colores = ("Rojo", "Verde", "Azul")

for color in colores:
    print(color)
```

Resultado:

```text
Rojo
Verde
Azul
```

---

## Diferentes tipos

Una tupla puede contener valores de diferentes tipos:

```python
datos = ("Jonatan", 38, True)
```

Aquí tenemos:

```text
"Jonatan" → str
38        → int
True      → bool
```

---

## Tupla de un solo elemento

Existe un detalle importante.

Esto:

```python
numero = (5)
```

no crea una tupla.

Para crear una tupla con un solo elemento necesitamos la coma:

```python
numero = (5,)
```

Podemos comprobarlo:

```python
print(type(numero))
```

Resultado:

```text
<class 'tuple'>
```

---

## ¿Cuándo utilizar una tupla?

Son útiles cuando queremos representar valores que conceptualmente no deberían cambiar.

Por ejemplo:

```python
coordenada = (10, 25)
```

o:

```python
fecha = (29, 9, 2026)
```

La inmutabilidad ayuda a evitar modificaciones accidentales.

---

## Ejercicio

Crear una tupla con cinco lenguajes:

```python
lenguajes = (
    "Python",
    "C#",
    "JavaScript",
    "SQL",
    "HTML"
)
```

Después:

1. Mostrar el primer elemento.
2. Mostrar el último.
3. Mostrar la cantidad.
4. Recorrerla utilizando `for`.

---

## Desafío

Crear una tupla:

```python
numeros = (10, 20, 30, 40, 50)
```

Recorrerla y calcular la suma de todos sus elementos.

Podés comenzar con:

```python
suma = 0
```

y después:

```python
for numero in numeros:
    suma += numero
```

---

## Dato importante

La diferencia esencial:

```text
LISTA
[]
Modificable


TUPLA
()
Inmutable
```

Ambas permiten almacenar múltiples valores y acceder a ellos mediante índices.

---

## Resumen

Crear:

```python
colores = ("Rojo", "Verde", "Azul")
```

Acceder:

```python
colores[0]
```

Cantidad:

```python
len(colores)
```

Recorrer:

```python
for color in colores:
    print(color)
```

Concepto fundamental:

```text
Las tuplas son inmutables.
```
