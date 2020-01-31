students = []


class Student:
    school_name = 'School'

    # constructor to init an obj
    def __init__(self, name, student_id=1, student_grade=0):
        self.name = name
        self.student_id = student_id
        self.student_grade = student_grade
    
    # override the print function basically, if I print the new created obj, it will return from this function
    # instead of a string of memory
    def __str__(self):
        return "student name: " + self.name + '\n' + "student id:" + str(
            self.student_id) + '\n' + "student grade: " + str(self.student_grade)

    def get_student_name_capitalized(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


class HighSchool(Student):
    school_name = "The second high school"

    def get_student_name_capitalized(self):
        original_value = super().get_student_name_capitalized()
        return original_value + 'is in the school called: ' + self.get_school_name()


john = HighSchool(name='john', student_id=4, student_grade=99)
print(john)
print(john.get_student_name_capitalized())
