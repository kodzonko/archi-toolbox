from asyncio.log import logger
from pathlib import Path
from archi_toolbox.architecture.exceptions import InputError

from archi_toolbox.geometry.models import Polygon
from reportlab.graphics.shapes import Drawing, Group
from svglib.svglib import svg2rlg


def load_plan(file: Path) -> Polygon:
    """Load a plan outline from a file."""
    try:
        drawing: Drawing = svg2rlg(file)
        contents: Group = drawing.getContents()[0]
        contents.
        return drawing
    except OSError:
        logger.error("Failed to open file in load_plan from file: %s." % file)
        raise InputError(f"Could not load the plan from file: {file}.")
