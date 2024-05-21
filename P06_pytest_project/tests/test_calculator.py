from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a,b)

        # assert
        expected = 5555
        assert result == expected

    def test_minus(self):
        a = 10
        b = 5
        cal = Calculator()
        result = cal.subtract(a,b)
        expected = 5
        assert result == expected
    
    def test_multiply(self):
        a = 10
        b = 5
        cal = Calculator()
        result = cal.multiply(a,b)
        expected = 50
        assert result == expected

    def test_divide(self):
        a = 10
        b = 5
        cal = Calculator()
        result = cal.divide(a,b)
        expected = 2
        assert result == expected

    def test_divide_zero(self):
        a = 10
        b = 0
        cal = Calculator()
        try:
            result = cal.divide(a,b)
        except ZeroDivisionError:
            assert True
