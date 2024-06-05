import pytest
import scipy.stats as sp

from utils.fin_utils import calculate_parametric_var


def test_calculate_parametric_var():
    # Define test inputs and expected outputs
    value = 1_000_000  # Portfolio value
    confidence = 0.95  # 95% confidence level
    mu = 0.05  # Annualized expected return (5%)
    sigma = 0.2  # Annualized volatility (20%)

    # Calculate expected VaR using the formula
    F_inv = sp.norm.ppf(1 - confidence)
    expected_var = abs(value * (mu - sigma * F_inv))

    # Call the function
    calculated_var = calculate_parametric_var(value, confidence, mu, sigma)

    # Assert the result
    assert calculated_var == pytest.approx(expected_varr, rel=1e-5)
