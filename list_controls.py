#!/usr/bin/env python2
#encoding: UTF-8

# Define a function sum() and a function multiply() 
# that sums and multiplies (respectively) all the numbers in a list of numbers. 
# For example, sum([1, 2, 3, 4]) should return 10, and 
# multiply([1, 2, 3, 4]) should return 24.

def sum(value):
    
    if type(value) is not list:
        return False
    
    summation = 0
    
    for i in value:
        if type(i) is not int:
            return False
        summation = summation + i
        
    return summation

def multiply(value):
    
    if type(value) is not list:
        return False
    
    result = 1
    
    for i in value:
        if type(i) is not int:
            return False
        result = result * i
        
    return result

def main():
    
    ans = input("Enter values in list: ")
    
    print sum(ans)
    print multiply(ans)

if __name__ == "__main__":
    main()
