# Write a program that maps a list of words 
# into a list of integers representing the lengths of the correponding words.

def main():
    
    word_list = input("Enter a list of strings: ")
    
    if type(word_list) != list or len(word_list) == 0 or word_list is None:
        print False
    else:
        print map(lambda x: len(x), word_list)

if __name__ == "__main__":
    main()