# Define a function reverse() 
# that computes the reversal of a string. 
# For example, reverse("I am testing") 
# should return the string "gnitset ma I".

def reverse(string):
    return string[::-1]

def main():
    word = raw_input("Enter string: ")
    
    print reverse(word)
    
if __name__ == "__main__":
    main()
