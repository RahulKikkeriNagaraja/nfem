'''
Tests for the eigenvalue analysis
'''

from numpy.testing import assert_almost_equal
from unittest import TestCase

from . import test_two_bar_truss_model

class TestEigenvalueAnalysis(TestCase):
    def setUp(self):
        # two bar truss model
        self.model = test_two_bar_truss_model.get_model()

    def test_limit_point(self):
        limit_model = self.model.get_duplicate()
        limit_model.lam = 0.1
        limit_model.perform_non_linear_solution_step(strategy="load-control")
        limit_model.solve_eigenvalues()

        ev_actual = limit_model.first_eigenvalue
        ev_expected = 3.6959287916726304 # safety_factor
        assert_almost_equal(ev_actual, ev_expected)

        # test eigenvector [0.0, 1.0]
        eigenvector_model = limit_model.first_eigenvector_model
        u_actual = eigenvector_model.get_dof_state(('B','u'))
        u_expected = 0.0
        assert_almost_equal(u_actual, u_expected)
        v_actual = eigenvector_model.get_dof_state(('B','v'))
        v_expected = 1.0
        assert_almost_equal(v_actual, v_expected)

    def test_bifurcation_point(self):
        bifurcation_model = self.model.get_duplicate()
        bifurcation_model._nodes['B'].reference_y = 3.0
        bifurcation_model._nodes['B'].y = 3.0
        bifurcation_model.lam = 0.1
        bifurcation_model.perform_non_linear_solution_step(strategy="load-control")
        bifurcation_model.solve_eigenvalues()

        ev_actual = bifurcation_model.first_eigenvalue
        ev_expected = 1.7745968576086002 # safety_factor
        assert_almost_equal(ev_actual, ev_expected)

        # test eigenvector [1.0, 0.0]
        eigenvector_model = bifurcation_model.first_eigenvector_model
        u_actual = eigenvector_model.get_dof_state(('B','u'))
        u_expected = 1.0
        assert_almost_equal(u_actual, u_expected)
        v_actual = eigenvector_model.get_dof_state(('B','v'))
        v_expected = 0.0
        assert_almost_equal(v_actual, v_expected)
        
    def test_LPB_limit_point(self):
        lpb_model = self.model.get_duplicate()
        lpb_model.lam = 0.1
        lpb_model.perform_linear_solution_step()
        lpb_model.solve_linear_eigenvalues()

        lam_crit_actual = lpb_model.first_eigenvalue * lpb_model.lam
        lam_crit_expected = 0.7071067811865452
        assert_almost_equal(lam_crit_actual, lam_crit_expected)

        # FIXME eigenvector shows bifurcation instead of limit for h>=1.0...

