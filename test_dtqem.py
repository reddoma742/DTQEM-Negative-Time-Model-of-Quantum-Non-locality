"""
Unit Tests for DTQEM Final Code
Run with: python -m unittest test_dtqem.py
"""

import unittest
import numpy as np
from dtqem_final import DTQEM, DoubleSlitPhysics

class TestDTQEM(unittest.TestCase):
    def setUp(self):
        self.model = DTQEM(t_obs=1e-6, distance_km=11000)

    def test_v_eff_at_180_0K(self):
        v = self.model.v_eff(180, 0)
        self.assertAlmostEqual(v, 1e7, delta=1e6)

    def test_v_eff_at_180_300K(self):
        v = self.model.v_eff(180, 300)
        self.assertAlmostEqual(v, 1200, delta=120)

    def test_visibility_between_0_and_1(self):
        for theta in [0, 90, 180]:
            for T in [0, 150, 300]:
                vis = self.model.visibility(theta, T)
                self.assertGreaterEqual(vis, 0.0)
                self.assertLessEqual(vis, 1.0)

    def test_t_eff_positive_or_inf(self):
        t = self.model.t_eff(180, 0)
        self.assertTrue(t > 0 or np.isinf(t))

    def test_delta_E_positive_or_inf(self):
        dE = self.model.delta_E_eV(180, 0)
        self.assertTrue(dE > 0 or np.isinf(dE))

    def test_invalid_theta_raises(self):
        with self.assertRaises(ValueError):
            self.model.alpha(200)
        with self.assertRaises(ValueError):
            self.model.v_eff(200, 0)

    def test_invalid_T_raises(self):
        with self.assertRaises(ValueError):
            self.model.K_eff(-10)

class TestDoubleSlit(unittest.TestCase):
    def setUp(self):
        self.ds = DoubleSlitPhysics()

    def test_intensity_range(self):
        x, I = self.ds.pattern_1d(visibility=0.5)
        self.assertTrue(np.all(I >= 0))
        self.assertTrue(np.all(I <= 1))

    def test_symmetric_pattern(self):
        x, I = self.ds.pattern_1d(visibility=1.0)
        mid = len(x)//2
        self.assertAlmostEqual(I[mid-10], I[mid+10], places=5)

if __name__ == '__main__':
    unittest.main()
