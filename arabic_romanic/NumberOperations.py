from arabic_romanic.ArabicNumber import ArabicNumber
class NumberOperations:

    def __init__(self):
        self.arabic_number = ArabicNumber()

    def introduce_nr_digits_list(self):
        #put in a dictionary positions/values
        number = self.arabic_number.introduce_arabic_number()
        list_digits = []
        while number!=0:
            digit = int(number%10)
            list_digits.append(digit)
            number = int(number/10)

        list_digits.reverse()
        return list_digits

    def make_position_value_dictionary(self,list_digits):
        counter = 1; dict={}
        for i in range(0, len(list_digits)):
            dict.update({counter:list_digits[i]})
            counter+=1
        return dict


    #depending on list _size we will calculate and add what is the number...try this variant




