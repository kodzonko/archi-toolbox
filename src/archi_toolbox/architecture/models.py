"""Architecture domain models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from archi_toolbox.geometry.models import Polygon


@dataclass
class Tile:
    """Represents a tile with its geometry and tiling characteristics."""

    geometry: Polygon
    grout_width: float
