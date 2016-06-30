# Define a procedure histogram() that takes a list of integers 
# and prints a histogram to the screen. 
# For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******

def histogram(int_list):
    """Draw histogram"""
        
    if verify(int_list):    # Check if histogram is correct
        result = ''
        
        for i in int_list:
            result = result + '*' * i + '\n'
            
        return result
    
def verify(int_list):
    """Check if list i appropriate"""
    
    int_list = list(int_list)
    
    if len(int_list) == 0:
        return False
    
    for i in int_list:
        if type(i) != int:
            return False
    
    return True

def main():
    get_list = input("Enter int list: ")
    
    print histogram(get_list)

if __name__ == "__main__":
    main()