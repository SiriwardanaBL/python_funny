def reverse_string(value:str):
    string = value
    index = -1 
    reversed_string = ""
    while True: 
        if index < -len(string):
            print(reversed_string)
            break
        else:
            reversed_string += string[index]
            index -= 1 
    
reverse_string("Bihan")
