"""Geometry domain models."""

from dataclasses import dataclass


@dataclass
class Point:
    """A point in two- or three-dimensional space."""

    x: int
    y: int
    z: int | None = None


@dataclass
class Edge:
    """A line segment between two points."""

    start: Point
    end: Point


@dataclass
class Polygon:
    """A polygon represented by an ordered list of points."""

    points: list[Point]
