from number_converter import NumberSystem


def test_conversion_to_binary():
    number = 243
    number_in_binary_without_prefix = str(bin(243))[2:]
    converted_number = NumberSystem(243, 2).get_converted_number()
    if converted_number != number_in_binary_without_prefix:
        raise Exception('Conversion to binary failed!')

def test_conversion_to_octal():
    number = 243
    number_in_binary_without_prefix = str(oct(243))[2:]
    converted_number = NumberSystem(243, 8).get_converted_number()
    if converted_number != number_in_binary_without_prefix:
        raise Exception('Conversion to octal failed!')

def test_conversion_to_hexadecimal():
    number = 243
    number_in_binary_without_prefix = str(hex(243))[2:]
    converted_number = NumberSystem(243, 16).get_converted_number()
    if converted_number != number_in_binary_without_prefix:
        raise Exception('Conversion to hexadecimal failed!')

if __name__ == "__main__":
    test_conversion_to_binary()