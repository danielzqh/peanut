class Person(object):
    def getGender(self):
        return "Unknown"

class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
        return "Female"

aMan = Male()
aWoman = Female()
print(aMan.getGender())
print(aWoman.getGender())
