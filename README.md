# Fibonacci Recurrence Relationship:  
1. F(n) = F(n-1) + F(n-2)  
    > where n = 1,2,3,... and F(1)=F(2)=1  

# Logic:
To calculate the nth term in the Fibonacci Sequence, we take advantage of the matrix exponentiation properties of the Fibonacci Matrix.  
> In short:  
> > Fibonacci Matrix = [[1,1],[1,0]] or ['1 1 ; 1 0']  
> > the [0,0]th element of the FibMatrix to the exponent of n = (n+1)th term in te Fibonacci Sequence

# Functionality and Return:
1. The function asks the user to input the input their desired fibonacci term  
2. returns the desired fiboancci term in integer data type

# Programming Concepts used:
1. Functions and Returns  
2. Input  
3. Exception Handling

# Libraries used:
Numpy:  
	numpy.matrix()  
	numpy.matrix()**
