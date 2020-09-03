
num_int = 0   
max_int = 0

while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        # if the number is higher than the previous max number it becomes the max number
        max_int = num_int 
print("The maximum is", max_int)    
