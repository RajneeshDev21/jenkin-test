def process_data(name, age):
    """
    Function that takes two parameters and returns multiple values
    
    Args:
        name (str): Person's name
        age (int): Person's age
    
    Returns:
        tuple: Returns name, age, and a greeting message
    """
    greeting = f"Hello, {name}!"
    is_adult = age >= 18
    return name, age, greeting, is_adult


def main():
    # Call the function and unpack multiple return values
    name, age, greeting, is_adult = process_data("Alice", 25)
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Message: {greeting}")
    print(f"Is Adult: {is_adult}")


if __name__ == "__main__":
    main()