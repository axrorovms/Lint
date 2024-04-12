from _ast import Expr

from operators.operator import (Constant, Call, UnaryOp, BinOp,
                                Add, USub, Sub, Name, Module)
from utils import input_int, add64, sub64, neg64


def interp_exp(e):
    match e:
        case BinOp(first_value=left, op=Add(), second_value=right):
            l = interp_exp(left)
            r = interp_exp(right)
            return add64(l, r)
        case BinOp(first_value=left, op=Sub(), second_value=right):
            l = interp_exp(left)
            r = interp_exp(right)
            return sub64(l, r)
        case UnaryOp(op=USub(), value=v):
            return neg64(interp_exp(v))
        case Constant(value=value):
            return value
        case Call(func=Name('input_int'), args=[]):
            return input_int()
        case _:
            raise Exception('error in interp_exp, unexpected ' + repr(e))


def interp_stmt(s):
    match s:
        case Expr(Call(Name('print'), [arg])):
            print(interp_exp(arg))
        case Expr(value):
            interp_exp(value)
        case _:
            raise Exception('error in interp_stmt, unexpected ' + repr(s))


def interp(p):
    match p:
        case Module(body=body):
            for s in body:
                interp_stmt(s)
        case _:
            raise Exception('error in interp, unexpected ' + repr(p))


if __name__ == "__main__":
    eight = Constant(8)
    neg_eight = UnaryOp(USub(), eight)
    read = Call(Name('input_int'), [])
    ast1_1 = BinOp(read, Add(), neg_eight)
    pr = Expr(Call(Name('print'), [ast1_1]))
    p = Module([pr])
    interp(p)
