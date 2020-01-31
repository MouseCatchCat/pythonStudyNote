students = [];
def get_student_title_case():
    students_title_case = [];
    for student in students:
        students_title_case.append(student['name'].title());
    return students_title_case;

def print_student_title_case():
        students_title_case = get_student_title_case();
        print(students_title_case);

def add_student(name, student_id = 1, student_grade = 0):
    student = {"name": name, "student_id": student_id, "student_grade": student_grade};
    students.append(student)
    return students;

def save_file(student):
    try:
        f = open('students.txt', 'a');
        f.write(student+"\n");
        f.close();
    except Exception as error:
        print('There is problem with save the file');

def read_file():
    try:
        f = open('students.txt', 'r');
        for student in f.readlines():
            student = student.rstrip();
            add_student(student);
        f.close();
    except Exception:
        print('There is problem with reading the file');

print_student_title_case();

# read the file first to get all datas in the students
read_file();

# user friendly ask
is_adding_more_student = input('Do you want to add students? if yes please type yes, if no, please type no: ');

while is_adding_more_student == "yes":
    try:
        student_name = input("Please enter the student name: ");
        student_id = input("Please enter the student id: ");
        student_grade = input("Please enter the student grade: ");
    except Exception as error:
        print('There is error for the enterring infomation: {0}'.format(error));
    add_student(student_name, student_id, student_grade);
    save_file(student_name);
    is_adding_more_student = input('Do you want to add more students? if yes please type yes, if no, please type no: ');

print_student_title_case();
