import sys


class NumberSystem:
    HEX_CONVERTERS = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    def __init__(self, number, system):
        self.number = number
        self.system = system

    def get_converted_number(self):
        converted_number = self.get_calculated_numbers_list()
        self.replace_numbers_with_hex_letters(converted_number)
        concatenated_converted_number = self.concatenate_numbers(converted_number)
        return concatenated_converted_number

    def get_calculated_numbers_list(self):
        dividing_result = None
        converted_number_list = []
        while self.number != 0:
            rest = self.get_rest_of_dividing()
            converted_number_list.append(rest)
            self.number = self.get_number_dividing_value()
        return converted_number_list[::-1]

    def get_number_dividing_value(self):
        return self.number // self.system

    def get_rest_of_dividing(self):
        return self.number % self.system

    def replace_numbers_with_hex_letters(self, number_list):
        for i, number in enumerate(number_list):
            if number in self.HEX_CONVERTERS.values():
                hex_notation = self.find_key_in_hex_convertes(number)
                number_list[i] = hex_notation

    def find_key_in_hex_convertes(self, number):
        for key, value in self.HEX_CONVERTERS.items():
            if number == value:
                return key

    def concatenate_numbers(self, converted_numbers):
        for i, number in enumerate(converted_numbers):
            converted_numbers[i] = str(number)
        return ''.join(converted_numbers)


if __name__ == '__main__':
    number = int(input('Provide number in decimal system to convert: '))
    system = int(input('Provide number system to which you want convert: '))
    numberSys = NumberSystem(number, system)
    print(numberSys.get_converted_number())
    
