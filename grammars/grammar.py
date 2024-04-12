from _ast import Expr

from operators.operator import (Constant, Call, UnaryOperator, BinaryOp,
                                Add, USub, Sub, Name, Module, read, ast1_1)


def is_exp(e):
    match e:
        case Constant(value=n):
            return True
        case Call(func=Name(id='input_int'), args=[]):
            return True
        case UnaryOperator(op=USub(), value=e1):
            return is_exp(e1)
        case BinaryOp(first_value=e1, op=Add(), second_value=e2):
            return is_exp(e1) and is_exp(e2)
        case BinaryOp(first_value=e1, op=Sub(), second_value=e2):
            return is_exp(e1) and is_exp(e2)
        case _:
            return False


def is_stmt(s):
    match s:
        case Expr(Call(func=Name(id='print'), args=[e])):
            return is_exp(e)
        case Expr(e):
            return is_exp(e)
        case _:
            return False


def is_Lint(p):
    match p:
        case Module(body=body):
            return all([is_stmt(s) for s in body])
        case _:
            return False


print(is_Lint(Module([Expr(ast1_1)])))
print(is_Lint(Module([Expr(BinaryOp(read, Sub(), UnaryOperator(Add(), Constant(8))))])))