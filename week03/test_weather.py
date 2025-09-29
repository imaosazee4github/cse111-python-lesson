from weather import cels_from_fahr
from pytest import approx

import pytest

def  test_cels_from_fahr():
    """Test the cels_from_fahr function by calling it and comparing the values it returns.
    Notice this test function uses pytest.approx to compare floating-points numbers.
    """

    assert cels_from_fahr(-25) == approx(-31.66667)
    assert cels_from_fahr(0) == approx(-17.77778)
    assert cels_from_fahr(32) == approx(0)
    assert cels_from_fahr(70) == approx(21.1111)
# call the main function that is part of the pytest so that the computer
# will execute the test functions in this file

pytest.main(["-v", "--tb=line", "-rN", __file__])