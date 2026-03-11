class Student:
    school_name = "SoftUni"

    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def get_info(self):
        print(f"{self.name} studies at {self.school_name} and has grade {self.grade}")

student_one = Student("Rudi",6)
student_two = Student("Bob",3)
student_one.get_info()
student_two.get_info()