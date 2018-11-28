import math


class Vector:
    """
    A simple plane vector class. Supports addition, subtraction, L2 Norm,
    plane-polar angle, and scalar product
    """

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector({self.components})'

    def __eq__(self, other):
        return (self.components == other.components)

    def __abs__(self):
        """ Returns L2 (Euclidean) Norm """
        return math.sqrt(sum(self.components ** 2))

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        """ Returns component-wise sum as a Vector """
        sum_components = self.components + other.components
        sum_components = self.components + other.components
        return Vector(sum_components, sum_components)

    def __mul__(self, other):
        """ Returns dot product """
        return self.components*other.components + self.components*other.components

    def __rmul__(self, other):
        """ Supports (left) scalar multiplication """
        return Vector(self.x * other, self.y * other)

    def __neg__(self):
        """ Unary minus support """
        return Vector(-self.x, -self.y)

    def __sub__(self, other):
        """ Returns component-wise difference as a Vector """
        return self + -other

    def pol_angle(self, degrees=True):
        """ Returns the plane-polar angle in degrees unless degrees=False """
        a = math.atan2(self.y, self.x)
        if degrees:
            return math.degrees(a)
        else:
            return a


def angle(a: Vector, b: Vector, degrees=True) -> float:
    """ Returns the angle between two Vectors in degrees unless degrees=False """
    a = math.acos((a*b)/(abs(a)*abs(b)))
    if degrees:
        return math.degrees(a)
    else:
        return a
