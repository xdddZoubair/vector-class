import math


class Vector:
    """
    A simple plane vector class. Supports addition, subtraction, L2 Norm,
    plane-polar angle, and scalar product
    """

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):
        return not self == other

    def __abs__(self):
        """ Returns L2 (Euclidean) Norm """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        """ Returns component-wise sum as a Vector """
        sum_x = self.x + other.x
        sum_y = self.y + other.y
        return Vector(sum_x, sum_y)

    def __mul__(self, other):
        """ Returns dot product """
        return self.x*other.x + self.y*other.y

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


