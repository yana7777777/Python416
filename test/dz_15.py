from math import pi

# print((lambda b: pi * (b ** 2))(2))
#
# print((lambda a, b: a * b)(10, 13))
#
# print((lambda a, b, h: (a + b) / 2 * h)(7, 5, 3))


exp = {
    'Circle': lambda b: pi * b ** 2,
    'Rectangle': lambda a, b: a * b,
    'Trapezoid': lambda a, b, h: (a + b) / 2 * h
}

print(exp['Circle'](2))
print(exp['Rectangle'](10, 13))
print(exp['Trapezoid'](7, 5, 3))
