# Define a function is_palindrome() that recognizes 
# palindromes (i.e. words that look the same written backwards).
# For example, is_palindrome("radar") should return True.

def reverse(string):
    if string == string[::-1]:
        return True
    else:
        return False

def main():
    word = raw_input("Enter string: ")
    
    print reverse(word)
    
if __name__ == "__main__":
    main()
