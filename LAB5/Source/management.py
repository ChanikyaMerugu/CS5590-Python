import numpy as np
class person_details:
    def __init__(self, name, lid_id):
        self.name = name
        self.lid_id = lid_id
    def displayEmployee(self):
        print("Name : ", self.name, ", library id: ", self.lid_id)
    def _welcomeMessage(self):
            print("\nGreetings", self.name, "this is umkc library!\n")
            print("your details:")
            print("Name:", self.name, "identificatino", self.lib_id)
class location:
    def __init__(self,loc):
        self.loc = loc

    def displayaddress(self):
        print("Address is: ", self.loc)
class info(person_details, location):
    def __init__(self, name, lib_id, loc):
        self.type = "user"
        person_details.name = name
        person_details.lib_id = lib_id
        person_details._welcomeMessage(self)
        location.loc = loc
        location.displayaddress(self)

class Ainfo(person_details, location):
    def __init__(self, name, lib_id, loc):
        self.type = "admin"
        #super.__init__(name, 'navi')
        person_details.name = name
        person_details.lib_id = lib_id
        person_details._welcomeMessage(self)
        location.loc = loc
        location.displayaddress(self)
class book(object):
    def __init__(self):
        print("please enter your book:")
        book_list = ["S.no", "name of the book", "no.of days to return"]
        row_count = [1, 2, 3]
        self.data = np.array([[1, 'hello', 10],
                         [2, 'hello2', 20],
                         [3, 'hello3', 30]])
        print(self.data)

    def changeList(self, type):
        if(type == "Admin"):
            print("\nadmin can one use the books\n")
            decision = input("add one more:")
            if(decision.upper() == "YES"):
                list = input("please enter the name of the book(sno,book, days you needed):").split(",")
                np.append(self.data, list)
                print(np.append(self.data, list))
        else:
            print("please try again later")


user = info('chanu','ravi','123')
b=book()
admin = Ainfo('hello','hello', '4321')
c=book()

