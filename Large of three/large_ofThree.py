#!/usr/bin/env python2
#encoding: UTF-8

# Define a function max_of_three() 
# that takes three numbers as arguments 
# and returns the largest of them.

def max_of_three(num1, num2, num3):
    if type(num1) is not int or type(num2) is not int or type(num3) is not int:
        return False
    num_list = [num1, num2, num3]
    temp = 0
    
    if num1 == num2 == num3:
        return num3
    
    for i in range(len(num_list) - 1):
        if num_list[i] < num_list[i + 1]:
            temp = num_list[i + 1]
    return temp

def main():
    value1 = input("Enter first value: ")
    value2 = input("Enter second value: ")
    value3 = input("Enter third value: ")
    
    print max_of_three(value1, value2, value3)
    

if __name__ == "__main__":
    print "Hello World"
