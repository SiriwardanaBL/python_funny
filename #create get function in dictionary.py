def get(name: dict, key: any, option: any):
    try:
        if not isinstance(name, dict):
            raise TypeError("Error: The first argument must be a dictionary.")

        if key in name:
            print(name[key])  # Fixed incorrect variable reference
        else:
            print(option)

    except TypeError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
name_age = {"Bihan": 21, "Iresh": 18, "Ishan": 9, "Thushari": 40, "Nimal": 44}
get(name_age, "Bin", 0)
