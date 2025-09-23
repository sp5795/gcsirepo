user_input=int(input("Enter a number: "))

def even_odd (user_input):
    '''
    The following function takes input from the user in the form of a number
    and checks whether its odd or even and print the output message'''

    if user_input % 2==0:                          #if the remainder is 0 then the number of even
        print("Number is even")
    else:                                          #otherwise the number is odd
        print("Number is odd")

def square_cube(user_input):
    '''
    The following function takes input from the user in the form of a number
    and prints the square and root of that number
    '''
    #Square
    number=user_input
    print("Squaure of",number ,"=",number*number)
    #Cube
    print("Cube of",number ,"=",number*number*number)

def main():
    even_odd(user_input)
    square_cube(user_input)

main()


