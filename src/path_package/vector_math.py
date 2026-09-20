#imports
from sympy.core.symbol import Symbol, symbols
from sympy.core.numbers import Integer, Float, Rational, Pi
from sympy.core.power import Pow
from sympy.core.add import Add
from sympy.core.mul import Mul
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.functions.elementary.exponential import exp, log
from sympy.functions.elementary.trigonometric import (
        sin,
        cos,
        tan,
        csc,
        cot,
        sec,
        asin,
        acos,
        atan,
        acot,
        asec,
        acsc,
        atan2,
        pi,
)
from sympy.simplify.simplify import simplify
from sympy.core.function import expand
from sympy.polys.polytools import factor
from sympy.simplify.radsimp import radsimp


#global variables


#classes

class Vector:
    """
    This is the class for vector objects.  Vecors contain an i, j,
    and k component, which can be positive or negative.
    """
    def __init__(self, i, j, k):
        """The initialization of the class Vector"""
        self.i = i
        self.j = j
        self.k = k
        self.component = (self.i, self.j, self.k)

    def mag_square(self):
        """
        A method for determining the squared magnitude of a vector
        """
        i_comp = pow(self.i, 2)
        j_comp = pow(self.j, 2)
        k_comp = pow(self.k, 2)
        mag_square = i_comp+j_comp+k_comp
        return mag_square

    def magnitude(self):
        """A method to determine the magnitude of a vector"""
        i_comp = pow(self.i, 2)
        j_comp = pow(self.j, 2)
        k_comp = pow(self.k, 2)

        magnitude = sqrt((i_comp+j_comp+k_comp))
        return magnitude

    def unit_vector(self):
        """
        A method to form a tuple representing the unit vector
        associated with a given Vector.  Used to create such an object
        later.
        """
        magnitude = self.magnitude()
        i_unit = radsimp(self.i / magnitude)
        j_unit = radsimp(self.j / magnitude)
        k_unit = radsimp(self.k / magnitude)
        unit_vector = (i_unit, j_unit, k_unit)
        return unit_vector


    def scalar(self, scalar):
        """A method for applying scalar multiplication"""
        self.i *= scalar
        self.j *= scalar
        self.k *= scalar
        self.component = (self.i, self.j, self.k)

    def __str__(self):
        """"A method for string formation"""
        return f"<{self.i}i, {self.j}j, {self.k}k>"

"""
As of 08/09/2026 this is class is not used, but may be implemented
in future modules
"""
class ThreeDLine:
    pass

"""
As of 08/06/2026 this class is unused and may be added to a
physics module at a later date
"""
class ForceVector(Vector):
    pass
    
"""
As of 08/06/2026 this class is unused and may be reworked later
for a different purpose
"""
class CrossProductDeterminant:
    pass


#Functions
def dot(v1, v2):
    """A function used to compute dot products"""
    dot_prod =  (v1.i*v2.i) + (v1.j*v2.j) + (v1.k*v2.k)
    return dot_prod

def angle_between(v1, v2):
    """A method used to find the angle between two vectors"""
    mags_mul = v1.magnitude() * v2.magnitude()
    dot_prod = dot(v1, v2)
    cos_theta = radsimp(dot_prod / mags_mul)
    theta = acos(cos_theta)
    return theta

def ortho_check(v1, v2):
    """A function for checking if two vectors are orthogonal"""
    if dot(v1, v2) == 0:
        return True
    return False

def proj(v1, v2):
    """A function used to project v1 onto v2"""
    dot_prod = dot(v1, v2)
    v2_mag_sq = v2.mag_square()
    scalar_comp = Rational(dot_prod, v2_mag_sq)
    i, j, k = v2.component
    proj_v1_on_v2 = Vector(i, j, k)
    proj_v1_on_v2.scalar(scalar_comp)
    return proj_v1_on_v2

def work_by_dot(v1, v2):
    """
    A function used to compute work when the angle between vectors is
    not known.  Note that this function is somewhat redundant, but in
    is meant to be expanded later.
    """
    work = dot(v1, v2)
    return work

def work_by_angle(v1, v2, theta):
    """
    A function used to compute the work done when the angle between two
    vectors is known
    """
    work = v1.magnitude()*v2.magnitude()*(cos(theta))
    return work

def cross_product(v1, v2):
    """A function used to calculate the cross product of two vectors"""
    v1i, v1j, v1k = v1.component
    v2i, v2j, v2k = v2.component

    cp_i = (v1j*v2k)-(v2j*v1k)
    cp_j = -((v1i*v2k)-(v2i*v1k))
    cp_k = (v1i*v2j)-(v2i*v1j)

    cross_product = Vector(cp_i, cp_j, cp_k)
    return cross_product

def add_vectors(v1, v2):
    """A function used to perform vector addition"""
    v1i, v1j, v1k = v1.component
    v2i, v2j, v2k = v2.component

    added_i = v1i+v2i
    added_j = v1j+v2j
    added_k = v1k+v2k

    added_vector = Vector(added_i, added_j, added_k)
    return added_vector

def subtract_vectors(v1, v2):
    """A function used to perform vector subtraction"""
    v1i, v1j, v1k = v1.component
    v2i, v2j, v2k = v2.component

    subtracted_i = v1i-v2i
    subtracted_j = v1j-v2j
    subtracted_k = v1k-v2k

    subtracted_vector = Vector(
        subtracted_i, subtracted_j, subtracted_k
    )
    return subtracted_vector
