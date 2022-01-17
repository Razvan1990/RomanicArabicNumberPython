from romanic_arabic.IntroduceRomanicNumberConstraints import Constraints
class RomanicNumber:

    def __init__(self):
        self.constraints = Constraints()


    def introduce_number(self):
        number_romanic = input("Please introduce the romanic number ")
        number_romanic_up = number_romanic.upper()
        condition1 = self.constraints.check_correct_characters(number_romanic_up)
        condition2 = self.constraints.check_number_of_charaters(number_romanic_up)
        condition3 = self.constraints.check_number_consecutive_characters(number_romanic_up)
        while condition1==False or condition2==False or condition3==False:
            print("Please reintroduce the number")
            number_romanic = input("")
            number_romanic_up = number_romanic.upper()
            condition1 = self.constraints.check_correct_characters(number_romanic_up)
            condition2 = self.constraints.check_number_of_charaters(number_romanic_up)
            condition3 = self.constraints.check_number_consecutive_characters(number_romanic_up)
        return number_romanic_up