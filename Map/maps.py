# Write a program that maps a list of words 
# into a list of integers representing the lengths of the correponding words.

def map_list(get_list):
    """Returns a list of lengths of elements in input list"""
    
    if type(get_list) != list or len(get_list) == 0 or get_list is None:
        return False
    
    int_list = []
    
    for i in get_list:
        if type(i) != str:
            return False
        else:
            int_list.append(len(i))
        
    return int_list

def main():
    
    word_list = input("Enter a list of words: ")
    
    print map_list(word_list)

if __name__ == "__main__":
    main()