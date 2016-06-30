# Define a function overlapping() that takes two lists 
# and returns True if they have at least one member in common, False otherwise. 
# You may use your is_member() function, or the in operator, 
# but for the sake of the exercise, you should (also) write it using 
# two nested for-loops.

from membership import is_member

def overlapping(first_list, second_list):
    """Find common element between two lists"""
    
    for i in first_list:
        return is_member(i, second_list)

def main():
    
    list_one = input("Enter first list: ")
    
    list_two = input("Enter second list: ")
    
    print overlapping(list_one, list_two)

if __name__ == "__main__":
    main()