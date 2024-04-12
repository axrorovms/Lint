################################################################################
# Auxiliary Functions
################################################################################

# signed 64-bit arithmetic

min_int64 = -(1 << 63)

max_int64 = (1 << 63) - 1

mask_64 = (1 << 64) - 1

offset_64 = 1 << 63


def to_unsigned(x):
    return x & mask_64


def to_signed(x):
    return ((x + offset_64) & mask_64) - offset_64


def add64(x, y):
    return to_signed(x + y)


def sub64(x, y):
    return to_signed(x - y)


def mul64(x, y):
    return to_signed(x * y)


def neg64(x):
    return to_signed(-x)


def xor64(x, y):
    return to_signed(x ^ y)


def is_int64(x) -> bool:
    return isinstance(x, int) and (x >= min_int64 and x <= max_int64)


def input_int() -> int:
    x = int(input())
    x = min(max_int64, max(min_int64, x))
    return x
