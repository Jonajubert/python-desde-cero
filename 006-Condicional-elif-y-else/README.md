# Python Desde Cero

## Capítulo 006 - Condicional elif y else

En el capítulo anterior aprendimos a utilizar `if`.

Ahora vamos a ampliar nuestras estructuras condicionales utilizando:

```python
elif
else
```

Esto nos permitirá crear programas capaces de elegir entre varios caminos.

---

# ¿Qué aprenderás?

- Cómo utilizar `else`.
- Cómo utilizar `elif`.
- Cómo evaluar varias condiciones.
- Cómo funciona el orden de evaluación.
- Por qué la indentación sigue siendo fundamental.

---

# Recordemos if

`if` permite ejecutar código cuando una condición es verdadera.

```python
edad = 20

if edad >= 18:
    print("Sos mayor de edad.")
```

Pero si la condición es falsa, ese bloque simplemente no se ejecuta.

---

# else

Podemos utilizar `else` para indicar qué hacer cuando la condición no se cumple.

```python
edad = 16

if edad >= 18:
    print("Sos mayor de edad.")
else:
    print("Sos menor de edad.")
```

Ahora tenemos dos caminos:

```text
          edad >= 18
               │
        ┌──────┴──────┐
        │             │
      True          False
        │             │
        ▼             ▼
       if            else
```

---

# elif

¿Qué ocurre si necesitamos más de dos posibilidades?

Python utiliza:

```python
elif
```

Por ejemplo:

```python
if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
```

Ahora nuestro programa tiene tres posibles resultados.

---

# ¿Qué significa elif?

Podemos interpretarlo como:

```text
else + if
```

Es decir:

> Si la condición anterior fue falsa, evaluá esta otra condición.

En otros lenguajes podemos encontrar:

```text
else if
```

Python utiliza la palabra:

```python
elif
```

---

# ¿Cómo se evalúa?

Supongamos:

```python
nota = 8
```

Primero:

```text
nota >= 9
8 >= 9
False
```

Python continúa.

Después:

```text
nota >= 6
8 >= 6
True
```

Entonces ejecuta:

```text
Aprobado
```

y termina esa cadena condicional.

---

# Flujo completo

```text
                 nota >= 9
                     │
              ┌──────┴──────┐
            True           False
              │               │
              ▼               ▼
         Excelente        nota >= 6
                              │
                       ┌──────┴──────┐
                     True           False
                       │               │
                       ▼               ▼
                   Aprobado       Desaprobado
```

---

# El orden importa

Consideremos:

```python
nota = 10
```

Esto está correctamente ordenado:

```python
if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprobado")
```

Python encuentra:

```text
10 >= 9 → True
```

Resultado:

```text
Excelente
```

---

# ¿Qué ocurre si invertimos el orden?

```python
if nota >= 6:
    print("Aprobado")
elif nota >= 9:
    print("Excelente")
```

Con:

```text
nota = 10
```

la primera condición ya es verdadera:

```text
10 >= 6 → True
```

Resultado:

```text
Aprobado
```

Python no continúa evaluando el `elif`.

Por eso el orden de nuestras condiciones puede cambiar el resultado.

---

# La indentación sigue siendo fundamental

Cada bloque debe estar correctamente indentado:

```python
if nota >= 9:
    print("Excelente")

elif nota >= 6:
    print("Aprobado")

else:
    print("Desaprobado")
```

La indentación indica qué instrucciones pertenecen a cada condición.

---

# Estructura general

```python
if condicion_1:
    # Primera posibilidad

elif condicion_2:
    # Segunda posibilidad

else:
    # Ninguna condición anterior
```

Podemos tener varios `elif`:

```python
if condicion_1:
    ...

elif condicion_2:
    ...

elif condicion_3:
    ...

else:
    ...
```

---

# Código completo

```python
print("Escribí tu nombre:")
nombre = input()

print("Ingresá tu nota:")
nota = int(input())

if nota >= 9:
    print(f"Excelente, {nombre}.")

elif nota >= 6:
    print(f"Aprobaste, {nombre}.")

else:
    print(f"Desaprobaste, {nombre}.")
```

---

# Ejercicio

Crear un programa que solicite una temperatura.

Clasificarla de la siguiente manera:

```text
30 o más
→ Hace calor

Entre 15 y 29
→ Temperatura agradable

Menos de 15
→ Hace frío
```

Utilizar:

```python
if
elif
else
```

---

# Dato importante

Python evalúa las condiciones de arriba hacia abajo.

Cuando encuentra la primera condición:

```text
True
```

ejecuta ese bloque y omite los restantes de esa cadena.

Por eso:

```text
EL ORDEN IMPORTA
```

---

# Próximo capítulo

Ya podemos utilizar Python para tomar decisiones entre varios caminos.

A partir de estas estructuras podremos construir programas con comportamientos cada vez más interesantes.
