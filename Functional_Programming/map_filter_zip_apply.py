#!/usr/bin/env python3


list(map(lambda x: x*x, range(10)))
list(map(lambda x,y: x*y, range(10), range(20,30)))

w1="EPAM"
w2="GOOD"

list(zip(range(len(w1)),w1,w2))

list(filter(lambda x: x%2, range(100)))
