#Snikitha Padala | 43009394

value_1=int(input("Enter the first side: "))
value_2=int(input("Enter the second side: "))
value_3=int(input("Enter the third side: "))

def triangle_validator(value_1,value_2,value_3):
    """
    the above function takes user input and checks whether the triangle is valid or not 
    """
    if (value_1+value_2)>value_3 and (value_1+value_3)>value_2 and (value_2+value_3)>value_1:
        """
        the following conditions have to be met:
        1. A plus B must be greater than C
        2. A plus C must be greater than B
        3. B plus C must be greater than A
        (here value_1 = A, value_2 = B, value_3 = C)
        """

        return True             #if the condition is met the functions returns True
    else:
        return False            #if the conditon is not satisfied then it returns False              
    
def main():
    """
    The main () function runs the defined function above
    """
    print(triangle_validator(value_1,value_2,value_3))

main()
