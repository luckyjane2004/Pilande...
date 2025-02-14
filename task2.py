class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old and I study {self.course}.")

# Create three student objects
student1 = Student("LUCKY JANE PILANDE", 20, "Information Technology")
student2 = Student("KIMBERLY SHANE VILLEGAS", 20, "Information Technology")
student3 = Student("TRISHA KATE SANTIAGO", 20, "Information Technolpgy")

# Call the introduce method for each student
student1.introduce()
student2.introduce()
student3.introduce()