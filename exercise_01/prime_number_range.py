def prime_numbers(start,end):
    try:
        if not isinstance(start, int):
            raise TypeError("First argument must be a list.")
        if not isinstance(end, int):
            raise TypeError("Index must be an integer.")
        
        number_list = []
        number = start
        while True:
           if number == end:
              print(number_list)
              break
           else:
              number_list.append(number)
              number += 1
       
    except (TypeError, IndexError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
 
prime_numbers(10,34)