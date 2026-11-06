import sys
from pathlib import Path

import flet as ft


def ruta_recurso(ruta_relativa: str) -> str:
    """Devuelve la ruta correcta tanto en desarrollo como en el ejecutable."""
    if getattr(sys, "frozen", False):
        base = Path(sys._MEIPASS)
    else:
        base = Path(__file__).resolve().parent

    return str(base / ruta_relativa)


async def main(page: ft.Page) -> None:
    page.title = "Ejemplo: icono de ventana"
    page.window.icon = ruta_recurso("assets/mi_ico.ico")

    page.add(
        ft.Text("¡El icono de la ventana está configurado!"),
        ft.Text("Probá también el ejecutable generado con flet pack."),
    )


ft.run(main)
