import pytest
from svglib.svglib import svg2rlg
from pathlib import Path
from mockito import when

from archi_toolbox.architecture.operations.tiling import load_plan
from tests.unit.conftest import RESOURCE_ROOT


@pytest.fixture
def rectangle() -> "Drawing":
    return RESOURCE_ROOT / "simple_rectangle.svg"


def test_load_plan_loads_polygon_from_svg(rectangle: "Drawing") -> None:
    plan = load_plan(rectangle)
    assert plan.getContents() == "l"
