#faezeh kuchakzadeh
#class thursday 14-18
#adad va amalgare vorudi dar tabe(def)

def calculator():
    number1 = int(input('enter first number : \n'))
    number2 = int(input('enter second number : \n'))
    operator = input('enter Arithmetic Operator : \n')

    if operator== '+':
        print(number1+number2)
    elif operator=='-':
        print(number1-number2)
    elif operator=='/':
        print(number1/number2)
    elif operator=='*':
        print(number1*number2)
    elif operator=='**':
        print(number1**number2)
    else:
        print('I dont know what you say.\n')
    #print(f'mohasebe shoma :')
calculator()
