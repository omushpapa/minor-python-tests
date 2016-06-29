#!/usr/bin/env python2
#encoding: UTF-8

# Write a function translate() that will translate a text into "rövarspråket" 
# (Swedish for "robber's language"). 
# That is, double every consonant and 
# place an occurrence of "o" in between. 
# For example, translate("this is fun") 
# should return the string "tothohisos isos fofunon".

def rob_string(string):
    
    if type(string) is not str:
        return False
    
    
    if len(string) < 1:
        return False
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    last_word = ''
    
    for i in string:
        if i.isdigit():
            return False
        elif i not in vowels and i != ' ':
            temp = i + 'o' + i
        else:
            temp = i
        last_word = last_word + temp
        
    return last_word

def main():
    
    print rob_string(raw_input("Enter a string: "))
    

if __name__ == "__main__":
    main()