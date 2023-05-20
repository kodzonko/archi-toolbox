from dataclasses import dataclass
from typing import Optional


@dataclass
class Point:
    x: int
    y: int
    z: Optional[int] = None


@dataclass
class Edge:
    start: Point
    end: Point


@dataclass
class Polygon:
    points: list[Point]
