from arabic_romanic.NumberOperations import NumberOperations
from arabic_romanic.MappingArabicRomanic import Mapping


class CalculationRoman:

    def __init__(self):
        self.numberOperations = NumberOperations()
        self.mapping = Mapping()
        self.list_numbers_dict = [1000, 500, 100, 50, 10, 5, 1]

    def calculate_romanic_number(self):
        # list of digits of number

        self.list_numbers_dict_digits = self.numberOperations.introduce_nr_digits_list()
        dict_pos_values = self.numberOperations.make_position_value_dictionary(self.list_numbers_dict_digits)
        result = ""
        # making calculations
        # 4 digits number
        if len(self.list_numbers_dict_digits) == 4:
            for key in dict_pos_values.keys():
                if key == 1:
                    if dict_pos_values[key] == 1:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[0]]
                    elif dict_pos_values[key] == 2:
                        result += 2 * self.mapping.mapping_dictionary[self.list_numbers_dict[0]]
                    elif dict_pos_values[key] == 3:
                        result += 3 * self.mapping.mapping_dictionary[self.list_numbers_dict[0]]
                if key == 2:
                    if dict_pos_values[key] == 1:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[2]]
                    elif dict_pos_values[key] == 2:
                        result += 2 * self.mapping.mapping_dictionary[self.list_numbers_dict[2]]
                    elif dict_pos_values[key] == 3:
                        result += 3 * self.mapping.mapping_dictionary[self.list_numbers_dict[2]]
                    elif dict_pos_values[key] == 4:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[2]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[1]]
                    elif dict_pos_values[key] == 5:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[1]]
                    elif dict_pos_values[key] == 6:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[1]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[2]]
                    elif dict_pos_values[key] == 7:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[1]] + 2 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[2]]
                    elif dict_pos_values[key] == 8:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[1]] + 3 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[2]]
                    elif dict_pos_values[key] == 9:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[2]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[0]]
                if key == 3:
                    if dict_pos_values[key] == 1:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 2:
                        result += 2 * self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 3:
                        result += 3 * self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 4:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[4]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[3]]
                    elif dict_pos_values[key] == 5:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[3]]
                    elif dict_pos_values[key] == 6:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[3]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 7:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[3]] + 2 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 8:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[3]] + 3 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 9:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[4]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[2]]
                if key == 4:
                    if dict_pos_values[key] == 1:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 2:
                        result += 2 * self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 3:
                        result += 3 * self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 4:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[6]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[5]]
                    elif dict_pos_values[key] == 5:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[5]]
                    elif dict_pos_values[key] == 6:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[5]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 7:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[5]] + 2 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 8:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[5]] + 3 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 9:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict_digits[6]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
        # 3 digits number
        elif len(self.list_numbers_dict_digits) == 3:
            for key in dict_pos_values.keys():
                if key == 1:
                    if dict_pos_values[key] == 1:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[2]]
                    elif dict_pos_values[key] == 2:
                        result += 2 * self.mapping.mapping_dictionary[self.list_numbers_dict[2]]
                    elif dict_pos_values[key] == 3:
                        result += 3 * self.mapping.mapping_dictionary[self.list_numbers_dict[2]]
                    elif dict_pos_values[key] == 4:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[2]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[1]]
                    elif dict_pos_values[key] == 5:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[1]]
                    elif dict_pos_values[key] == 6:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[1]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[2]]
                    elif dict_pos_values[key] == 7:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[1]] + 2 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[2]]
                    elif dict_pos_values[key] == 8:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[1]] + 3 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[2]]
                    elif dict_pos_values[key] == 9:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[2]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[0]]
                if key == 2:
                    if dict_pos_values[key] == 1:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 2:
                        result += 2 * self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 3:
                        result += 3 * self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 4:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[4]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[3]]
                    elif dict_pos_values[key] == 5:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[3]]
                    elif dict_pos_values[key] == 6:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[3]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 7:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[3]] + 2 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 8:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[3]] + 3 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 9:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[4]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[2]]
                if key == 3:
                    if dict_pos_values[key] == 1:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 2:
                        result += 2 * self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 3:
                        result += 3 * self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 4:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[6]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[5]]
                    elif dict_pos_values[key] == 5:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[5]]
                    elif dict_pos_values[key] == 6:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[5]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 7:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[5]] + 2 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 8:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[5]] + 3 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 9:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[6]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
        # 2 digits number
        elif len(self.list_numbers_dict_digits) == 2:
            for key in dict_pos_values.keys():
                if key == 1:
                    if dict_pos_values[key] == 1:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 2:
                        result += 2 * self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 3:
                        result += 3 * self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 4:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[4]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[3]]
                    elif dict_pos_values[key] == 5:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[3]]
                    elif dict_pos_values[key] == 6:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[3]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 7:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[3]] + 2 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 8:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[3]] + 3 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
                    elif dict_pos_values[key] == 9:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[4]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[2]]
                if key == 2:
                    if dict_pos_values[key] == 1:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 2:
                        result += 2 * self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 3:
                        result += 3 * self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 4:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[6]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[5]]
                    elif dict_pos_values[key] == 5:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[5]]
                    elif dict_pos_values[key] == 6:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[5]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 7:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[5]] + 2 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 8:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[5]] + 3 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 9:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[6]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[4]]
        # 1 digit number
        elif len(self.list_numbers_dict_digits) == 1:
            for key in dict_pos_values.keys():
                if key == 1:
                    if dict_pos_values[key] == 1:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 2:
                        result += 2 * self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 3:
                        result += 3 * self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 4:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[6]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[5]]
                    elif dict_pos_values[key] == 5:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[5]]
                    elif dict_pos_values[key] == 6:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[5]] + \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 7:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[5]] + 2 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 8:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[5]] + 3 * \
                                  self.mapping.mapping_dictionary[self.list_numbers_dict[6]]
                    elif dict_pos_values[key] == 9:
                        result += self.mapping.mapping_dictionary[self.list_numbers_dict[6]] + \
                                  self.mapping.mapping_dictionary[
                                      self.list_numbers_dict[4]]
        result_formated = " ".join(result)
        print(result_formated)

