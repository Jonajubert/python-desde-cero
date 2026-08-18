# Python Desde Cero

## Capítulo 005 - Condicional if

Hasta ahora nuestros programas ejecutaban las instrucciones una detrás de otra.

En este capítulo aprenderemos a ejecutar código solamente cuando se cumple una determinada condición.

Para eso utilizaremos `if`.

---

# ¿Qué aprenderás?

- Qué es una condición.
- Cómo utilizar `if`.
- Qué significan `True` y `False`.
- Cómo utilizar operadores de comparación.
- Por qué la indentación es importante.
- Cómo ejecutar código según una condición.

---

# ¿Qué es if?

`if` permite ejecutar un bloque de código solamente cuando una condición se cumple.

Su estructura básica es:

```python
if condicion:
    # Código que se ejecutará
```

Por ejemplo:

```python
edad = 20

if edad >= 18:
    print("Sos mayor de edad.")
```

---

# ¿Cómo funciona?

Python evalúa:

```python
edad >= 18
```

El resultado solamente puede ser:

```text
True
```

o:

```text
False
```

Si obtenemos `True`, se ejecuta el código perteneciente al `if`.

Si obtenemos `False`, ese código se omite.

---

# Flujo de decisión

Podemos representarlo así:

```text
           edad >= 18
                │
                ▼
          ¿Se cumple?
           /        \
        True        False
          │            │
          ▼            ▼
      Ejecutar      Continuar
       código       programa
```

---

# Los dos puntos

Observá esta línea:

```python
if edad >= 18:
```

Después de la condición aparecen:

```text
:
```

Los dos puntos indican el comienzo del bloque asociado al `if`.

---

# La indentación

Python utiliza la indentación para determinar qué instrucciones pertenecen al `if`.

Correcto:

```python
if edad >= 18:
    print("Sos mayor de edad.")
```

Incorrecto:

```python
if edad >= 18:
print("Sos mayor de edad.")
```

La indentación no es solamente una cuestión estética.

Forma parte de la sintaxis de Python.

---

# Recibir la edad

En el capítulo anterior aprendimos a utilizar:

```python
input()
```

Pero `input()` devuelve texto.

Si ingresamos:

```text
30
```

inicialmente obtenemos:

```text
"30"
```

Para trabajar con ese valor como número utilizamos:

```python
int()
```

Por eso escribimos:

```python
edad = int(input())
```

Ahora `edad` contiene un número entero.

---

# Código completo

```python
print("Escribí tu nombre:")
nombre = input()

print("Escribí tu edad:")
edad = int(input())

if edad >= 18:
    print(f"Hola {nombre}, sos mayor de edad.")
```

---

# Operadores de comparación

Podemos construir diferentes condiciones:

| Operador | Significado |
|---|---|
| `==` | Igual a |
| `!=` | Distinto de |
| `>` | Mayor que |
| `<` | Menor que |
| `>=` | Mayor o igual |
| `<=` | Menor o igual |

Por ejemplo:

```python
edad >= 18
```

pregunta:

> ¿La edad es mayor o igual a 18?

---

# = no es lo mismo que ==

Esta diferencia es fundamental.

## Asignación

```python
edad = 18
```

Significa:

```text
Guardar 18 en edad.
```

## Comparación

```python
edad == 18
```

Significa:

```text
¿edad es igual a 18?
```

El resultado será:

```text
True
```

o:

```text
False
```

---

# True y False

Podemos comprobar directamente una comparación:

```python
edad = 20

print(edad >= 18)
```

Resultado:

```text
True
```

Pero:

```python
edad = 16

print(edad >= 18)
```

produce:

```text
False
```

---

# Ejercicio

Crear un programa que solicite una nota:

```python
print("Ingresá una nota:")
nota = int(input())
```

Luego utilizar `if` para mostrar:

```text
Aprobado
```

solamente cuando la nota sea mayor o igual a 6.

---

# Dato importante

En Python, la indentación forma parte de la sintaxis.

El código que queremos ejecutar cuando el `if` sea verdadero debe estar correctamente indentado.

```python
if condicion:
    # Este código pertenece al if
```

---

# Próximo paso

Ya sabemos ejecutar código cuando una condición es verdadera.

Pero todavía falta responder una pregunta:

¿Qué hacemos cuando la condición es falsa?

Para eso incorporaremos `else`.
