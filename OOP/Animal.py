class Animal():
    """ The class creates an animal object with the age given during initialiation
        and provides methods to set age and name, get age and name; along the
        with magic function to return the string representation of the animal
        object.
    """
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        # Provides the age attribute
        return self.age
    
    def get_name(self):
        # Provides the name attribute
        return self.name

    def set_age(self, newage):
        # Method to set the age of the animal object
        self.age = newage

    def set_name(self, newname):
        # Method to set the name of the animal object
        self.name = newname

    def __str__(self):
        # Provides the string representation of the animal object
        return "animal:" + str(self.name) + ":" + str(self.age)

class Rabbit(Animal):
    """ The class inherits from animal class and allows to create a child rabbit
        object for the two parent rabbit and assigns a tag to the child rabbit
        to distinguish it as it initially has no name attribute for indetification
    """
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        # provides the id attribute for the rabbit object
        return str(self.rid).zfill(3)

    def get_parent1(self):
        # provides parent1 attribute
        return self.parent1

    def get_parent2(self):
        # provides parent2 attribute
        return self.parent2

    def __add__(self, other):
        # returning object of same type as this class, creates child rabbit object
        
        return Rabbit(0, self, other)

    def __eq__(self, other):
        # Method to check whether two child rabbits have same parent rabbits
        parents_same = self.parent1.rid == other.parent1.rid and \
                       self.parent2.rid == other.parent2.rid

        parents_opposite = self.parent2.rid == other.parent1.rid and \
                           self.parent1.rid == other.parent2.rid

        return parents_same or parents_opposite

    
