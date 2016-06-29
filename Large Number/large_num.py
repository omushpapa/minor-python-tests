#!/usr/bin/env python2
#encoding: UTF-8

# Define a function max() that takes two numbers as arguments 
# and returns the largest of them. 
# Use the if-then-else construct available in Python. 
# (It is true that Python has the max() function built in, 
# but writing it yourself is nevertheless a good exercise.)

def max(num1, num2):
    if type(num1) is not int or type(num2) is not int:
        return False
    if num1 == num2:
        return "Equal"
    if num1 > num2:
        return num1
    if num2 > num1:
        return num2
    
def main():
    first_value = input("Enter first number: ")
    second_value = input("Enter second number: ")
    print max(first_value, second_value)
    
if __name__ == "__main__":
    main()