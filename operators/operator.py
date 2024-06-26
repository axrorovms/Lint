from ast import USub, Add, Sub


class Constant:
    __match_args__ = ('value',)
    def __init__(self, value):
        self.value = value


class UnaryOp:
    __match_args__ = ("op", "value")

    def __init__(self, op, value):
        self.op = op
        self.value = value


class Call:
    __match_args__ = ("func", "args")

    def __init__(self, func, args):
        self.func = func
        self.args = args


class Name:
    __match_args__ = ("id",)

    def __init__(self, id):
        self.id = id


class BinOp:
    __match_args__ = ("first_value", "op", "second_value")

    def __init__(self, first_value, op, second_value):
        self.first_value = first_value
        self.op = op
        self.second_value = second_value



class Module:
    __match_args__ = ("body",)

    def __init__(self, body):
        self.body = body


neg_eight = UnaryOp(USub(), Constant(8))

read = Call(Name('input_int'), [])

ast1_1 = BinOp(read, Add(), neg_eight)

