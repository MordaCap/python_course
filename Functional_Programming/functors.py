#!/usr/bin/env python3

# Python code to illustrate program
# using functors
 
class Functor(object):
    def __init__(self, n=10):
        self.n = n
            
    # This construct allows objects to be called as functions in python
    def __call__(self, x) :
        x_first = x[0]
        if type(x_first) is int:
            return self. __MergeSort(x)
        if type(x_first) is float:
            return self. __HeapSort(x)
        else :
            return self.__QuickSort(x) 
 
    def __MergeSort(self,a):
        #" Dummy MergeSort "
        print("Data is Merge sorted")
        return a
    def __HeapSort(self,b):
        # " Dummy HeapSort "
        print("Data is Heap sorted")
        return b
    def __QuickSort(self,c):
        #  "Dummy QuickSort"
        print("Data is Quick sorted")
        return c
 

# Now let's code the class which will call the above functions.
# Without the functor this class should know which specific function to be called 
# based on the type of input
 
### USER CODE
class Caller(object):
    def __init__(self):
        self.sort=Functor()
     
    def Dosomething(self,x):
# Here it simply calls the function and doesn't need to care about
# which sorting is used. It only knows that sorted output will be the 
# result of this call
        return self.sort(x)

 
Call=Caller()
 
# Here passing different input
print(Call.Dosomething([5,4,6])) # Mergesort
 
print(Call.Dosomething([2.23,3.45,5.65])) # heapsort
print(Call.Dosomething(['a','s','b','q'])) # quick sort
# creating word vocab
