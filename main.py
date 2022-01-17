from romanic_arabic.CalculationRomanic import CalculationArab
from arabic_romanic.CalculationArabic import  CalculationRoman
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculator = CalculationArab()
    calculator.calculate_arabic_number()
    #roman
    calculator2 = CalculationRoman()
    calculator2.calculate_romanic_number()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
