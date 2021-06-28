#!/usr/bin/env python3
import re
import sys


class PolynomialOld(object):

    def __init__(self, *args, **kwargs):
        if not args and not kwargs:
            exit(1)
        if args and isinstance(args[0], list):
            self.nums = args[0]
        elif args:
            self.nums = list(args)
        else:
            list_of_nums = []
            list_for_max = []

            # zjistim si jakeho stupne je polynom
            for key in kwargs:
                key_cutted = key[1:]
                to_append = key_cutted
                list_for_max.append(to_append)

            # doplnim si nuly na mista clenu kteri v polynomu nejsou
            for i in range(int(max(list_for_max)) + 1):
                for member in ['x' + str(i)]:
                    list_of_nums.append(kwargs.get(member, 0))
            # ukladam seznam koeficientu
            self.nums = list(list_of_nums)
        self.length = len(self.nums)

    def __str__(self):
        if self.length == 0:
            return "0"

        expression_list = []
        if self.nums[0] != 0:
            if self.nums[0] > 0:
                expression_list.append(" + " + str(self.nums[0]))
            else:
                expression_list.append(str(self.nums[0]))

        for i in range(self.length):
            if self.nums[i] != 0:
                if self.nums[i] < 0:
                    expression_list.append(str(self.nums[i]) + (
                            "x^" + str(i) if i > 1 else "x"))
                else:
                    expression_list.append(" + " + str(self.nums[i]) + (
                            "x^" + str(i) if i > 1 else "x"))

        expression_str = ''.join(expression_list[::-1]).replace('-', ' - ')
        expression_str = re.sub('^ [+] ', '', expression_str)
        expression_str = re.sub('1x', 'x', expression_str)

        if len(expression_str) == 0:
            return "0"

        return expression_str

    # srovnani dvou polynomu
    def __eq__(self, other):
        return self.nums == other.nums

    # secteni polynomu
    def __add__(self, other):
        added_polynoms = [0] * max(self.length, other.length)

        # nactu si prvni polynom
        for i in range(0, self.length):
            added_polynoms[i] = (added_polynoms[i] + self.nums[i])
        # pricitam k nemu druhy polynom
        for i in range(0, other.length):
            added_polynoms[i] = (added_polynoms[i] + other.nums[i])

        # vracim objekt tridy Polynomial
        return Polynomial(added_polynoms)

    def __mul__(self, other):
        # seznam muze mit 2x velikost polynomu, kazdy neabsolutni clen vyusti ve dva
        # plus pokud je pritomen absolutni clen, tak ten se zpropaguje jen na vysledny jeden proto -1
        multiplicated_pols = [0] * (2 * self.length - 1)

        for i in range(0, self.length):
            for j in range(0, other.length):
                multiplicated_pols[i + j] = multiplicated_pols[i + j] + (
                        self.nums[i] * other.nums[j])
        # vracim objekt tridy Polynomial
        return Polynomial(multiplicated_pols)

    def __pow__(self, pow):
        # cokoli na nultou je 1
        if pow == 0:
            return 1
        # neco na prvou je to neco
        if pow == 1:
            return self
        # cyklem se provede potrebny pocet nasobeni
        result = self
        for i in range(0, pow - 1):
            result = result * self

        return result

    def at_value(self, value1, value2=None):
        if value2 is None:
            result = self.nums[0]
            for i in range(1, self.length):
                if self.nums[i] != 0:
                    result += (value1**i) * self.nums[i]
            return result

        else:
            result1 = self.nums[0]
            for i in range(1, self.length):
                if self.nums[i] != 0:
                    result1 += (value1**i) * self.nums[i]

            result2 = self.nums[0]
            for i in range(1, self.length):
                if self.nums[i] != 0:
                    result2 += (value2**i) * self.nums[i]

            return result2 - result1

    def derivative(self):
        derivation = []

        for i in range(1, self.length):
            derivation.append(int(i * self.nums[i]))
        return Polynomial(derivation)


class Polynomial:
    """
    Class Polynomial represents general mathematical polynomial.
    Polynomial object can be instantiated from the list, dictionary or
    keys with values. Class implements many useful magic methods as
    addition, comparison, multiplication and power. Also __str__ method
    for user readable representation of self.
    On top of these methods, there are two more instance methods:
      - at_point(), which evaluates the polynomial value at the given
            point, and
      - derivative(), which returns a derivative of the polynomial.

    input_pol: list, dict, kwargs - keys with values (dict)
    """

    pol_members = []
    length = 0

    def __init__(self, *args, **kwargs):
        if not args and not kwargs:
            exit(1)
        if args and isinstance(args[0], list):
            self.pol_members = args[0]
        elif args and isinstance(args[0], dict):
            # TODO
            self.pol_members = list(args)

        # Make a list from kwargs
        else:
            orders = lambda pol: [int(x[1:]) for x in pol]
            max_order = max(orders(kwargs))
            self.pol_members = [0] * (max_order + 1)

            for key in kwargs:
                key_order = int(key[1:])
                self.pol_members[key_order] = kwargs.get(key)

        self.length = len(self.pol_members)

    def __str__(self):
        print(self.pol_members)
        pol_reversed = self.pol_members.copy()
        pol_reversed.reverse()
        if self.length <= 1:
            return str(pol_reversed[0])

        # TODO napred pripravit, pak pridat znamenka, pak slozit dohromady
        else:
            result = [f'{pol_reversed[0]}x^{self.length-1}']
        for order, x in zip(reversed(range(self.length - 1)), pol_reversed[1:]):
            if x == self.length:
                result.append(x)
            if x == 0:
                continue
            elif order < 0:
                result.append(f' - {x}x^{order}')
            else:
                result.append(f' + {x}x^{order}')
        return ''.join(result)

    def __eq__(self, other):
        return self.pol_members == other.pol_members

    def __add__(self, other):
        ...

    def __mul__(self, other):
        ...

    def __pow__(self, pow):
        ...

    def at_value(self, value1, value2=None):
        ...

    def derivative(self):
        ...


if __name__ == '__main__':
    pol1 = Polynomial(x1=5, x2=2, x5=1, x4=2, x0=8)
    pol2 = Polynomial(x1=5, x2=2, x5=1, x4=2, x0=8)
    print(pol1 == pol2)

