import pytest

from app.Calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(1, 2) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def test_division_success(self):
        assert self.calc.division(6, 3) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(6, 3) == 3

    def test_multiply_success(self):
        assert self.calc.multiply(6, 3) == 18

    def teardown(self):
        print('Выполнение метода teardown')
