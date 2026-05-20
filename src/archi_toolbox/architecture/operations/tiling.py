"""Operations for loading and processing tile plans."""

from __future__ import annotations

from typing import TYPE_CHECKING

from svglib.svglib import svg2rlg

from archi_toolbox.architecture.exceptions import InputError
from archi_toolbox.logger import logger

if TYPE_CHECKING:
    from pathlib import Path

    from reportlab.graphics.shapes import Drawing


def load_plan(file: Path) -> Drawing:
    """Load a plan outline from a file."""
    try:
        drawing: Drawing = svg2rlg(file)
    except OSError as exc:
        logger.error("Failed to open file in load_plan from file: {}.", file)
        raise InputError.plan_load_failed(file) from exc
    else:
        return drawing
