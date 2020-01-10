'''
Tests for the eigenvalue analysis
'''

from numpy.testing import assert_almost_equal
from unittest import TestCase

from . import test_two_bar_truss_model
from ..bracketing import bracketing

class TestBracketing(TestCase):
    def setUp(self):
        # two bar truss model
        self.model = test_two_bar_truss_model.get_model()

    def test_bracketing_limit_point(self):
        limit_model = self.model.get_duplicate()
        limit_model.predict_tangential(strategy="lambda", value=0.05)
        limit_model.perform_non_linear_solution_step(strategy="load-control")

        critical_model = bracketing(limit_model)

        actual = critical_model.lam
        expected = 0.13607744543608463
        assert_almost_equal(actual, expected)

    def test_bracketing_bifurcation_point(self):
        bifurcation_model = self.model.get_duplicate()
        bifurcation_model._nodes['B'].reference_y = 3.0
        bifurcation_model._nodes['B'].y = 3.0
        bifurcation_model.predict_tangential(strategy="lambda", value=0.05)
        bifurcation_model.perform_non_linear_solution_step(strategy="load-control")

        critical_model = bracketing(bifurcation_model)
        actual = critical_model.lam
        expected = 0.16733018783531955
        assert_almost_equal(actual, expected)