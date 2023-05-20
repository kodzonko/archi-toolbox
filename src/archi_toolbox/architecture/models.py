from dataclasses import dataclass

from archi_toolbox.geometry.models import Polygon


@dataclass
class Tile:
    """Represents a tile with its geometry and tiling characteristics."""

    geometry: Polygon
    grout_width: float
