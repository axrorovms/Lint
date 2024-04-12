from _ast import Expr

from operators.operator import (Constant, Call, UnaryOp, BinOp,
                                Add, USub, Sub, Name, Module)
from utils import input_int, add64, sub64, neg64


def interp_exp(e):
    match e:
        case BinOp(left, Add(), right):
            l = interp_exp(left);
            r = interp_exp(right)
            return add64(l, r)
        case BinOp(left, Sub(), right):
            l = interp_exp(left);
            r = interp_exp(right)
            return sub64(l, r)
        case UnaryOp(USub(), v):
            return neg64(interp_exp(v))
        case Constant(value):
            return value
        case Call(Name('input_int'), []):
            return input_int()


def interp_stmt(s):
    match s:
        case Expr(Call(Name('print'), [arg])):
            print(1)

            print(interp_exp(arg))
        case Expr(value):
            interp_exp(value)


def interp_Lint(p):
    match p:
        case Module(body=body):
            for s in body:
                interp_stmt(s)


if __name__ == "__main__":
    eight = Constant(8)
    neg_eight = UnaryOp(USub(), eight)
    read = Call(Name('input_int'), [])
    ast1_1 = BinOp(read, Add(), neg_eight)
    interp_Lint(Module([Expr(Call(Name('print'), [ast1_1]))]))
