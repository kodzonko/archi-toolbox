"""Tests for tile plan loading operations."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from conftest import RESOURCE_ROOT

from archi_toolbox.architecture.operations.tiling import load_plan

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def rectangle() -> Path:
    """Return the simple rectangle SVG test resource."""
    return RESOURCE_ROOT / "simple_rectangle.svg"


def test_load_plan_loads_drawing_from_svg(rectangle: Path) -> None:
    """Load a ReportLab drawing from an SVG file."""
    plan = load_plan(rectangle)
    assert len(plan.getContents()) == 1
