# ============================================================
# circle.py
# A class representing a geometric Circle.
# Demonstrates OOP, properties (decorators), and dunder methods.
# ============================================================

import math  # Used for pi and the area calculation


# ════════════════════════════════════════════════════════════
# CLASS: Circle
# ════════════════════════════════════════════════════════════

class Circle:
    """
    Represents a geometric circle.

    Can be created with a radius or a diameter.
    Supports area computation, string representation,
    addition, and comparison via dunder (magic) methods.
    """

    # ── Constructor ──────────────────────────────────────────
    def __init__(self, radius):
        """
        Initialize the circle with a radius.

        Parameters:
            radius (float): the radius of the circle (must be > 0)
        """
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self._radius = radius  # Store as private attribute

    # ── Class method: alternative constructor via diameter ───
    @classmethod
    def from_diameter(cls, diameter):
        """
        Alternative constructor — create a Circle from a diameter.
        Uses @classmethod so it can be called without an instance.

        Parameters:
            diameter (float): the diameter of the circle

        Returns:
            Circle: a new Circle instance with radius = diameter / 2

        Usage:
            c = Circle.from_diameter(10)  # radius = 5
        """
        return cls(diameter / 2)

    # ── Property: radius ─────────────────────────────────────
    @property
    def radius(self):
        """
        Getter for the radius.
        Using @property makes radius accessible like an attribute,
        not a method call: circle.radius (not circle.radius())
        """
        return self._radius

    @radius.setter
    def radius(self, value):
        """
        Setter for the radius — validates before setting.
        Allows: circle.radius = 7
        """
        if value <= 0:
            raise ValueError("Radius must be a positive number.")
        self._radius = value

    # ── Property: diameter ───────────────────────────────────
    @property
    def diameter(self):
        """
        Computed property — returns the diameter (radius × 2).
        No separate storage needed; always derived from radius.
        """
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        """
        Setter for diameter — converts to radius internally.
        Allows: circle.diameter = 14  →  radius becomes 7
        """
        if value <= 0:
            raise ValueError("Diameter must be a positive number.")
        self._radius = value / 2

    # ── Method: area ─────────────────────────────────────────
    def area(self):
        """
        Computes and returns the area of the circle.
        Formula: π × r²
        """
        return math.pi * self._radius ** 2

    # ── Dunder: __str__ ──────────────────────────────────────
    def __str__(self):
        """
        Human-readable string representation.
        Called by print() and str().

        Example output: Circle(radius=5.00, diameter=10.00, area=78.54)
        """
        return (
            f"Circle(radius={self._radius:.2f}, "
            f"diameter={self.diameter:.2f}, "
            f"area={self.area():.2f})"
        )

    # ── Dunder: __repr__ ─────────────────────────────────────
    def __repr__(self):
        """
        Developer-facing representation.
        Called in the REPL and by repr().
        Should ideally allow recreating the object.
        """
        return f"Circle(radius={self._radius})"

    # ── Dunder: __add__ ──────────────────────────────────────
    def __add__(self, other):
        """
        Adds two circles together.
        Returns a NEW circle whose radius = sum of both radii.
        Called when using the + operator: c1 + c2

        Parameters:
            other (Circle): the circle to add

        Returns:
            Circle: a new Circle with combined radius
        """
        if not isinstance(other, Circle):
            raise TypeError("Can only add a Circle to another Circle.")
        return Circle(self._radius + other._radius)

    # ── Dunder: __gt__ ───────────────────────────────────────
    def __gt__(self, other):
        """
        Checks if this circle is GREATER THAN another.
        Called by the > operator: c1 > c2
        Compares by radius.

        Returns:
            bool: True if self.radius > other.radius
        """
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle with Circle.")
        return self._radius > other._radius

    # ── Dunder: __lt__ ───────────────────────────────────────
    def __lt__(self, other):
        """
        Checks if this circle is LESS THAN another.
        Called by the < operator: c1 < c2
        Also used by sorted() and list.sort() to sort circles.

        Returns:
            bool: True if self.radius < other.radius
        """
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle with Circle.")
        return self._radius < other._radius

    # ── Dunder: __eq__ ───────────────────────────────────────
    def __eq__(self, other):
        """
        Checks if two circles are EQUAL (same radius).
        Called by the == operator: c1 == c2

        Returns:
            bool: True if both circles have the same radius
        """
        if not isinstance(other, Circle):
            return False
        return self._radius == other._radius


# ════════════════════════════════════════════════════════════
# TESTING — runs only when this file is executed directly
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":

    print("=" * 55)
    print("           🔵  CIRCLE CLASS — DEMO")
    print("=" * 55)

    # ── Creating circles ─────────────────────────────────────
    print("\n📌 Creating circles:")

    c1 = Circle(5)                    # From radius
    c2 = Circle.from_diameter(16)     # From diameter → radius = 8
    c3 = Circle(3)
    c4 = Circle(5)                    # Same as c1

    print(f"  c1 = {c1}")
    print(f"  c2 = {c2}")
    print(f"  c3 = {c3}")
    print(f"  c4 = {c4}")

    # ── Radius and diameter access (via @property) ───────────
    print("\n📌 Radius & Diameter:")
    print(f"  c2 radius   : {c2.radius}")
    print(f"  c2 diameter : {c2.diameter}")

    # ── Area ─────────────────────────────────────────────────
    print("\n📌 Area:")
    print(f"  c1 area : {c1.area():.4f}")
    print(f"  c2 area : {c2.area():.4f}")

    # ── Addition (__add__) ───────────────────────────────────
    print("\n📌 Addition (c1 + c2):")
    c5 = c1 + c2  # radius = 5 + 8 = 13
    print(f"  c1 + c2 = {c5}")

    # ── Comparison: greater than (__gt__) ────────────────────
    print("\n📌 Comparison (>):")
    print(f"  c2 > c1 : {c2 > c1}")   # 8 > 5 → True
    print(f"  c3 > c1 : {c3 > c1}")   # 3 > 5 → False

    # ── Comparison: equal (__eq__) ───────────────────────────
    print("\n📌 Equality (==):")
    print(f"  c1 == c4 : {c1 == c4}")  # 5 == 5 → True
    print(f"  c1 == c2 : {c1 == c2}")  # 5 == 8 → False

    # ── Sorting a list of circles (__lt__) ───────────────────
    print("\n📌 Sorting a list of circles:")
    circles = [c2, c3, c1, c5, c4]
    print("  Before sort:", [repr(c) for c in circles])

    circles.sort()  # Uses __lt__ under the hood
    print("  After sort :", [repr(c) for c in circles])

    # ── Modifying via setters ────────────────────────────────
    print("\n📌 Modifying via setters:")
    c3.radius = 10
    print(f"  c3 after setting radius=10  : {c3}")
    c3.diameter = 6
    print(f"  c3 after setting diameter=6 : {c3}")

    print("\n" + "=" * 55)
    print("  ✅ All features demonstrated successfully!")
    print("=" * 55)