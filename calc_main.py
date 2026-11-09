#SmartCalculator Main File
import calc_module

#Lambda Function for Square
square = lambda x:x ** 2
results = []

while True:
    print("======SMART CALCILATOR======")
    print("1. Addition")
    print("2. Substration")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Sum and Average")
    print("7. Square Using Lambda and Map")
    print("8. Filter and Result")
    print("9. Exit")

    choise = int(input('Enter Your choise:'))

#Addition

    if choise == 1:
        a = float(input('Enter first Number:'))
        b = float(input('Enter scound Number:'))

        result = calc_module.addition(a=a,b=b)
        results.append(result)
        print('Addition: ',result)

#Substration
    if choise == 2:
        a = float(input('Enter First Number:'))
        b = float(input('Enter Secound Number:'))

        result = calc_module.substration(a=a,b=b)
        results.append(result)
        print('Substration: ',result)

#Multiplication
    if choise == 3:
        a = float(input('Enter First Number:'))
        b = float(input('Enter secound Number:'))

        result = calc_module.multiplication(a=a,b=b)
        results.append(result)
        print('Multiplication:',result)

#Dvision
    if choise == 4:
        a = float(input('Enter First Number:'))
        b = float(input('Enter secound Number:'))

        result = calc_module.division(a=a,b=b)
        if isinstance(result,(int,float)):
            results.append(result)
            
        print('Division: ',result)

#Power
    if choise == 5:
        a = int(input('Enter Base Number: '))

        exponent = input('Enter Exponent (Press Enter, If default 2):')

        if exponent == "":
            result = calc_module.power(num=a)
        else:
            result = calc_module.power(num=a,exponent=float(exponent))

        results.append(result)
        print('Power: ',result)

#Sum and Average
    if choise == 6:
        count = int(input('How many Numbers?'))
        numbers = []

        for i in range(count):
            num = int(input('Enter the Numbers:'))
            numbers.append(num)

        total,average = calc_module.sum_average(*number)

        print('Total: ',total)
        print('Average:',average)

#Lambda and Map
    if choise == 7:
        numbers = list(map(float, input('Enter Number seperated by space: ').split()))
        
        squared = list(map(square,numbers))

        results.extend(squared)

        print("Squared Result:",squared)

#Filter Even Result
    if choise == 8:
        even_result = list(filter(lambda x:x%2 == 0,results))

        print('All Results:',results)
        print('Even Results:',even_result)

#Exit
    if choise == 9:
        print('Successful Calculation Done: ',calc_module.numOperation)

        print('Thank you for using Smart Calculator!')
        break
    else:
        print('Enter valid choise!')
        
    
            

        
    

        






        














