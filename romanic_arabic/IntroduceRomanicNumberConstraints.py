class Constraints:

    def __init__(self):
        self.accepted_string ="MDCLXVI"

    def check_number_consecutive_characters(self, romanic_number):
        poz1 = 0; poz2 = 0;result = 0;
        list_number_characters = []

        while poz1<= len(romanic_number)-1 and poz2 <= len(romanic_number)-1:
            #sssaluut
            if romanic_number[poz1]== romanic_number[poz2]:
                list_number_characters. append(romanic_number[poz2])
                poz2+=1
                result = max(result, len(list_number_characters))
            else:
                list_number_characters. clear()
                poz1+=1

        if result>3:
            print("You have introduced {} consecutive characaters. The maximul is 3.". format(result), end="\n")
            return False
        else:
            return True

    def check_correct_characters(self, romanic_number):
        flag = True
        for i in range (0, len(romanic_number)):
            if romanic_number[i] not in self.accepted_string:
                print("You have introduced {} which is an invalid character".format(romanic_number[i]))
                flag = False
        return flag


    def check_number_of_charaters(self, romanic_number):
        dict ={}; flag = True;
        for i in range (0, len(romanic_number)):
            if romanic_number[i] in dict:
                dict.update({romanic_number[i]:dict[romanic_number[i]]+1})
            else:
                dict.update({romanic_number[i]:1})

        for i in dict.keys():
            if dict[i]>4:
                print("You entered {} too many times.You can enter just a maximum of 4 characters of the same type ". format(i), end ='\n')
                flag = False;
        return flag

    #add extra space in order to not get inderOutOfBounds at string
    def add_extra_space(self, romanic_number):
        new_romanic_number = romanic_number +" "
        return new_romanic_number
