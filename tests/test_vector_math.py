"""
This is a testing module for the vector math module controlling the 
underlying math of this program.
"""

#imports
import unittest
import path_package.vector_math as vec
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

class TestVector(unittest.TestCase):
    """This is the test class fot the Vector object."""

    def setUp(self):
        self.vector1 = vec.Vector(2, 3, 6)
        self.vector2 = vec.Vector(1, 0, 0)
        self.vector3 = vec.Vector(1, 1, 1)
        """
        This vector was chose as a low magnitude vector with a whole
        number magnitude of 7.  It is a pythagorean triple.
        """

    def test_mag_square(self):
        self.assertEqual(self.vector1.mag_square(), 49, "mag^2 incorrect")

    def test_magnitude(self):
        self.assertEqual(
            self.vector1.magnitude(), 7, "magnitude incorrect"
        )

    def test_unit_vector(self):
        i_comp = Rational(2, 7)
        j_comp = Rational(3, 7)
        k_comp = Rational(6, 7)
        unit_vector_tuple = self.vector1.unit_vector()
        self.assertEqual(
            unit_vector_tuple,
            (i_comp, j_comp, k_comp),
            "unit_vector method incorrect"
        )

    def test_scalar(self):
        #scalar_vector = self.vector3.scalar(3)
        #scalar_vector_components = scalar_vector.component
        self.vector3.scalar(3)
        self.assertEqual(
            self.vector3.component,
            (3, 3, 3),
            "scalar incorrect"
        )

    def test__str__(self):
        self.assertEqual(
            str(self.vector2), "<1i, 0j, 0k>",
            "string formation incorrect"
        )


# Functions tests
class TestDotProduct(unittest.TestCase):
    def test_dot(self):
        vector1 = vec.Vector(1, 2, 3)
        vector2 = vec.Vector(3, 2, 1)
        dot_product = vec.dot(vector1, vector2)
        self.assertEqual(dot_product, 10, "dot incorrect.")

class TestAngleBetween(unittest.TestCase):
    def test_angle_between(self):
        vector1 = vec.Vector(1, 0, 0)
        vector2 = vec.Vector(1, sqrt(3), 0)
        expected_angle_between = vec.angle_between(vector1, vector2)
        self.assertEqual(
            expected_angle_between, pi/3, "angle_between incorrect."
        )

class TestOrthoCheck(unittest.TestCase):
    def test_ortho_check(self):
        vector1 = vec.Vector(1, 0, 0)
        vector2 = vec.Vector(0, 1, 0)
        ortho = vec.ortho_check(vector1, vector2)
        self.assertTrue(ortho, "ortho_check incorrect")

class TestProjClass(unittest.TestCase):
    def test_proj_class(self):
        vector1 = vec.Vector(5, 2, 0)
        vector2 = vec.Vector(1, 2, 2)
        #now we obtain the projection of vector1 on vector2
        proj_v1_v2 = vec.proj(vector1, vector2)
        self.assertIsInstance(
            proj_v1_v2, vec.Vector, "proj class incorrect"
        )

class TestProjOutcome(unittest.TestCase):
    def test_proj_outcome(self):
        vector1 = vec.Vector(5, 2, 0)
        vector2 = vec.Vector(1, 2, 2)
        #now we obtain the projection of vector1 on vector2
        proj_v1_v2 = vec.proj(vector1, vector2)
        self.assertEqual(
            proj_v1_v2.component, (1, 2, 2), "proj value incorrect"
        )

class TestWorkByDot(unittest.TestCase):
    def test_work_by_dot(self):
        vector1 = vec.Vector(1, 2, 1)
        vector2 = vec.Vector(2, 1, 2)
        dot_work = vec.dot(vector1, vector2)
        self.assertEqual(
            dot_work, 6, "work_by_dot incorrect"
        )

class TestWorkByAngle(unittest.TestCase):
    def test_work_by_angle(self):
        vector1 = vec.Vector(2, 0, 0)
        vector2 = vec.Vector(1, 1, sqrt(2))
        theta = pi/4
        angle_work = vec.work_by_angle(vector1, vector2, theta)
        self.assertEqual(
            angle_work, 2*sqrt(2), "work_by_angle incorrect"
        )

class TestCrossProductClass(unittest.TestCase):
    def test_cross_product_class(self):
        vector1 = vec.Vector(1, 2, 3)
        vector2 = vec.Vector(3, 2, 1)
        crossp_vector = vec.cross_product(vector1, vector2)
        self.assertIsInstance(
            crossp_vector, vec.Vector, "cross_product class incorrect"
        )

class TestCrossProductResult(unittest.TestCase):
    def test_cross_product_result(self):
        vector1 = vec.Vector(1, 2, 3)
        vector2 = vec.Vector(4, 5, 6)
        crossp_vector = vec.cross_product(vector1, vector2)
        crossp_comp = crossp_vector.component
        self.assertEqual(
            crossp_comp, (-3, 6, -3), "cross_product result incorrect"
        )

class TestAddVectors(unittest.TestCase):
    def test_add_vectors(self):
        vector1 = vec.Vector(1, 2, 3)
        vector2 = vec.Vector(3, 2, 1)
        add_vec = vec.add_vectors(vector1, vector2)
        self.assertEqual(
            add_vec.component, (4, 4, 4), "add_vectors incorrect"
        )

class TestSubtractVectors(unittest.TestCase):
    def test_subtract_vectors(self):
        vector1 = vec.Vector(4, 5, 6)
        vector2 = vec.Vector(1, 1, 1)
        sub_vec = vec.subtract_vectors(vector1, vector2)
        self.assertEqual(
            sub_vec.component, (3, 4, 5), "subtract_vectors incorrect"
        )

if __name__=='--main__':
    unittest.main()
