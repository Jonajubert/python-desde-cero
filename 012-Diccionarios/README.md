# Python Desde Cero

## Capítulo 012 - Diccionarios

En los capítulos anteriores aprendimos a trabajar con listas y tuplas.

En ambas estructuras accedemos a los elementos mediante su posición.

Ahora conoceremos una estructura que permite asociar cada valor con una **clave**:

**DICCIONARIOS**

---

## Crear un diccionario

Utilizamos llaves `{}` y pares `clave: valor`, separados por comas:

```python
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Eldorado"
}
```

Cada clave identifica un dato.

| Clave | Valor |
|---|---|
| `"nombre"` | `"Ana"` |
| `"edad"` | `25` |
| `"ciudad"` | `"Eldorado"` |

Los valores pueden tener diferentes tipos. En este ejemplo tenemos textos y un número entero.

---

## Acceder a un valor

Escribimos la clave entre corchetes:

```python
print(persona["nombre"])
```

Resultado:

```text
Ana
```

En este diccionario usamos `"nombre"` para obtener el nombre. No utilizamos su posición.

---

## Cantidad de elementos

Podemos utilizar `len()`:

```python
print(len(persona))
```

Resultado:

```text
3
```

Cuenta los pares clave-valor.

---

## Modificar un valor

Asignamos un nuevo valor a una clave existente:

```python
persona["edad"] = 26
print(persona["edad"])
```

Resultado:

```text
26
```

---

## Agregar un dato

Si la clave no existe, la asignación agrega un nuevo par:

```python
persona["lenguaje"] = "Python"
print(len(persona))
```

Resultado:

```text
4
```

---

## Consultar con get()

Si accedemos con corchetes a una clave que no existe, Python genera `KeyError`.

Podemos usar `get()` y definir un valor alternativo:

```python
print(persona.get("telefono", "No registrado"))
```

Resultado:

```text
No registrado
```

Esta consulta no agrega la clave al diccionario.

Si omitimos el valor alternativo, devuelve `None` cuando la clave no existe.

---

## Comprobar una clave

`in` permite comprobar si una clave está presente:

```python
if "nombre" in persona:
    print("La clave nombre existe.")
```

En un diccionario, `in` busca entre las claves.

---

## Eliminar un dato

Utilizamos `del` seguido del acceso por clave:

```python
del persona["ciudad"]
```

Se elimina tanto la clave como su valor asociado.

La clave debe existir.

---

## Recorrer un diccionario

Podemos utilizar `for` junto con `items()`:

```python
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

Después de los cambios anteriores:

```text
nombre: Ana
edad: 26
lenguaje: Python
```

En cada vuelta, `items()` entrega una clave y su valor.

Las variables `clave` y `valor` reciben esos dos datos.

---

## Las claves son únicas

Asignar otra vez sobre la misma clave reemplaza su valor:

```python
producto = {"nombre": "Cuaderno", "precio": 1500}

producto["precio"] = 1800

print(producto["precio"])
```

Resultado:

```text
1800
```

No se crea una segunda clave `"precio"`.

---

## Ejercicio

Crear un diccionario llamado `libro` con:

- Título.
- Autor.
- Año.

Después:

1. Mostrar el título usando su clave.
2. Modificar el año.
3. Agregar la clave `"disponible"` con el valor `True`.
4. Mostrar la cantidad de pares.
5. Recorrerlo con `items()`.

---

## Desafío

Crear un diccionario con tres productos y sus precios:

```python
precios = {
    "pan": 1800,
    "leche": 1500,
    "arroz": 1200
}
```

Recorrerlo y calcular cuánto cuesta comprar una unidad de cada producto.

Podés comenzar con:

```python
total = 0

for producto, precio in precios.items():
    total += precio

print(total)
```

Resultado esperado:

```text
4500
```

---

## Dato importante

Los diccionarios son modificables y conservan el orden de inserción, pero el acceso a sus valores se realiza mediante claves.

En este capítulo usamos claves de texto.

También pueden utilizarse otros tipos aptos como claves, por ejemplo números; las listas no pueden ser claves.

Un diccionario vacío se crea con `{}`.

---

## Resumen

| Acción | Código |
|---|---|
| Crear | `persona = {"nombre": "Ana"}` |
| Acceder | `persona["nombre"]` |
| Agregar o modificar | `persona["edad"] = 26` |
| Consultar con alternativa | `persona.get("telefono", "No registrado")` |
| Comprobar una clave | `"nombre" in persona` |
| Eliminar | `del persona["edad"]` |
| Contar | `len(persona)` |
| Recorrer pares | `persona.items()` |

Concepto fundamental:

**Cada clave permite identificar un valor.**

---

## Ejecutar el ejemplo

Desde esta carpeta:

```bash
python main.py
```
