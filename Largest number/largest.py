# The function max() from exercise 1) and 
# the function max_of_three() from exercise 2) will only work 
# for two and three numbers, respectively. 
# But suppose we have a much larger number of numbers, 
# or suppose we cannot tell in advance how many they are? 
# Write a function max_in_list() that takes a list of numbers and 
# returns the largest one.

def max_in_list(num_list):
    
    return sorted(num_list)[-1]

def verify(int_list):
    """Check if list is appropriate"""
        
    int_list = list(int_list)
    
    if len(int_list) == 0:
        return False
    
    for i in int_list:
        if type(i) != int:
            return False
    
    return True

def main():
    
    get_list = input("Enter list of numbers: ")
    
    if (
        type(get_list) == int or 
        type(get_list) == None or 
        get_list == ""
        ):  
            
        print get_list
    elif verify(get_list):
        
        print max_in_list(get_list)
    else:
        
        print False
    
if __name__ == "__main__":
    main()