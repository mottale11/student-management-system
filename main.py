# STUDENT MANAGEMENT SYSTEM

# ------PERSON-------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


# -----STUDENT-----
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.__grades = {}
        self.__gpa = 0

    def add_grade(self, course_name, score):
        if 0<= score <= 100:
            if course_name not in self.__grades:
                self.__grades[course_name] = []
            self.__grades[course_name].append(score)
            print(f"New grade added: {score} to {course_name}")
        else:
            print("Invalid Grade. Must be between 0-100.")

    def calculate_gpa(self):
        all_scores = []
        for scores in self.__grades.values():
            all_scores.extend(scores)

        if not all_scores:
            self.__gpa = 0
        else:
            avg = sum(all_scores)/len(all_scores)
            self.__gpa = round(min(4, avg/25), 2)
        return self.__gpa

    def get_transcript(self):
        print(f"\n---Transcript for {self.name} ---")
        if not self.__grades:
            print("No grades available yet.")
            return
        for course, scores in self.__grades.items():
            avg = sum(scores)/len(scores)
            print(f"- {course}: Grades = {scores} | Average = {avg:.2f} \t GPA = {self.calculate_gpa():.2f}")


    def introduce(self):
        print(f"I am Student. My name is {self.name},"
              f"I am{self.age} years old, and my student ID is {self.student_id}.")


# ------TEACHER------
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print(f"I am Teacher. My name is {self.name}, and I am {self.age} years old."
              f"I teach: {self.subject}")


# ------ COURSE ------
class Course:
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to {self.course_name}")

    def list_students(self):
        print(f"\n----Students in {self.course_name} Course-----")
        if not self.students:
            print("No students enrolled yet")
            return
        for student in self.students:
            print(f"- {student.name} (ID: {student.student_id})")

    def enter_exam_scores(self):
        print(f"\n--- Enter Exam Scores for {self.course_name} Course ---")
        for student in self.students:
            try:
                score = float(input(f"Enter score for {student.name} "))
                student.add_grade(self.course_name, score)
            except ValueError:
                print("Invalid input. Skipping student...")

    def course_average(self):
        all_scores = []
        for student in self.students:
            student_score = []
            try:
                student_score = student._Student__grades[self.course_name]
            except KeyError:
                pass

            all_scores.extend(student_score)

        if not all_scores:
            return 0
        return sum(all_scores)/len(all_scores)


# -------------------MAIN DRIVEN SYSTEM------------

students = {}
teachers = {}
courses = {}

def menu():
    print("\n---------------------------------------------")
    print("     Welcome to Student Management System!")
    print("---------------------------------------------")
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. Add Course")
    print("4. Enroll Student in Course")
    print("5. Enter Exam Scores for Course")
    print("6. Show Transcript")
    print("7. List Students in Course")
    print("8. Course Average")
    print("9. Exit")


while True:
    menu()
    choice = input("Select an option: ")

    # Add student
    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        sid = int(input("Enter student ID: "))

        students[sid] = Student(name, age, sid)
        print(f"Student {name} added successfully.")

    # Add teacher
    elif choice == "2":
        name = input("Enter teacher name: ")
        age = int(input("Enter teacher age: "))
        subject = input("Enter subject taught: ")

        teachers[name] = Teacher(name, age, subject)
        print(f"Teacher {name} added successfully.")

    # Add course
    elif choice == "3":
        cname = input("Enter course name: ")
        teacher_name = input("Enter teacher name: ")

        if teacher_name not in teachers:
            print("Teacher not found. Please add teacher first.")
        else:
            courses[cname] = Course(cname, teachers[teacher_name])
            print(f"Course {cname} added successfully.")

    # Enroll student in course
    elif choice == "4":
        sid = int(input("Enter student ID: "))
        cname = input("Enter course name: ")
        if sid not in students:
            print("Student not found. Please add student first.")
        elif cname not in courses:
            print("Course not found. Please add course first.")
        else:
            courses[cname].add_student(students[sid])

    # Enter exam scores for Course
    elif choice == "5":
        cname = input("Enter course name: ")
        if cname not in courses:
            print("Course not found.")
        else:
            courses[cname].enter_exam_scores()

    # Show transcript
    elif choice == "6":
        sid = int(input("Enter student ID: "))
        if sid not in students:
            print("Student not found.")
        else:
            students[sid].get_transcript()

    # List students in course
    elif choice == "7":
        cname = input("Enter course name: ")
        if cname not in courses:
            print("Course not found.")
        else:
            courses[cname].list_students()

    # Course average
    elif choice == "8":
        cname = input("Enter course name: ")
        if cname not in courses:
            print("Course not found.")
        else:
            print(f"Course average for {cname}: {courses[cname].course_average()}")

    # Exit
    elif choice == "9":
        print("Exiting system...")
        break
    else:
        print("Invalid option. Please try again.")
