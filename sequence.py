# Creating a sequence, each number is the sum of the last three numbers
n = int(input("Enter the length of the sequence: ")) 
# We need to define the first three digits in the sequence
a = 1
b = 2
c = 3
print(a,b,c,end=" ")
# The first three are defined so we need to adjust the range
for _ in range(1,n-2):
    # Next digit becomes the sum of the last three digits
    d = a+b+c
    print(d,end=" ")
    # We need to change the variables so that the variables for a,b and c shift
    a = b
    b = c
    c = d
    
    
    