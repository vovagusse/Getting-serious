prog = True

def render_pyramid(input_num):
    for i in range(input_num // 2):
        print('*' * (i + 1))
    
    for i in range((input_num // 2) + 1, 0, -1):
        print('*' * (i))

def main():
    while prog == True:
        input_num = int(input("Enter pyramid's y axis height: "))
        if (input_num % 2 == 0) or (type(input_num) != int):
            print("Enter an odd integer! \n(Your input is either even, or not an integer/not convertable to integer. Try again!)")
            
        else:
            render_pyramid(input_num)
            break


main()