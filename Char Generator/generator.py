# Define a function generate_n_chars() 
# that takes an integer n and a character c and 
# returns a string, n characters long, consisting only of c:s. 
# For example, generate_n_chars(5,"x") should return the string "xxxxx". 
# (Python is unusual in that you can actually write an expression 5 * "x" 
# that will evaluate to "xxxxx". For the sake of the exercise 
# you should ignore that the problem can be solved in this manner.)

def generate_n_chars(reps, char):
    if verify(reps, char):  # Check if input is appropriate
        result = ''

        for i in range(reps):
            result = result + char

        return result
    
    else:
        return False

def verify(reps, char):
    if (type(reps) != int or 
        type(char) != str or
        reps <= 0 or
        len(char) > 1 or 
        len(char) <= 0):
            
        return False
    else:
        return True

def main():
    get_char = raw_input("Enter character: ")
    
    rep = input("Enter number of repetitions: ")
    
    print generate_n_chars(rep, get_char)

if __name__ == "__main__":
    main()
