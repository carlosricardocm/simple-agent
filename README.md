# Tu primer agente de IA — versión Gemini

Código de apoyo para la sección **«Taller: construye un agente desde cero»**
de la presentación *Agentes, prompts y RAG*.

Es un agente de IA funcional en ~245 líneas de Python, **sin frameworks**:
solo memoria, herramientas y un bucle.

## Requisitos

- **Python 3.10 o superior** (obligatorio: `google-genai` no existe para 3.9 ni anteriores)
- Una llave de la API de Gemini (gratuita): https://aistudio.google.com/apikey

Comprueba tu versión antes de nada:

```bash
python --version
```

Si dice 3.9 o menos, ve a la sección «Problemas comunes» más abajo.

## Instalación

### Opción A — con conda (recomendada)

Es la ruta más limpia en Windows: evita los conflictos de PATH entre varias
instalaciones de Python.

```bash
conda create -n agente python=3.10 -y
conda activate agente
pip install -r requirements.txt
```

### Opción B — con venv

Necesitas que el `python` que uses sea 3.10 o superior. Si tienes varias
versiones instaladas en Windows, el lanzador `py` te deja elegir:

```bash
py -3.13 -m venv .venv        # Windows
python3 -m venv .venv         # macOS / Linux

.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux

python -m pip install --upgrade pip
pip install -r requirements.txt
```

### La llave

Copia `.env.example` a `.env` y pon ahí tu llave:

```
GEMINI_API_KEY=xxxxxxxxxxxxxxxxxxxx
```

## Ejecución

```bash
python main.py
```

Probado con Python 3.10 (conda) y `google-genai` 2.19.0.

Cosas que puedes pedirle:

- `¿Qué archivos hay en esta carpeta?`
- `Lee el archivo main.py y explícame qué hace en dos frases.`
- `Crea un archivo notas.txt con una lista de los temas de la clase.`
- `En notas.txt cambia "RAG" por "Generación aumentada por recuperación".`

Escribe `salir` para terminar.

## Problemas comunes

### `ERROR: Could not find a version that satisfies the requirement google-genai`

Va acompañado de `(from versions: none)`. Casi siempre significa que **tu Python es
anterior al 3.10**, que es el mínimo que pide el paquete. Un pip antiguo (20.x) es la
pista: es el que venía con Python 3.9.

Comprueba primero:

```bash
python --version
```

**Si es 3.9 o menor**, lo más rápido es crear un entorno de conda con una versión
compatible (no hace falta desinstalar nada):

```bash
conda create -n agente python=3.10 -y
conda activate agente
pip install -r requirements.txt
```

Si no usas conda, instala un Python moderno desde https://www.python.org/downloads/
(marca *Add python.exe to PATH*) y crea el entorno con él:

```bash
rmdir /s /q .venv
py -3.13 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

`py -3.13` usa el lanzador de Windows para elegir la versión; con `py -0` ves todas las
que tienes instaladas. Ojo: si tienes Anaconda, su Python suele quedar primero en el
PATH y `python` a secas apuntará a él aunque instales uno más nuevo.

**Si ya es 3.10 o mayor**, basta con actualizar pip:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### `google.genai.errors.ClientError: API key not valid`

La llave no se está leyendo. Revisa que el archivo se llame exactamente `.env` (no
`.env.txt`), que esté en la misma carpeta que `main.py` y que la línea sea
`GEMINI_API_KEY=...` sin comillas ni espacios alrededor del `=`.

### `AttributeError: 'Client' object has no attribute 'interactions'`

Tu `google-genai` es demasiado antiguo. Actualiza: `pip install -U google-genai`.

## Aviso importante

El agente **lee y escribe archivos reales** en tu disco, en el directorio desde
donde lo ejecutas. Pruébalo siempre dentro de una carpeta de juguete, nunca en
una carpeta con trabajo importante. No tiene deshacer.

## Archivos

| Archivo            | Qué contiene                                              |
|--------------------|-----------------------------------------------------------|
| `agent.py`         | Memoria, declaración e implementación de las herramientas |
| `main.py`          | Cliente de Gemini y los dos bucles                        |
| `requirements.txt` | Dependencias                                              |
| `.env.example`     | Plantilla para tu llave                                   |

## Créditos

Adaptado del proyecto *Tu primer agente de IA* de Ringa Tech
(https://github.com/ringa-tech/tu-primer-agente-de-ia), que a su vez se basa
en *How to Build an Agent* de Thorsten Ball. La versión original usa la API de
OpenAI; aquí se portó a la API de Gemini para poder probarla con la capa
gratuita.
