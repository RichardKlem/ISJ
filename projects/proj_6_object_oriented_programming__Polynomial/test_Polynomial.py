from isj_proj6_xklemr00 import Polynomial
import pytest


class TestPolynomial:
    @staticmethod
    def test_equality(pol_a, pol_b, exp_res):
        ...

    @staticmethod
    def test_string(pol_a, exp_res):
        ...

    @staticmethod
    def test_addition(pol_a, pol_b, exp_res):
        ...

    @staticmethod
    def test_multiplication(pol_a, pol_b):
        ...

    @staticmethod
    def test_power(pol_a, exponent, exp_res):
        ...


# Set of different types of polynomials.
class TestListPol(TestPolynomial):
    const_pol_pos1 = Polynomial([5])
    const_pol_pos2 = Polynomial([3])
    const_pol_neg1 = Polynomial([-2])
    const_pol_neg2 = Polynomial([-2])

    lin_pol_pos = Polynomial([5, 3])
    lin_pol_mix = Polynomial([1, -2])
    lin_pol_neg = Polynomial([-12, -7])

    quad_pol_pos = Polynomial([-1, 0, 5])
    quad_pol_mix = Polynomial([2, 1, 0])
    quad_pol_neg = Polynomial([-3, -7, -11])

    general_pol1 = Polynomial([-3, -7, 5, 1, 0, -28, 115, -42])
    general_pol2 = Polynomial([5, 82, -31, -3])
    general_pol3 = Polynomial([0, 0, -1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 19])

    all_pols = [const_pol_pos1, const_pol_pos2, const_pol_neg1, const_pol_neg2, lin_pol_pos,
                lin_pol_mix, lin_pol_neg, quad_pol_pos, quad_pol_mix, quad_pol_neg, general_pol1,
                general_pol2, general_pol3]

    @staticmethod
    @pytest.mark.parametrize('pol_a,pol_b,exp_res',
                             [
                                     (const_pol_pos1, const_pol_pos1, True),
                                     (lin_pol_mix, lin_pol_mix, True),
                                     (lin_pol_mix, quad_pol_mix, False),
                                     (quad_pol_neg, quad_pol_neg, True),
                                     (const_pol_pos1, const_pol_pos1, False),
                                     (general_pol3, const_pol_pos1, False),
                                     (general_pol3, general_pol3, False),
                                     (general_pol3, general_pol2, False),])
    def test_equality(pol_a: Polynomial, pol_b: Polynomial, exp_res: bool):
        assert ((pol_a == pol_b) == exp_res)

    @staticmethod
    def test_string(pol_a, exp_res):
        ...

    @staticmethod
    def test_addition(pol_a, pol_b, exp_res):
        ...

    @staticmethod
    def test_multiplication(pol_a, pol_b):
        ...

    @staticmethod
    def test_power(pol_a, exponent, exp_res):
        ...


class TestKeywordsPol:
    const_pol_pos1 = Polynomial(x0=5)
    const_pol_pos2 = Polynomial(x0=1)
    const_pol_neg1 = Polynomial(x0=-3)
    const_pol_neg2 = Polynomial(x0=-11)

