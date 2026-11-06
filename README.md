# Flet Window Icon for Windows

Ejemplo mínimo para configurar el icono de una ventana Flet y generar un ejecutable de Windows con ese icono.

## Requisitos

- Windows
- Python instalado
- Flet instalado
- Un archivo de icono `.ico`

## Estructura

```text
flet-window-icon/
├── main.py
├── assets/
│   └── mi_ico.ico
├── requirements.txt
└── README.md
```

## 1. Instalar Flet

```bash
pip install -r requirements.txt
```

## 2. Colocar el icono

Guardá tu archivo `.ico` en:

```text
assets/mi_ico.ico
```

## 3. Ejecutar la aplicación

```bash
flet run main.py
```

## 4. Generar el ejecutable

```bash
flet pack main.py --name FletWindowIcon --icon assets\mi_ico.ico --add-data "assets:assets" --pyinstaller-build-args=--clean --yes
```

El comando establece el icono del ejecutable (`--icon`) e incluye la carpeta `assets` (`--add-data`).

## ¿Qué hace `ruta_recurso()`?

La función contempla dos situaciones:

- Cuando se ejecuta el archivo Python, busca los recursos junto a `main.py`.
- Cuando se ejecuta la aplicación empaquetada, busca los recursos en la carpeta temporal utilizada por PyInstaller (`sys._MEIPASS`).

## Las dos configuraciones del icono

- `page.window.icon`: configura el icono de la ventana de Flet.
- `--icon`: configura el icono del archivo ejecutable de Windows.

Son configuraciones independientes.

## Nota

Este ejemplo fue preparado para Windows. La compatibilidad debe comprobarse con la versión de Flet y las herramientas de empaquetado utilizadas en cada entorno.
