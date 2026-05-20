from pathlib import Path

import pytest

from archi_toolbox.architecture.operations.tiling import load_plan

from ...conftest import RESOURCE_ROOT


@pytest.fixture
def rectangle() -> Path:
    return RESOURCE_ROOT / "simple_rectangle.svg"


def test_load_plan_loads_drawing_from_svg(rectangle: Path) -> None:
    plan = load_plan(rectangle)
    assert len(plan.getContents()) == 1
