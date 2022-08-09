class Kaksha:
    def __init__(
        self, fname, rank, height
    ):  # init is aka constructor. with the help of self we create our variables
        self.name = fname  # attributed of class
        self.rank = rank
        self.height_cm = height
        self.introduction = self.intro(fname, rank, height)

    def intro(self, fname, rank, height):  # method of the class
        variable = f'(My name is {fname} I have scored rank {str(rank)} and having height of {str(height)})'
        return variable


first = Kaksha('shubham', 1, 165)
second = Kaksha('raj', 2, 175)
third = Kaksha('deeksha', 3, 156)

print(second.introduction)

# print(first.name, first.rank, first.height)

first.sex = 'male'
second.sex = 'female'

# print(first.__dict__)
# print(second.__dict__)
# print(third.__dict__)

#print( third.sex) # shows a attribute error bcz for third object we donot define sex attribute.

# adding variables into the class is known as properties and adding function is called as method.


# Now we make a child class.
class Student(Kaksha):
    def __init__(
        self, fname, rank, height, year
    ):  #  The __init__() function is called automatically every time the class is being used to create a new object.

        #Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
        super().__init__(fname, rank, height)

        # adding property in child class.
        self.grd_year = year


# fourth = Student('aanjaney', 4, 168, 2015)
# fourth_intro = Student.intro('raj', 12, 178)
