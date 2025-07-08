# def a(lst):
#     count = 0
#     for i in lst:
#         if i < 0:
#             count += 1
#     return count
#
#
# print(a([-2, 3, 8, -11, -4, 6]))


def negative(n):
    if len(n) == 0:
        return 0
    count = 0  # 1 0 0 1 1 0
    if n[0] < 0:
        count += 1
    return count + negative(n[1:])


lst = [-2, 3, 8, -11, -4, 6]
print(negative(lst))