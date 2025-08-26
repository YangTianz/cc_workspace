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

    def test_subtract(self):
        assert self.calc.subtract(10, 4) == 6
        assert self.calc.subtract(5, 8) == -3
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(-3, -7) == 4

    def test_multiply(self):
        assert self.calc.multiply(6, 7) == 42
        assert self.calc.multiply(-3, 4) == -12
        assert self.calc.multiply(0, 100) == 0
        assert self.calc.multiply(-2, -5) == 10

    def test_divide(self):
        assert self.calc.divide(15, 3) == 5
        assert self.calc.divide(-12, 4) == -3
        assert self.calc.divide(7, 2) == 3.5
        assert self.calc.divide(-8, -2) == 4

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)

    def test_sqrt(self):
        assert self.calc.sqrt(16) == 4
        assert self.calc.sqrt(25) == 5
        assert self.calc.sqrt(0) == 0
        assert self.calc.sqrt(2) == pytest.approx(1.414213562373095)

    def test_sqrt_negative(self):
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.sqrt(-4)