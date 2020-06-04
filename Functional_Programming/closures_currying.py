#!/usr/bin/env python3

from functools import partial

def mult1(x):
  def mult(y):
    return x*y
  return mul


mult1 = lambda x: lambda y: x*y

def mult2(x,y):
  return x*y

mult3 = lambda x: partial(mult2,x)

print(mult1(4)(5))
print(mult2(4, 5))
print(mult3(4)(5))


talk_to = lambda first_word: lambda name: lambda emotion: first_word+" "+name+emotion

greet = talk_to("Hello")
bye = talk_to("Good Bye")

print(greet("Rasul")("!!!"))
print(bye("Rasul")("... :("))


def multiplier( n ):    # замыкания - closure
    def mul( k ):
        return n * k
    return mul

 
mul3 = multiplier( 3 )
 
from functools import partial
def mulPart( a, b ):    # частичное применение функции
    return a * b

 
par3 = partial( mulPart, 3 )
 
class mulFunctor:       # эквивалентный функтор
    def __init__( self, val1 ):
        self.val1 = val1
    def __call__( self, val2 ):
        return self.val1 * val2

 
fun3 = mulFunctor( 3 )
 
print( '{} . {} . {}'.format( mul3( 5 ), par3( 5 ), fun3( 5 ) ) )






