"""Utilidades de visualización con el estilo F1 Broadcast Dark Mode."""

import matplotlib.pyplot as plt

from .config import AX_COLOR, BG_COLOR, BLANCO_F1, GRID_COLOR, PLATA_F1


def f1_dark_context(font_family: str = "Bahnschrift"):
    """Devuelve un context manager ``rc_context`` con el tema oscuro F1 oficial.

    Args:
        font_family: Familia tipográfica principal para títulos y etiquetas.

    Returns:
        Context manager de Matplotlib listo para usar en bloques ``with``.
    """
    return plt.rc_context(
        {
            "font.family": font_family,
            "axes.titleweight": "bold",
            "axes.titlesize": 14,
            "axes.titlepad": 15,
            "axes.labelsize": 11,
            "axes.labelweight": "normal",
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "grid.color": GRID_COLOR,
            "grid.linestyle": "--",
            "grid.alpha": 0.8,
            "legend.frameon": False,
            "legend.fontsize": 10,
            "figure.facecolor": BG_COLOR,
            "axes.facecolor": AX_COLOR,
        }
    )


def estilizar_ejes_f1(
    ax: plt.Axes,
    titulo: str,
    xlabel: str = "",
    ylabel: str = "",
    grid_axis: str = "both",
) -> plt.Axes:
    """Aplica título, etiquetas, colores de ejes y bordes limpios estilo broadcast.

    Args:
        ax: Objeto ``Axes`` de Matplotlib a formatear.
        titulo: Título principal del gráfico.
        xlabel: Etiqueta del eje X. Si está vacía, no se modifica.
        ylabel: Etiqueta del eje Y. Si está vacía, no se modifica.
        grid_axis: Ejes sobre los que mostrar la rejilla (``"both"``, ``"x"`` o ``"y"``).

    Returns:
        El mismo objeto ``Axes`` estilizado.
    """
    ax.set_title(titulo, color=BLANCO_F1)
    if xlabel:
        ax.set_xlabel(xlabel, color=PLATA_F1, labelpad=8)
    if ylabel:
        ax.set_ylabel(ylabel, color=PLATA_F1, labelpad=8)
    ax.tick_params(colors=PLATA_F1)
    ax.grid(True, axis=grid_axis)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(GRID_COLOR)
    ax.spines["bottom"].set_color(GRID_COLOR)
    return ax


def umbral_criterio(
    ax: plt.Axes,
    y: float,
    etiqueta: str,
    color: str = PLATA_F1,
    linestyle: str = "--",
    linewidth: float = 1.6,
) -> None:
    """Traza una línea horizontal de referencia para distinguir umbrales de aceptación.

    Args:
        ax: Objeto ``Axes`` sobre el que dibujar la línea.
        y: Valor en el eje Y correspondiente al umbral de criterio.
        etiqueta: Texto descriptivo para la leyenda del gráfico.
        color: Color hexadecimal o nombre de color de la línea.
        linestyle: Estilo de trazo de Matplotlib (por defecto discontinuo ``"--"``).
        linewidth: Grosor de la línea en puntos.
    """
    ax.axhline(
        y=y,
        color=color,
        linestyle=linestyle,
        linewidth=linewidth,
        label=etiqueta,
        zorder=2,
    )
