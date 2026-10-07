class Student:

    # Constructor
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    # Method to save student
    def save_student(self):
        with open("students.txt", "a") as file:
            file.write(
                f"{self.student_id},{self.name},{self.age},{self.course}\n"
            )

def view_students():

    try:
        with open("students.txt", "r") as file:

            records = file.readlines()
            

            if len(records) == 0:
                print("\nNo student records found.")
                return

            print("\n========== STUDENT RECORDS ==========")

            for record in records:
                if not record.strip():
                    continue

                student_id, name, age, course = record.strip().split(",")

                print(f"Student ID : {student_id}")
                print(f"Name       : {name}")
                print(f"Age        : {age}")
                print(f"Course     : {course}")

    except FileNotFoundError:
        print("\nNo records found.")

def search_student():

    search_name = input("\nEnter student name: ")

    try:
        with open("students.txt", "r") as file:

            found = False

            for record in file:
                if not record.strip():
                    continue

                student_id, name, age, course = record.strip().split(",")

                if name.lower() == search_name.lower():

                    print("\nStudent Found")
                    print("----------------")
                    print(f"Student ID :, {student_id}")
                    print(f"Name       :, {name}")
                    print(f"Age        :, {age}")
                    print(f"Course     :, {course}")

                    found = True
                    break

            if not found:
                print("Student not found.")

    except FileNotFoundError:
        print("No records available.")
        
def delete_student():
    delete_name=input("\nEnter the name of the student you want to delete:")
    
    try:
        with open("students.txt", "r") as file:

            records = file.readlines()
            
            updated_records = []
            
            found = False
        
        for record in records:
            if not record.strip():
                continue
            
            student_id, name, age, course = record.strip().split(",")
            if name.strip().lower()==delete_name.strip().lower():
                found=True
                print(f"The student {name} has been removed!")
            else:
                updated_records.append(record)
                
        if not found:
            print(f"\nError: No student found with ID '{delete_id}'.")
            return
            
        with open("students.txt", "w") as file:
            for record in updated_records:
                file.write(record + "\n")
    except FileNotFoundError:
        print("No records available.")

while True:

    print("\n================================")
    print("      STUDENT RECORD SYSTEM")
    print("================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete student")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    # ADD STUDENT
    if choice == "1":

        print("\nADD STUDENT")

        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        student = Student(
            student_id,
            name,
            age,
            course
        )

        student.save_student()

        print("\nStudent record saved successfully!")

    # VIEW STUDENTS
    elif choice == "2":

        view_students()

    # SEARCH STUDENT
    elif choice == "3":

        search_student()
        
    #DELETE STUDENT
    elif choice=="4":
        
        delete_student()
        

    # EXIT
    elif choice == "5":

        print("\nProgram Closed.")
        break

    # INVALID OPTION
    else:

        print("\nInvalid choice. Try again.")
