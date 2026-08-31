# Python Desde Cero

## Capítulo 007 - Bucle while

Hasta ahora aprendimos a almacenar información, realizar operaciones y tomar decisiones.

Ahora incorporaremos una herramienta fundamental:

**los bucles.**

Un bucle permite ejecutar instrucciones repetidamente.

En este capítulo conoceremos:

```python
while
```

---

# ¿Qué aprenderás?

- Qué es un bucle.
- Cómo funciona `while`.
- Qué es una condición de repetición.
- Cómo utilizar un contador.
- Cómo modificar una variable dentro del bucle.
- Qué es un bucle infinito.
- Cuándo puede ser útil utilizar `while`.

---

# ¿Qué es un bucle?

Un bucle permite repetir un bloque de instrucciones.

Imaginemos que queremos mostrar los números del 1 al 5.

Podríamos escribir:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

Pero estamos repitiendo prácticamente la misma instrucción.

Con un bucle podemos automatizar esa repetición.

---

# El bucle while

Una estructura básica es:

```python
while condicion:
    instrucciones
```

Podemos interpretarla como:

```text
MIENTRAS la condición sea True
            ↓
    ejecutar instrucciones
            ↓
   volver a comprobar
```

Cuando la condición pasa a ser:

```text
False
```

el bucle termina.

---

# Nuestro primer while

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

Resultado:

```text
1
2
3
4
5
```

---

# ¿Cómo funciona?

Comenzamos con:

```python
contador = 1
```

Después Python evalúa:

```python
contador <= 5
```

Primera vuelta:

```text
1 <= 5 → True
```

Entonces ejecuta:

```python
print(contador)
contador += 1
```

Ahora:

```text
contador = 2
```

y Python vuelve a comprobar la condición.

---

# El ciclo completo

```text
contador = 1
     │
     ▼
¿contador <= 5?
     │
  ┌──┴──┐
  │     │
 True  False
  │     │
  ▼     ▼
print   FIN
  │
  ▼
contador += 1
  │
  └───────────────┐
                  │
                  ▼
          comprobar nuevamente
```

---

# Paso a paso

Nuestro programa realiza:

```text
contador = 1
1 <= 5 → True
imprime 1
contador = 2

2 <= 5 → True
imprime 2
contador = 3

3 <= 5 → True
imprime 3
contador = 4

4 <= 5 → True
imprime 4
contador = 5

5 <= 5 → True
imprime 5
contador = 6

6 <= 5 → False

FIN
```

---

# ¿Qué significa +=?

En nuestro código utilizamos:

```python
contador += 1
```

Es una forma abreviada de escribir:

```python
contador = contador + 1
```

Si:

```text
contador = 3
```

después de:

```python
contador += 1
```

tenemos:

```text
contador = 4
```

---

# Cuidado con los bucles infinitos

Observemos:

```python
contador = 1

while contador <= 5:
    print(contador)
```

Tenemos un problema.

`contador` comienza en:

```text
1
```

pero nunca cambia.

Por lo tanto:

```text
1 <= 5 → True
1 <= 5 → True
1 <= 5 → True
1 <= 5 → True
...
```

El programa continúa ejecutando el mismo bloque.

Esto se denomina:

```text
BUCLE INFINITO
```

---

# ¿Cómo lo evitamos?

Tenemos que asegurarnos de que algo modifique la condición.

En nuestro ejemplo:

```python
contador += 1
```

hace que eventualmente lleguemos a:

```text
6 <= 5 → False
```

y el bucle termina.

---

# while con entrada del usuario

`while` también resulta útil cuando no sabemos previamente cuántas repeticiones serán necesarias.

Por ejemplo:

```python
opcion = ""

while opcion != "salir":
    opcion = input("Escribí 'salir' para terminar: ")

print("Programa finalizado.")
```

El programa seguirá preguntando mientras:

```text
opcion != "salir"
```

sea:

```text
True
```

---

# Ejemplo

```text
Escribí 'salir' para terminar: hola

Escribí 'salir' para terminar: continuar

Escribí 'salir' para terminar: prueba

Escribí 'salir' para terminar: salir

Programa finalizado.
```

No sabemos cuántas veces repetirá el usuario la operación.

Por eso `while` resulta apropiado.

---

# La indentación

Como vimos con los condicionales, Python utiliza la indentación para determinar qué instrucciones pertenecen al bloque.

Correcto:

```python
while contador <= 5:
    print(contador)
    contador += 1
```

Ambas instrucciones pertenecen al `while`.

---

# Estructura mental

Cuando utilices `while`, pensá en tres elementos:

```text
1. ESTADO INICIAL

contador = 1


2. CONDICIÓN

contador <= 5


3. ACTUALIZACIÓN

contador += 1
```

Tenemos:

```text
INICIO
  ↓
CONDICIÓN
  ↓
ACCIÓN
  ↓
ACTUALIZACIÓN
  ↓
CONDICIÓN...
```

---

# ¿Cuándo utilizar while?

`while` es especialmente útil cuando queremos repetir algo:

```text
MIENTRAS
```

una condición determinada continúe siendo verdadera.

Por ejemplo:

```text
Mientras el usuario no escriba "salir"

Mientras queden intentos

Mientras exista una conexión

Mientras una condición sea verdadera
```

Más adelante conoceremos otras formas de repetición en Python.

---

# Código completo

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1


opcion = ""

while opcion != "salir":
    opcion = input("Escribí 'salir' para terminar: ")

print("Programa finalizado.")
```

---

# Dato importante

Antes de crear un `while`, preguntate:

> ¿Qué hará que la condición deje de ser verdadera?

Si la respuesta es:

```text
Nada
```

probablemente estés creando un bucle infinito.

---

# Ejercicio

Crear un programa que muestre:

```text
10
9
8
7
6
5
4
3
2
1
¡Despegue!
```

Utilizando:

```python
while
```

Pista:

```python
contador = 10
```

Después tendrás que modificar el contador en cada repetición.

---

# Desafío extra

Crear un programa que solicite una contraseña.

Mientras la contraseña sea incorrecta:

```text
Contraseña incorrecta
```

y volver a solicitarla.

Cuando sea correcta:

```text
Acceso permitido
```

---

# Próximo capítulo

Ya sabemos repetir instrucciones mientras una condición sea verdadera.

A partir de los bucles podremos automatizar tareas y comenzar a construir programas mucho más interesantes.
