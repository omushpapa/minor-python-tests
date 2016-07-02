# Write a function find_longest_word() 
# that takes a list of words and 
# returns the length of the longest one.

def find_longest_word(string):
    new_string = filter(lambda x: type(x) == str and x != '', string)
    
    if not new_string:
        return False
    else:
        return reduce((lambda x, y: x if len(x)>len(y) else y), new_string)

def main():
    get_string = input("Enter list of strings: ")
    
    print find_longest_word(get_string)

if __name__ == "__main__":
    main()