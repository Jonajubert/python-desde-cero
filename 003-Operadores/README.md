# Python Desde Cero

#  Capítulo 003

# Operadores

Hasta ahora aprendimos a almacenar información utilizando variables.

Ahora veremos cómo trabajar con esos datos mediante operadores.

Los operadores permiten realizar cálculos, comparar valores y evaluar condiciones.

---

#  ¿Qué aprenderás?

- Qué es un operador.
- Operadores aritméticos.
- Operadores de comparación.
- Operadores lógicos.
- Cuándo utilizar cada uno.

---

# Operadores aritméticos

Permiten realizar operaciones matemáticas.

| Operador | Descripción |
|----------|-------------|
| + | Suma |
| - | Resta |
| * | Multiplicación |
| / | División |
| // | División entera |
| % | Resto |
| ** | Potencia |

Ejemplo

```python
resultado = 20 + 10
```

---

# Operadores de comparación

Devuelven `True` o `False`.

| Operador | Significado |
|----------|-------------|
| == | Igual |
| != | Distinto |
| > | Mayor |
| < | Menor |
| >= | Mayor o igual |
| <= | Menor o igual |

Ejemplo

```python
20 > 10
```

Resultado

```text
True
```

---

# Operadores lógicos

Permiten combinar condiciones.

| Operador | Descripción |
|----------|-------------|
| and | AND |
| or | OR |
| not | NOT |

Ejemplo

```python
True and False
```

Resultado

```text
False
```

---

# Resultado esperado

```text
=== OPERADORES EN PYTHON ===

Suma: 30
Resta: 10
Multiplicación: 200
División: 2.0

¿20 es mayor que 10?: True
¿20 es igual a 10?: False

True and False = False
True or False = True
not True = False
```

---

#  Ejercicio

Crear dos variables numéricas y mostrar:

- Suma.
- Resta.
- Multiplicación.
- División.

Luego comparar ambos valores utilizando:

- >
- <
- ==

Finalmente probar:

- and
- or
- not

---

#  ¿Sabías que?

En Python los operadores lógicos se escriben como palabras (`and`, `or`, `not`), mientras que en C# se utilizan símbolos (`&&`, `||`, `!`).

Es una de las primeras diferencias que notarás al aprender ambos lenguajes.

---

#  Próximo capítulo

## Entrada y salida de datos

Aprenderemos a utilizar `input()` para leer información ingresada por el usuario.
