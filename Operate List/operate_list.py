# Define a function sum() and a function multiply() 
# that sums and multiplies (respectively) all the numbers in a list of numbers. 
# For example, sum([1, 2, 3, 4]) should return 10, 
# and multiply([1, 2, 3, 4]) should return 24.

def check_list(num_list):
    """Check if input is list"""
    
    if num_list is None:
        return False
    
    if len(num_list) == 0:
        return False
    
    new_list = []
    
    for i in num_list:
        if i!='[' and i!=']' and i!=',':
            new_list.append(i)
    
    for x in new_list:
        if type(x) != int:
            return False
    
    return True

def sum(num_list):
    """Compute sum of list values"""
    
    if check_list(num_list):
        
        final_sum = 0

        for i in num_list:
            final_sum = final_sum + i

        return final_sum
    
    else:
        return False

def multiply(num_list):
    """Multiply list values"""
    
    if check_list(num_list):
        
        final_sum = 1

        for i in num_list:
            final_sum = final_sum * i

        return final_sum
    
    else:
        return False

def main():
    get_list = input("Enter list: ")
    
    print sum(get_list)
    print multiply(get_list)

if __name__ == "__main__":
    main()
