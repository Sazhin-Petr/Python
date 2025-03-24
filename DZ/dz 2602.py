# def rect_peral(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(rect_peral(2, 4, 6))
# print(rect_peral(5, 8, 2))
# print(rect_peral(1, 6, 8))

# локальная переменная

# def rect_peral(a, b, c):
#     def inner(i, j, k):
#         s = 2 * (i * j + i * k + j * k)
#         return s
#
#     area = inner(a, b, c)
#
#     return area
#
#
# print(rect_peral(2, 4, 6))
# print(rect_peral(5, 8, 2))
# print(rect_peral(1, 6, 8))


#  нелокальная переменная

def rect_peral(a, b, c):
    s = None

    def inner(i, j):
        nonlocal s
        s += i * j

    inner(a, b)
    inner(a, c)
    inner(b, c)

    s = 2 * s
    return s


print(rect_peral(2, 4, 6))
print(rect_peral(5, 8, 2))
print(rect_peral(1, 6, 8))


def rect_peral(a, b, c):
    s = None

    def inner():
        nonlocal s
        s = 2 * (a * b + a * c + b * c)

    inner()
    return s


print(rect_peral(2, 4, 6))
print(rect_peral(5, 8, 2))
print(rect_peral(1, 6, 8))