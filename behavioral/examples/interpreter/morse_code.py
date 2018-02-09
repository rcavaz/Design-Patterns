import re


class Context(object):
    def __init__(self, morse):
        self._input = morse
        self._output = ''

    def __str__(self):
        return self._output

    def morse(self, txt=None):
        if txt is None:
            return self._input
        else:
            self._input = txt

    def abc(self, txt=None):
        if txt is None:
            return self._output
        else:
            self._output = txt


class AbstractExpression(object):
    def interpret(self, context):
        # If end of message
        if len(context.morse()) == 0:
            context.abc(context.abc() + self.char())
        # If current is a single blank
        elif re.match(' ', context.morse()):
            # If current is a double blank
            if re.match('  ', context.morse()):
                context.morse(context.morse()[2:])
                context.abc(context.abc() + self.char())
            else:
                context.morse(context.morse()[1:])
                context.abc(context.abc() + self.char())
        # If current is a dot
        elif re.match('\.', context.morse()):
            context.morse(context.morse()[1:])
            self.left().interpret(context)
        # If current is a dash
        elif re.match('-', context.morse()):
            context.morse(context.morse()[1:])
            self.right().interpret(context)
        else:
            raise Exception('Syntax error')

    def left(self):
        raise NotImplementedError

    def right(self):
        raise NotImplementedError

    def char(self):
        raise NotImplementedError


class TerminalExpression(AbstractExpression):
    def __init__(self, char='<?>'):
        self._char = char

    def char(self):
        return self._char

    def left(self):
        return self

    def right(self):
        return self


class NonterminalExpression(AbstractExpression):
    def __init__(self, **args):
        self._left  = args['dot']  if 'dot'  in args else TerminalExpression()
        self._right = args['dash'] if 'dash' in args else TerminalExpression()
        self._char  = args['char'] if 'char' in args else TerminalExpression()

    def left(self, node=None):
        if node is None:
            return self._left
        else:
            self._left = node

    def right(self, node=None):
        if node is None:
            return self._right
        else:
            self._right = node

    def char(self):
        return self._char.char()


class Client(object):
    def main(self):
        message = '... --- ...'
        context = Context(message)

        # Create chars
        a = TerminalExpression('a')
        b = TerminalExpression('b')
        c = TerminalExpression('c')
        d = TerminalExpression('d')
        e = TerminalExpression('e')
        f = TerminalExpression('f')
        g = TerminalExpression('g')
        h = TerminalExpression('h')
        i = TerminalExpression('i')
        j = TerminalExpression('j')
        k = TerminalExpression('k')
        l = TerminalExpression('l')
        m = TerminalExpression('m')
        n = TerminalExpression('n')
        o = TerminalExpression('o')
        p = TerminalExpression('p')
        q = TerminalExpression('q')
        r = TerminalExpression('r')
        s = TerminalExpression('s')
        t = TerminalExpression('t')
        u = TerminalExpression('u')
        v = TerminalExpression('v')
        w = TerminalExpression('w')
        x = TerminalExpression('x')
        y = TerminalExpression('y')
        z = TerminalExpression('z')
        #null = TerminalExpression('<?>')
        blank = TerminalExpression(' ')

        # Build the abstract syntax tree
        #n30 = NonterminalExpression()
        #n29 = NonterminalExpression()
        n28 = NonterminalExpression(char=q)
        n27 = NonterminalExpression(char=z)
        n26 = NonterminalExpression(char=y)
        n25 = NonterminalExpression(char=c)
        n24 = NonterminalExpression(char=x)
        n23 = NonterminalExpression(char=b)
        n22 = NonterminalExpression(char=j)
        n21 = NonterminalExpression(char=p)
        #n20 = NonterminalExpression()
        n19 = NonterminalExpression(char=l)
        #n18 = NonterminalExpression()
        n17 = NonterminalExpression(char=f)
        n16 = NonterminalExpression(char=v)
        n15 = NonterminalExpression(char=h)
        n14 = NonterminalExpression(char=o)
        n13 = NonterminalExpression(char=g, dot=n27, dash=n28)
        n12 = NonterminalExpression(char=k, dot=n25, dash=n26)
        n11 = NonterminalExpression(char=d, dot=n23, dash=n24)
        n10 = NonterminalExpression(char=w, dot=n21, dash=n22)
        n9  = NonterminalExpression(char=r, dot=n19)
        n8  = NonterminalExpression(char=u, dot=n17)
        n7  = NonterminalExpression(char=s, dot=n15, dash=n16)
        n6  = NonterminalExpression(char=m, dot=n13, dash=n14)
        n5  = NonterminalExpression(char=n, dot=n11, dash=n12)
        n4  = NonterminalExpression(char=a, dot=n9, dash=n10)
        n3  = NonterminalExpression(char=i, dot=n7, dash=n8)
        n2  = NonterminalExpression(char=t, dot=n5, dash=n6)
        n1  = NonterminalExpression(char=e, dot=n3, dash=n4)
        root = NonterminalExpression(char=blank, dot=n1, dash=n2)

        while len(context.morse()) > 0:
            root.interpret(context)

        print '%s = %s' % (message, context.abc())


if __name__ == '__main__':
    c = Client()
    c.main()
