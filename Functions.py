username = input('Welcome to Square Root Calculator!, what is your name?')
user_number = int(input(f'Hi {username}! ,what number do you want to find its Square root?'))
print(f'Fine, now we need to know what  algorithm you prefer for solve the problem, please, write the number of the algorithm')
algorithm = int(input ( 'Exhaustive Enumeration-just exact square roots(1) / Binary(2) / Aproximation(3)'))
#Functions

def enumeration (number) : 
    answer = 0
    while answer**2 < number :
        answer += 1
    if answer**2 == number :
        print(f'The square root of {number} is {answer}')
    else :
        print(f'{number} don´t have an exact square root')

def binary (number) :
    epsilon = 0.01
    low = 0.0
    high = max(1.0, number)
    answer = (high + low) / 2
    while abs(answer**2 - number) >= epsilon :
        if answer**2 < number :
            low = answer
        else  :
            high = answer
        
        answer = (high + low) / 2
    print(f'The square root of {number} is {answer}')
    
def aprox (number) :
    epsilon = 0.001
    step = epsilon**2
    answer = 0.0
    while abs(answer**2 - number) >= epsilon and answer <= number :
        answer += step
    
    if abs(answer**2 - number) >= epsilon :
        print(f'The square root of {number} was not found')
    else :
        print(f'The square root of {number} is {answer}')
    

#ifs

if algorithm == 1 :
    print(f'{username},You have choosen the Exhaustive Enumeration algortihm')
    enumeration(user_number)
     

elif algorithm == 2 :
    print(f'{username},You have choosen the Binary algortihm')
    binary(user_number)

elif algorithm == 3 :
    print(f'{username},You have choosen the Aproximation algortihm')
    aprox(user_number)

else :
    print ('You didn´t choose any algorithm, please choose one')


