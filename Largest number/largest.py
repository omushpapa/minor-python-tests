# The function max() from exercise 1) and 
# the function max_of_three() from exercise 2) will only work 
# for two and three numbers, respectively. 
# But suppose we have a much larger number of numbers, 
# or suppose we cannot tell in advance how many they are? 
# Write a function max_in_list() that takes a list of numbers and 
# returns the largest one.

def max_in_list(num_list):
    
    if verify(num_list):
        if type(num_list) == int:
            return num_list
        
        if len(num_list) == 1:
            return num_list[0]
        
        temp = None

        for i in range(len(num_list) - 1):
            if num_list[i + 1] > num_list[i]:
                temp = num_list[i + 1]

        return temp 
    
    else:
        return False

def verify(int_list):
    """Check if list is appropriate"""
    
    if type(int_list) == int:
        return True
    
    int_list = list(int_list)
    
    if len(int_list) == 0:
        return False
    
    if len(int_list) == 1:
        return True
    
    for i in int_list:
        if type(i) != int:
            return False
    
    return True

def main():
    
    get_list = input("Enter list of numbers: ")
    
    print max_in_list(get_list)
    
if __name__ == "__main__":
    main()