Unit tests for E8 arithmetic universe calculations
"""

import pytest
import numpy as np
from src.e8_physics import E8ArithmeticUniverse
from src.modular_forms import E8ModularForms

class TestE8Calculations:
    
    def setup_method(self):
        self.universe = E8ArithmeticUniverse(precision=30)
        self.modular = E8ModularForms(precision=30)
    
    def test_phi_e8_value(self):
        """Test E8 golden ratio calculation"""
        phi = self.universe.phi_e8
        expected = (1 + np.sqrt(5))/2 * np.sqrt(8/5)
        
        assert abs(float(phi) - expected) < 1e-10
    
    def test_spectral_zeta(self):
        """Test E8 spectral zeta function"""
        zeta_minus_one = self.universe.compute_spectral_zeta(-1)
        assert abs(float(zeta_minus_one) - 1/240) < 1e-10
    
    def test_modular_invariance(self):
        """Test modular invariance of E8 theta function"""
        tau = 1j  # Imaginary unit
        invariance = self.modular.modular_invariance_check(tau)
        
        # Should be very small
        assert float(invariance['relative_error']) < 1e-10
    
    def test_cosmological_constant(self):
        """Test cosmological constant calculation"""
        result = self.universe.compute_cosmological_constant()
        lambda_value = result['value']
        
        # Should match predicted value
        expected = 1.1058e-52
        assert abs(lambda_value - expected) < 1e-55
    
    def test_fermion_mass_hierarchy(self):
        """Test fermion mass hierarchy"""
        masses = self.universe.compute_fermion_masses()
        
        # Check mass ordering
        assert masses['top'] > masses['bottom'] > masses['charm']
        assert masses['tau'] > masses['muon'] > masses['electron']
    
    def test_dark_matter_mass(self):
        """Test dark matter mass prediction"""
        dm = self.universe.compute_dark_matter_mass()
        
        # Should be around 12.7 GeV
        assert 12.0 < dm['value'] < 13.0
        assert dm['uncertainty'] == 0.3

if __name__ == "__main__":
    pytest.main([__file__, "-v"])