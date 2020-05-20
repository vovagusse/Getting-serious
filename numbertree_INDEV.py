def build(n):
    for i in range(n):  
        print(str((i+1)**2)) 

def user_input():
    return int(input("type your number here: ")) 

def start():
    num = user_input() 
    build(num)  
start()  
# yo the formula is wrong 