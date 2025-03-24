def is_anagram(value_1:str, value_2:str):
    value_1_list = []
    for i in value_1:
        value_1_list.append(i.lower())
    print(value_1_list)
    
    value_2_list = []
    for i in value_2:
        value_2_list.append(i.lower())
    print(value_2_list)
    
    if len(value_1_list) != len(value_2_list):
       return False
    else:
        count = 0
        while True:
            if count == len(value_2_list):
                return True
            else:
                if value_2_list[count] in value_1_list:
                    value_1_list.remove(value_2_list[count])
                    count += 1
                else:
                    return False
                 
 

print(is_anagram("Bhan", "Bihan"))
#space improvement required