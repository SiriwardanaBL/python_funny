def count_vowels_consonants(value:str):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'u', 'U']
    symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','.','[',']','{','}',':',';',"'",'"','<','>',',','/','?','|','~','`',' ','1','0','2','3','4','5','6','7','8','9'] 
    vowels_count = 0
    consonants_count = 0
    checking_value = value
    for char in checking_value:
        statement_1= char in vowels
        statement_2= char in symbols
        if statement_1 == True and statement_2 == False :
            vowels_count += 1
        elif statement_1 == False and statement_2 == False:
            consonants_count += 1 
        else:
            continue
    
    print(vowels_count, consonants_count)
         
count_vowels_consonants("Bihan")         

        
