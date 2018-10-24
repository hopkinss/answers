import statistics

list_values=[]
while True:    
    val = input("Enter integers. When finished, hit [Enter] to perform an operation> ")
    if val.upper() == '':
        oper = input("What operation would you like to perform:\n\t\"+\" for addition " \
                     "\n\t\"*\" for multiplication" \
                     "\n\t\"x\" for mean" \
                     "\n\t\"sd\" for standard deviation >")
        
        # Addition
        if oper =='+':
            print(f"The sum is {sum(list_values)}")
        
        # Multiplication
        elif oper == '*':   
            answer = 1
            for i in list_values:
                answer *= i
            print(f"The product {sum(list_values)} is {answer}")
                
        # Mean
        elif oper == 'x':
            x = statistics.mean(list_values)
            print(f"The mean {', '.join(map(str,list_values))} of is {x}")
        
        #SD
        elif oper.upper() == 'SD':
            x = statistics.stdev(list_values)
            print(f"The standard deviaton of {', '.join([str(i) for i in list_values])} of is {x}")
            
        break
        
    try:
        list_values.append(int(val))
    except ValueError:
        print(f"{val} is not an integer")

    

