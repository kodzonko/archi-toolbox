from asyncio.log import logger
from pathlib import Path

from reportlab.graphics.shapes import Drawing, Group
from svglib.svglib import svg2rlg

from archi_toolbox.architecture.exceptions import InputError


def load_plan(file: Path) -> Drawing:
    """Load a plan outline from a file."""
    try:
        drawing: Drawing = svg2rlg(file)
        contents: Group = drawing.getContents()[0]
        return drawing
    except OSError:
        logger.error("Failed to open file in load_plan from file: %s." % file)
        raise InputError(f"Could not load the plan from file: {file}.")
