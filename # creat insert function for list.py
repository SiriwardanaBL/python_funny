def insert(name, index, value):    
    try:
        if not isinstance(name, list):
            raise TypeError("First argument must be a list.")
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        
        if index < len(name):
            name[index] = value
        else:
            name.append(value)

        print(name)

    except (TypeError, IndexError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
branchers = ['Kalutara', 'Maharagama', 'Yapanaya', 'Kankasanthure']
insert(branchers, 3, 'Matara')  # Corrected the input to be valid
