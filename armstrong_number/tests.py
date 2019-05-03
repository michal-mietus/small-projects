from main import ArmstrongNumber


def test_is_number_narcistic_should_be_true():
    numbers = [407, 6, 153]
    for number in numbers:
        if not ArmstrongNumber(number).is_narcistic():
            print('Failed.', test_is_number_narcistic_should_be_true.__name__, number)
    

def test_is_number_narcistic_should_be_false():
    numbers = [408, 154, 222]
    for number in numbers:
        if ArmstrongNumber(number).is_narcistic():
            print('Failed.', test_is_number_narcistic_should_be_true.__name__, number)



if __name__ == '__main__':
    test_is_number_narcistic_should_be_true()
    test_is_number_narcistic_should_be_false()