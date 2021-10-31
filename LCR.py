def linearCongruentialMethod(Xo, m, a, c,
                             randomNums,
                             noOfRandomNums):
 
    # Initialize the seed state
    randomNums[0] = Xo
 
    # Traverse to generate required
    # numbers of random numbers
    for i in range(1, noOfRandomNums):
         
        # Follow the linear congruential method
        randomNums[i] = ((randomNums[i - 1] * a) +
                                         c) % m
 
# Driver Code
if __name__ == '__main__':
     
    Xo = 57
    m = 123
    a = 7
    c = 1
    noOfRandomNums = 25
 
    # To store random numbers
    randomNums = [0] * (noOfRandomNums)
 
    # Function Call
    linearCongruentialMethod(Xo, m, a, c,
                             randomNums,
                             noOfRandomNums)
 
    # Print the generated random numbers
    for i in randomNums:
        print(i, end = " ")