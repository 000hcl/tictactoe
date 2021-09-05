def attempt_int_conversion(number, minimum, maximum):
    """
    Checks if the input is can be converted into an integer between "minimum" and "maximum".

    Args:
        number: the input to be converted
        minimum: the minimum allowed value
        maximum: the maximum allowed value

    Returns:
        an integer if the conversion is successful
    """
    try:
        integer = int(number)
        if maximum >= integer >= minimum:
            return integer
        else:
            print("Invalid number. Please retry.")
    except:
        print("Invalid number. Please retry.")