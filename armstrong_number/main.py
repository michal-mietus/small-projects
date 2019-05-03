class ArmstrongNumber:
    def __init__(self, number):
        self.number = int(number)

    def is_narcistic(self):
        if self.raised_to_power_equals_number():
            return True
        return False

    def raised_to_power_equals_number(self):
        digits_list = self.get_digits_list()
        power = 0
        while True:
            result = self.raise_every_digit_to_power_and_add(digits_list, power)
            if result == self.number:
                return True
            elif result > self.number:
                return False
            power += 1

    def get_digits_list(self):
        return [int(x) for x in str(self.number)]

    def raise_every_digit_to_power_and_add(self, digits_list, power):
        result = 0
        for digit in digits_list:
            result += pow(digit, power)
        return result


if __name__ == '__main__':
    number = input('Please give a number to check: ')
    if ArmstrongNumber(number).is_narcistic():
        print('Number is narcistic')
    else:
        print('Number isn\'t narcistic')