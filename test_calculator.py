import pytest
from main import Calculator


class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_add(self):
        assert self.calc.add(5, 3) == 8
        assert self.calc.add(-2, 7) == 5
        assert self.calc.add(0, 0) == 0
        assert self.calc.add(-3, -4) == -7
        assert self.calc.add(2.5, 3.7) == 6.2
        assert self.calc.add(float('inf'), 1) == float('inf')
        assert self.calc.add(float('-inf'), 1) == float('-inf')

    def test_subtract(self):
        assert self.calc.subtract(10, 4) == 6
        assert self.calc.subtract(5, 8) == -3
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(-3, -7) == 4
        assert self.calc.subtract(5.5, 2.3) == 3.2

    def test_multiply(self):
        assert self.calc.multiply(6, 7) == 42
        assert self.calc.multiply(-3, 4) == -12
        assert self.calc.multiply(0, 100) == 0
        assert self.calc.multiply(-2, -5) == 10
        assert self.calc.multiply(2.5, 4) == 10.0
        assert self.calc.multiply(0.1, 0.2) == pytest.approx(0.02)
        assert self.calc.multiply(float('inf'), 2) == float('inf')

    def test_divide(self):
        assert self.calc.divide(15, 3) == 5
        assert self.calc.divide(-12, 4) == -3
        assert self.calc.divide(7, 2) == 3.5
        assert self.calc.divide(-8, -2) == 4
        assert self.calc.divide(5, 2) == 2.5
        assert self.calc.divide(1, 3) == pytest.approx(0.3333333333333333)
        assert self.calc.divide(float('inf'), 2) == float('inf')

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
        
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(-5, 0)
            
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(0, 0)

    def test_divide_by_float_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0.0)

    def test_sqrt(self):
        assert self.calc.sqrt(16) == 4
        assert self.calc.sqrt(25) == 5
        assert self.calc.sqrt(0) == 0
        assert self.calc.sqrt(2) == pytest.approx(1.414213562373095)
        assert self.calc.sqrt(1) == 1
        assert self.calc.sqrt(0.25) == 0.5
        assert self.calc.sqrt(100) == 10
        assert self.calc.sqrt(float('inf')) == float('inf')

    def test_sqrt_negative(self):
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.sqrt(-4)
            
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.sqrt(-0.1)
            
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.sqrt(float('-inf'))

    @pytest.mark.parametrize("a,b,expected", [
        (5, 3, 8),
        (-2, 7, 5),
        (0, 0, 0),
        (-3, -4, -7),
        (2.5, 3.7, 6.2),
    ])
    def test_add_parametrized(self, a, b, expected):
        assert self.calc.add(a, b) == expected

    @pytest.mark.parametrize("a,expected", [
        (0, 0),
        (1, 1),
        (4, 2),
        (9, 3),
        (16, 4),
        (25, 5),
        (100, 10),
        (2, pytest.approx(1.414213562373095)),
        (3, pytest.approx(1.7320508075688772)),
    ])
    def test_sqrt_parametrized(self, a, expected):
        assert self.calc.sqrt(a) == expected

    def test_pow(self):
        assert self.calc.pow(2, 3) == 8
        assert self.calc.pow(5, 0) == 1
        assert self.calc.pow(10, 1) == 10
        assert self.calc.pow(3, 2) == 9
        assert self.calc.pow(-2, 3) == -8
        assert self.calc.pow(-3, 2) == 9
        assert self.calc.pow(2, -1) == 0.5
        assert self.calc.pow(4, -2) == 0.0625
        assert self.calc.pow(0, 5) == 0
        assert self.calc.pow(1, 100) == 1
        assert self.calc.pow(2.5, 2) == 6.25
        assert self.calc.pow(10, 0.5) == pytest.approx(3.162277660168379)
        assert self.calc.pow(8, 1/3) == pytest.approx(2.0)
        assert self.calc.pow(float('inf'), 2) == float('inf')
        assert self.calc.pow(2, float('inf')) == float('inf')

    def test_pow_zero_to_zero(self):
        # This is mathematically undefined, but Python returns 1
        assert self.calc.pow(0, 0) == 1

    def test_pow_negative_exponent(self):
        assert self.calc.pow(2, -3) == 0.125
        assert self.calc.pow(10, -2) == 0.01
        assert self.calc.pow(-2, -3) == -0.125

    def test_pow_fractional_exponent(self):
        assert self.calc.pow(4, 0.5) == 2
        assert self.calc.pow(9, 0.5) == 3
        assert self.calc.pow(8, 1/3) == pytest.approx(2.0)
        assert self.calc.pow(16, 0.25) == 2

    @pytest.mark.parametrize("base,exponent,expected", [
        (2, 3, 8),
        (5, 0, 1),
        (10, 1, 10),
        (3, 2, 9),
        (-2, 3, -8),
        (-3, 2, 9),
        (2, -1, 0.5),
        (4, -2, 0.0625),
        (0, 5, 0),
        (1, 100, 1),
        (2.5, 2, 6.25),
        (10, 0.5, pytest.approx(3.162277660168379)),
        (8, 1/3, pytest.approx(2.0)),
        (0, 0, 1),
    ])
    def test_pow_parametrized(self, base, exponent, expected):
        assert self.calc.pow(base, exponent) == expected