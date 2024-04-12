from _ast import Expr

from operators.operator import (Constant, Call, UnaryOp, BinOp,
                                Add, USub, Sub, Name, Module)
from utils import add64, sub64, neg64


def pe_neg(r):
    match r:
        case Constant(n):
            return Constant(neg64(n))
        case _:
            return UnaryOp(USub(), r)


def pe_add(r1, r2):
    match (r1, r2):
        case (Constant(n1), Constant(n2)):
            return Constant(add64(n1, n2))
        case _:
            return BinOp(r1, Add(), r2)


def pe_sub(r1, r2):
    match (r1, r2):
        case (Constant(n1), Constant(n2)):
            return Constant(sub64(n1, n2))
        case _:
            return BinOp(r1, Sub(), r2)


def pe_exp(e):
    match e:
        case BinOp(left, Add(), right):
            return pe_add(pe_exp(left), pe_exp(right))
        case BinOp(left, Sub(), right):
            return pe_sub(pe_exp(left), pe_exp(right))
        case UnaryOp(USub(), v):
            return pe_neg(pe_exp(v))
        case Constant(value):
            return e
        case Call(Name('input_int'), []):
            return e


def pe_stmt(s):
    match s:
        case Expr(Call(Name('print'), [arg])):
            return Expr(Call(Name('print'), [pe_exp(arg)]))
        case Expr(value):
            return Expr(pe_exp(value))


def pe_P_int(p):
    match p:
        case Module(body):
            new_body = [pe_stmt(s) for s in body]
            return Module(new_body)
