# Python Desde Cero

## Capítulo 004 - Entrada y salida de datos

Hasta ahora nuestros programas trabajaban con valores definidos directamente en el código.

En este capítulo aprenderemos a interactuar con el usuario utilizando la consola.

---

# ¿Qué aprenderás?

- Cómo mostrar información.
- Cómo utilizar `print()`.
- Cómo solicitar información al usuario.
- Cómo utilizar `input()`.
- Cómo guardar la información ingresada.
- Cómo mostrar posteriormente esos datos.

---

# 1. Mostrar información

Para mostrar información en Python utilizamos:

```python
print()
```

Por ejemplo:

```python
print("Hola mundo")
```

Resultado:

```text
Hola mundo
```

---

# 2. Solicitar información

Podemos utilizar `print()` para indicarle al usuario qué dato queremos.

```python
print("Escribí tu nombre:")
```

La consola mostrará:

```text
Escribí tu nombre:
```

Por ahora solamente estamos mostrando información.

Todavía necesitamos leer lo que escriba el usuario.

---

# 3. Leer información

Para recibir información utilizamos:

```python
input()
```

Podemos guardar el dato ingresado directamente en una variable:

```python
nombre = input()
```

El programa esperará hasta que el usuario escriba algo y presione Enter.

Si escribe:

```text
Jonatan
```

la variable `nombre` almacenará ese valor.

---

# 4. Mostrar la variable

Una vez almacenado el dato podemos utilizarlo.

```python
print(nombre)
```

También podemos combinar texto y variables utilizando una f-string:

```python
print(f"Hola, {nombre}!")
```

Si `nombre` contiene:

```text
Jonatan
```

obtendremos:

```text
Hola, Jonatan!
```

---

# ¿Cómo funciona?

Nuestro programa sigue este proceso:

```text
1. SOLICITAR

print("Escribí tu nombre:")

        ↓

2. LEER

input()

        ↓

3. GUARDAR

nombre = input()

        ↓

4. MOSTRAR

print(f"Hola, {nombre}!")
```

---

# Otra forma de utilizar input()

Python también permite colocar el mensaje directamente dentro de `input()`:

```python
nombre = input("Escribí tu nombre: ")
```

Esto reemplaza:

```python
print("Escribí tu nombre:")
nombre = input()
```

Ambas formas funcionan.

En este capítulo utilizamos inicialmente las instrucciones separadas para observar claramente qué hace cada una.

---

# Código completo

```python
print("Escribí tu nombre:")
nombre = input()

print("Escribí tu ciudad:")
ciudad = input()

print()
print("=== DATOS INGRESADOS ===")

print(f"Hola, {nombre}!")
print(f"Vivís en {ciudad}.")
```

---

# Dato importante

`input()` devuelve texto.

Esto significa que si escribimos:

```text
30
```

Python inicialmente lo recibe como texto.

Por ahora trabajaremos con información de tipo `str`.

Más adelante veremos cómo convertir los datos ingresados para trabajar con números.

---

# Ejercicio

Modificar el programa para solicitar:

- Nombre.
- Ciudad.
- Lenguaje de programación que estás aprendiendo.

Guardar cada respuesta en una variable.

Luego mostrar:

```text
=== PERFIL ===

Nombre: Jonatan
Ciudad: Eldorado
Aprendiendo: Python
```

---

# Probá también

Después de comprender el primer ejemplo, reemplazá:

```python
print("Escribí tu nombre:")
nombre = input()
```

por:

```python
nombre = input("Escribí tu nombre: ")
```

Compará ambos resultados.

---

# Próximo capítulo

Continuaremos trabajando con los datos ingresados por el usuario y aprenderemos a utilizarlos dentro de programas más completos.
