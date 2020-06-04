#!/usr/bin/env python3

# https://automated-testing.info/t/neochevidnye-vozmozhnosti-pythona-kotorye-mozhno-vstretit-na-sobesedovanii/12417

from functools import reduce


# fib

fib1 = lambda n: [(lambda: (l[-1], l.append(l[-1] + l[-2]))[0])() for l in [[1, 1]] for x in range(n+1)]
fib2 = lambda n: [(l[-1], l.append(l[-1] + l[-2]))[0] for l in [[1, 1]] for x in range(n+1)]
fib3 = lambda n: [l.append(l[-1] + l[-2]) or l for l in [[1, 1]] for x in range(n)][0][1:]
fib4 = lambda n: reduce(lambda a, b: a + [a[-1] + a[-2]], range(n), [1, 1])[1:]
fib5 = lambda n: reduce(lambda a, b: a.append(a[-1] + a[-2]) or a, range(n), [1, 1])[1:]

print(fib1(12))
print(fib2(12))
print(fib3(12))
print(fib4(12))
print(fib5(12))
