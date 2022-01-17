class ArabicNumber:

    def introduce_arabic_number(self):
        x = int(input("Please introduce the number"))
        while x < 0 or x >3999:
            print("Not a convertible to romanic number. Please introduce again")
            x = int(input(" "))
        return x

