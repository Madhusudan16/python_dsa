
# A number greater than 1 with exactly two factors  i.e., 1 and the number itself is a prime number. #

number  = 67;

is_prime = True;

for i in range(2, 11): 
    if (number < 2) or (number != i and number%i == 0 ):
        print( "%d number is not a prime number" % (number)); 
        is_prime =  False
        break;
    
print(is_prime)