
# -----------------------------------------------------
#            first method
# -----------------------------------------------------

def second_largest_method_1(list):
    numbers = []
    for x in enumerate(list):
     if not isinstance(x[1], int):
           print(" -- "+str(x[1])+" is not an integer.")
         
     else:
         numbers.append(x[1])
    #print(numbers)
    largest_number = numbers[0]
    count = 1
    #removing largest number 
    
    while count < len(numbers):
           if largest_number < numbers[count]:
               largest_number = numbers[count]
               count += 1
           else:
               count += 1
    
    #print("larget number is "+str(largest_number))
    numbers.remove(largest_number)

    second_largest_number = numbers[0]
    count = 1
    #removing largest number
    while count < len(numbers):
           if second_largest_number < numbers[count]:
               second_largest_number = numbers[count]
               count += 1
           else:
               count += 1
    
    print("the second largest number is "+ str(second_largest_number))

second_largest_method_1([12, "35", 1, 10, 34, 'gh'])




# -----------------------------------------------------
#            second method
# -----------------------------------------------------



def second_largest_method_1(list):
    numbers = []
    for x in enumerate(list):
     if not isinstance(x[1], int):
           print(" -- "+str(x[1])+" is not an integer.")
         
     else:
         numbers.append(x[1])
    #print(numbers)
    #removing largest number 

    
    #print("larget number is "+str(largest_number))
    numbers.remove(max(numbers))

    print("the second largest number is "+ str(max(numbers)))



    
second_largest_method_1([12, "35", 1, 10, 34, 'gh'])