import datetime

class Person():
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def __str__(self):
        """return self's name"""
        return self.name

    def setBirthday(self, month, day, year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        """return True if self's name is lexicographically
            less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        self.idNum = MITPerson.nextIdNum # MITPerson attribute: unique ID
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting MIT people uses ther ID number!, not name
    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, utterance):
        return(self.getLastName()+" says:" + utterance)

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, " + utterance)

class Grad(Student):
    pass

def isStudent(obj):
    return isinstance(obj, Student)

class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department

    def speak(self, utterance):
        new = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, new + utterance)

    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)



    

# example usage of Person class
##p1 = Person('Mark Zuckerberg')
##p1.setBirthday(5,14,84)
##p2 = Person('Drew Houston')
##p2.setBirthday(3,4,83)
##p3 = Person('Bill Gates')
##p3.setBirthday(10,28,55)
##p4 = Person('Andrew Gates')
##p5 = Person('Steve Woznizk')
##
##personList = [p1, p2, p3, p4, p5]
##
##for e in personList:
##    print(e)
##
##personList.sort()
##print()
##
##for e in personList:
##    print(e)


# example usage of MITPerson class
m3 = MITPerson('Mark Zuckerberg')
Person.setBirthday(m3,5,14,84)
m2 = MITPerson('Drew Houston')
Person.setBirthday(m2,3,4,83)
m1 = MITPerson('Bill Gates')
Person.setBirthday(m1,10,28,55)

##MITPersonList = [m1, m2, m3]
##
##for e in MITPersonList:
##    print(e)
##
##MITPersonList.sort()
##
### prints sorted list as per idNum
##for e in MITPersonList:
##    print(e)

#example usage of UG and Grad class
s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Lin Manuel Miranda', 2018)
s4 = Grad('Leonardo di Caprio')

studenList = [s1, s2, s3, s4]

#example usage of Professor class
faculty = Professor('Doctor House', 'six')
