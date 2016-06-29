#!/usr/bin/env python2
#encoding: UTF-8

# Write a function that takes a character 
# (i.e. a string of length 1) and 
# returns True if it is a vowel, False otherwise.

def is_vowel(value):
    
    if type(value) is not str:
        return False
    
    if len(value) > 1 or len(value) <= 0:
        return False
    
    vowels = ['a', 'e', 'i', 'o' , 'u']
    
    if value in vowels:
        return True
    else:
        return False
    
def main():
    
    print is_vowel(raw_input("Enter a character: "))    

if __name__ == "__main__":
    main()
