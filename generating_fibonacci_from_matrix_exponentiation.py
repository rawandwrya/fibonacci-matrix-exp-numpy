import numpy as np

def fib_term():
    """
    Fibonacci Recurrence Relationship:
        F(n) = F(n-1) + F(n-2)
        where n = 1,2,3,... and F(1)=F(2)=1

    Logic:
        to calculate the nth term in the Fibonacci Sequence,
        we will use take advantage of the matrix exponentiation properties of the Fibonacci Matrix
        In short:
            Fibonacci Matrix = [[1,1],[1,0]] or ['1 1 ; 1 0']
            the [0,0]th element of the FibMatrix to the exponent of n = (n+1)th term in te Fibonacci Sequence

    Functionality and Return:
        The function asks the user to input the input their desired fibonacci term
        returns the desired fiboancci term in integer data type
    """
    
    # Defining the Fibonacci matrix F
    F = np.matrix([[1, 1], [1, 0]])

    improper_input = True
    while(improper_input):
        user_input = input("Enter the nth term: ")
        try:
            exponent = int(user_input)-1
            if (exponent>0):
                improper_input=False
                result = F**(exponent)
                print("The Fibonacci's ",user_input,"th term is: ",result[0,0])#this line can be commented out if not necessary
                return result
            else:
                print("make sure to input an exponent greater than 0")
        except:
            print("Invalid Input!")
        

if __name__ == '__main__':
    fib_term()
        
