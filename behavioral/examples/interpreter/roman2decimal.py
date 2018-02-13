import re


class Context(object):
    def __init__(self, roman):
        self._roman = roman
        self._decimal = 0

    def roman(self, number=None):
        if number is None:
            return self._roman
        else:
            self._roman = number

    def decimal(self, number=None):
        if number is None:
            return self._decimal
        else:
            self._decimal = number


class AbstractExpression(object):
    def interpret(self, context):
        if len(context.roman()) == 0:
            return

        if re.match(self.nine(), context.roman()):
            context.decimal(context.decimal() + (9 * self.multiplier()))
            context.roman(context.roman()[2:])
        elif re.match(self.four(), context.roman()):
            context.decimal(context.decimal() + (4 * self.multiplier()))
            context.roman(context.roman()[2:])
        elif re.match(self.five(), context.roman()):
            context.decimal(context.decimal() + (5 * self.multiplier()))
            context.roman(context.roman()[1:])

        while re.match(self.one(), context.roman()):
            context.decimal(context.decimal() + (1 * self.multiplier()))
            context.roman(context.roman()[1:])

    def one(self):
        raise NotImplementedError()

    def four(self):
        raise NotImplementedError()

    def five(self):
        raise NotImplementedError()

    def nine(self):
        raise NotImplementedError()

    def multiplier(self):
        raise NotImplementedError()



class ThousandExpression(AbstractExpression):
    def one(self):  return 'M'
    def four(self): return ' '
    def five(self): return ' '
    def nine(self): return ' '
    def multiplier(self): return 1000


class HundredExpression(AbstractExpression):
    def one(self):  return 'C'
    def four(self): return 'CD'
    def five(self): return 'D'
    def nine(self): return 'CM'
    def multiplier(self): return 100


class TenExpression(AbstractExpression):
    def one(self):  return 'X'
    def four(self): return 'XL'
    def five(self): return 'L'
    def nine(self): return 'XC'
    def multiplier(self): return 10


class BaseExpression(AbstractExpression):
    def one(self):  return 'I'
    def four(self): return 'IV'
    def five(self): return 'V'
    def nine(self): return 'IX'
    def multiplier(self): return 1


class Client(object):
    def main(self):
        roman = 'MCMLXXXVII'
        context = Context(roman)

        # Build the Abstract Syntax Tree
        tree = list()
        tree.append(ThousandExpression())
        tree.append(HundredExpression())
        tree.append(TenExpression())
        tree.append(BaseExpression())

        for i in tree:
            i.interpret(context)

        print '%s = %s' % (roman, context.decimal())


if __name__ == '__main__':
    c = Client()
    c.main()
