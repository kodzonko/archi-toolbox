from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    z: int | None = None


@dataclass
class Edge:
    start: Point
    end: Point


@dataclass
class Polygon:
    points: list[Point]
