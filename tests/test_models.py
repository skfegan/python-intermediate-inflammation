"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [3, 4]),
        ([[1.2, 2.1], [5.9, 6.0], [3.4, 4.5]], [3.5, 4.2]),
    ])
def test_daily_mean(test, expected):
    """Test that mean function works for an array of zeros, positive integers, and floats."""
    from inflammation.models import daily_mean

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 6], [5, 4]], [5, 6]),
        ([[1.2, 2.1], [5.9, 6.0], [3.4, 4.5]], [5.9, 6.0]),
    ])
def test_daily_max(test, expected):
    """Test that max function works for an array of zeros, positive integers, and floats."""
    from inflammation.models import daily_max

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [1, 2]),
        ([[1.2, 2.1], [5.9, 6.0], [0.4, 4.5]], [0.4, 2.1]),
    ])
def test_daily_min(test, expected):
    """Test that min function works for an array of zeros, positive integers, and floats."""
    from inflammation.models import daily_min

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))

