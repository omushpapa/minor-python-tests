# Write a function is_member() that takes a value 
# (i.e. a number, string, etc) x and a list of values a, 
# and returns True if x is a member of a, False otherwise. 
# (Note that this is exactly what the in operator does, 
# but for the sake of the exercise you should pretend Python did not have this operator.)

def is_member(value, get_list):
    """Checks if value is a member of get_list"""
    
    new_list = [str(i) for i in get_list]   # Convert list elements to string
    
    for x in new_list:
        if str(value) == x:
            return True
        
    return False

def main():
    
    user_list = input("Enter list: ")
    
    user_value = raw_input("Enter value: ")
    
    print check_member(user_value, user_list)

if __name__ == "__main__":
    main()
