def countUp(number):
    if number>0:
        countUp(number-1)
    print(number)
    
#main program
number = 3
countUp(number)
print("back in main program")
        
