class Polynomial():
    def __init__(self, coefficients, var="x"):
        """The variable coefficients is a list of elements from a field and the
        var variable represents the variable of the polynomial.

        Note that it is assumed that the coefficient's position in the list
        corresponds to the power that it is associated with.

        For example, [1, 2, 3] represents the polynomial 1x^0 + 2x^1 + 3x^2.
        """
        self.var = var
        self.coefficients = self._simplify(coefficients)

    def __add__(self, other):
        addition = self.coefficients[:]
        if len(self.coefficients) < len(other.coefficients):
            difference = len(other.coefficients) - len(self.coefficients)
            addition += [0 for x in range(difference)]
        for i, coefficient in enumerate(other.coefficients):
            addition[i] += coefficient

        return Polynomial(self._simplify(addition), self.var)

    def __sub__(self, other):
        subtraction = self.coefficients[:]
        if len(self.coefficients) < len(other.coefficients):
            difference = len(other.coefficients) - len(self.coefficients)
            subtraction += [0 for x in range(difference)]
        for i, coefficient in enumerate(other.coefficients):
            subtraction[i] -= coefficient

        return Polynomial(self._simplify(subtraction), self.var)

    def __mul__(self, other):
        degree = len(self.coefficients) + len(other.coefficients)
        multiplication = [0 for x in range(degree)]

        for i, x in enumerate(self.coefficients):
            for j, y in enumerate(other.coefficients):
                multiplication[i + j] += x * y

        return Polynomial(self._simplify(multiplication), self.var)

    def __eq__(self, other):
        if self.coefficients == other.coefficients:
            return True
        else:
            return False

    def __call__(self, value):
        return sum([coefficient * (value ** i) for i, coefficient
                    in enumerate(self.coefficients)])

    def __repr__(self):
        return str(self.coefficients)

    def __str__(self):
        strings = ["{0}{1}^{2}".format(coefficient, self.var, i)
                   for i, coefficient in enumerate(self.coefficients)]
        return " + ".join(strings)

    def scalar(self, element):
        """
        Performs scalar multiplication on polynomial by the variable element.

        Alters self.coefficients of the Polynomial instance by
        multiplying each entry of self.coefficients by element.
        """
        self.coefficients = [c * element for c in self.coefficients]

    def _simplify(self, coefficients):
        """The variable coefficients is a list of coefficients from a field.

        This function removes the extraneous zeroes at the end of the list
        coefficients. We do this so that we can compare [1,2,0] and [1,2], two
        equivalent polynomial representations, by just inspecting the lists.
        """

        while coefficients[-1] == 0:
            coefficients.pop()
            if not coefficients:
                coefficients = [0]
                break

        return coefficients
