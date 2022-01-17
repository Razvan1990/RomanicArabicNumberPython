from romanic_arabic.IntroduceRomanicNumberConstraints import Constraints
from romanic_arabic.RomanicNumber import RomanicNumber
from romanic_arabic.MappingRomanicArabic import Mapping

class CalculationArab:
    def __init__(self):
        self.romanic_number = RomanicNumber()
        self.map_values = Mapping()
        self.constraints = Constraints()

    def calculate_arabic_number(self):
        introduced_romanic_number = self.romanic_number.introduce_number()
        introduced_romanic_number_with_space =self.constraints.add_extra_space(introduced_romanic_number)

        """
        1. We must first traverse the string
        2. Keep a sum value with the numbers based on the mapping
        3. Check to see when we have small letter in front of big letter and calculate
        """
        result = 0; i = 0;
        while i <len(introduced_romanic_number_with_space)-1:
            #CM
            if introduced_romanic_number_with_space[i]=="C" and introduced_romanic_number_with_space[i+1]=="M":
                result+=self.make_difference(self.map_values.mapping_dictionary,introduced_romanic_number_with_space[i], introduced_romanic_number_with_space[i+1] )
                i+=2
            #CD
            elif introduced_romanic_number_with_space[i]=="C" and introduced_romanic_number_with_space[i+1]=="D":
                result+=self.make_difference(self.map_values.mapping_dictionary,introduced_romanic_number_with_space[i], introduced_romanic_number_with_space[i+1] )
                i+=2
            #XC
            elif introduced_romanic_number_with_space[i]=="X" and introduced_romanic_number_with_space[i+1]=="C":
                result+=self.make_difference(self.map_values.mapping_dictionary,introduced_romanic_number_with_space[i], introduced_romanic_number_with_space[i+1] )
                i+=2
            #XL
            elif introduced_romanic_number_with_space[i]=="X" and introduced_romanic_number_with_space[i+1]=="L":
                result+=self.make_difference(self.map_values.mapping_dictionary,introduced_romanic_number_with_space[i], introduced_romanic_number_with_space[i+1] )
                i+=2
            #IX
            elif introduced_romanic_number_with_space[i]=="I" and introduced_romanic_number_with_space[i+1]=="X":
                result+=self.make_difference(self.map_values.mapping_dictionary,introduced_romanic_number_with_space[i], introduced_romanic_number_with_space[i+1] )
                i+=2
            #IV
            elif introduced_romanic_number_with_space[i]=="I" and introduced_romanic_number_with_space[i+1]=="V":
                result+=self.make_difference(self.map_values.mapping_dictionary,introduced_romanic_number_with_space[i], introduced_romanic_number_with_space[i+1] )
                i+=2
            else:
                result+=self.map_values.mapping_dictionary[introduced_romanic_number_with_space[i]]
                i+=1
        print("The arabic number is", result)





    def make_difference(self, dictionary, character1, character2):
        number1 = dictionary[character1]
        number2 = dictionary[character2]
        return abs(number2- number1)
