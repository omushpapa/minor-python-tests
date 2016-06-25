#!/usr/bin/env python2
#encoding: UTF-8

# Define a function that computes the length of a given list or string. 
# (It is true that Python has the len() function built in, 
# but writing it yourself is nevertheless a good exercise.)

def string_length(string):
    
    if string == None:
        return False
    
    if type(string) is not str and type(string) is not list:
        return False
    
    value = 0
    
    for i in string:
        value = value + 1
    
    return value

def main():
    
    get_input = raw_input("Enter a value: ")
    
    print string_length(get_input)

if __name__ == "__main__":
    main()