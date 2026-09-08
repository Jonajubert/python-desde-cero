# Python Desde Cero

## Capítulo 008 - Bucle for

En el capítulo anterior aprendimos a utilizar el bucle:

```python
while
```

Ahora conoceremos otra estructura de repetición fundamental de Python:

```python
for
```

`for` nos permite recorrer los elementos de un iterable y ejecutar un bloque de código para cada uno de ellos.

---

# ¿Qué aprenderás?

En este capítulo veremos:

- Qué es un bucle `for`.
- Cómo funciona.
- Cómo utilizar `range()`.
- Cómo recorrer una lista.
- Qué representa la variable del bucle.
- Cómo utilizar inicio, fin y paso.
- Diferencias básicas entre `for` y `while`.

---

# Nuestro primer for

Podemos mostrar los números del 1 al 5 utilizando:

```python
for numero in range(1, 6):
    print(numero)
```

Resultado:

```text
1
2
3
4
5
```

La estructura:

```python
for numero in range(1, 6):
```

puede interpretarse como:

```text
PARA CADA número
       ↓
generado por range(1, 6)
       ↓
ejecutar el bloque
```

---

# ¿Qué hace range()?

`range()` genera una secuencia de números.

Por ejemplo:

```python
range(1, 6)
```

representa:

```text
1
2
3
4
5
```

El valor final no está incluido.

Por eso:

```text
inicio = 1
fin    = 6
```

produce valores hasta:

```text
5
```

---

# Inicio incluido, fin excluido

Este concepto es importante.

```python
range(1, 6)
```

podemos visualizarlo así:

```text
1  → incluido
2  → incluido
3  → incluido
4  → incluido
5  → incluido
6  → excluido
```

Por eso obtenemos cinco iteraciones.

---

# ¿Qué es numero?

En:

```python
for numero in range(1, 6):
```

`numero` es la variable que recibe el valor correspondiente en cada iteración.

Tenemos:

```text
1ª iteración → numero = 1
2ª iteración → numero = 2
3ª iteración → numero = 3
4ª iteración → numero = 4
5ª iteración → numero = 5
```

Después de asignar cada valor se ejecuta:

```python
print(numero)
```

---

# Flujo del for

Podemos representarlo así:

```text
range(1, 6)
     │
     ▼
     1
     │
     ▼
print(1)
     │
     ▼
     2
     │
     ▼
print(2)
     │
     ▼
    ...
     │
     ▼
     5
     │
     ▼
print(5)
     │
     ▼
    FIN
```

Python se encarga de avanzar automáticamente al siguiente elemento.

---

# Recorrer una lista

`for` no sirve únicamente para trabajar con números.

También podemos recorrer una lista:

```python
lenguajes = ["Python", "C#", "JavaScript"]

for lenguaje in lenguajes:
    print(lenguaje)
```

Resultado:

```text
Python
C#
JavaScript
```

En cada vuelta:

```text
lenguaje = "Python"

lenguaje = "C#"

lenguaje = "JavaScript"
```

---

# La estructura general

Podemos pensar:

```python
for elemento in iterable:
    instrucciones
```

Tenemos:

```text
elemento
   ↓
variable que recibe cada valor


iterable
   ↓
objeto cuyos elementos recorremos
```

Una lista es un ejemplo de iterable.

`range()` también produce un objeto iterable.

---

# range con un argumento

También podemos escribir:

```python
for numero in range(5):
    print(numero)
```

Resultado:

```text
0
1
2
3
4
```

Cuando utilizamos:

```python
range(5)
```

el comienzo implícito es:

```text
0
```

y el final continúa siendo excluido.

---

# range con inicio y fin

```python
range(1, 6)
```

Tenemos:

```text
inicio = 1
fin    = 6
```

Resultado:

```text
1 2 3 4 5
```

---

# range con paso

Podemos agregar un tercer argumento:

```python
range(0, 11, 2)
```

Su estructura es:

```text
range(inicio, fin, paso)
```

Tenemos:

```text
inicio → 0
fin    → 11
paso   → 2
```

Resultado:

```text
0
2
4
6
8
10
```

---

# Otro ejemplo

Podemos contar de cinco en cinco:

```python
for numero in range(0, 51, 5):
    print(numero)
```

Resultado:

```text
0
5
10
15
20
25
30
35
40
45
50
```

---

# for vs while

En el capítulo anterior utilizamos:

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

Ahora podemos conseguir el mismo resultado con:

```python
for numero in range(1, 6):
    print(numero)
```

Pero conceptualmente no funcionan de la misma manera.

---

# while

`while` trabaja principalmente alrededor de una condición:

```text
MIENTRAS
una condición sea verdadera
↓
repetir
```

Por ejemplo:

```python
while contraseña != "1234":
```

No necesariamente sabemos de antemano cuántas iteraciones tendremos.

---

# for

`for` recorre los elementos de un iterable:

```text
PARA CADA
elemento
↓
ejecutar
```

Por ejemplo:

```python
for lenguaje in lenguajes:
```

---

# Comparación inicial

```text
WHILE

¿La condición sigue siendo verdadera?
              ↓
             Sí
              ↓
           repetir
```

```text
FOR

¿Queda otro elemento por recorrer?
              ↓
             Sí
              ↓
           ejecutar
```

No se trata de elegir siempre uno u otro.

Debemos utilizar la estructura que represente mejor el problema.

---

# La indentación

Al igual que con `if` y `while`, Python utiliza la indentación para determinar qué instrucciones pertenecen al bloque.

Correcto:

```python
for numero in range(1, 6):
    print(numero)
    print("Iteración terminada")
```

Las dos instrucciones pertenecen al `for`.

---

# Ejemplo completo

```python
for numero in range(1, 6):
    print(numero)


lenguajes = ["Python", "C#", "JavaScript"]

for lenguaje in lenguajes:
    print(lenguaje)


for numero in range(0, 11, 2):
    print(numero)
```

---

# Dato importante

En:

```python
range(1, 6)
```

el `1` está incluido, pero el `6` no.

Por eso obtenemos:

```text
1
2
3
4
5
```

Recordar esta característica evita muchos errores al comenzar a trabajar con `range()`.

---

# Ejercicio

Utilizando `for` y `range()`, mostrar:

```text
1
2
3
4
5
6
7
8
9
10
```

Después modificar el programa para mostrar solamente:

```text
2
4
6
8
10
```

Pista:

```python
range(inicio, fin, paso)
```

---

# Desafío extra

Crear una lista:

```python
nombres = ["Ana", "Pedro", "Lucía", "Carlos"]
```

y utilizar:

```python
for
```

para mostrar:

```text
Hola Ana
Hola Pedro
Hola Lucía
Hola Carlos
```

---

# Próximo capítulo

Ya conocemos dos estructuras fundamentales de repetición:

```text
while
for
```

A partir de ellas podremos recorrer colecciones, automatizar tareas y construir algoritmos cada vez más interesantes.
