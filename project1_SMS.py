class Create_student:
    def __init__(self, Id, name, age, per):
        self.Id = Id
        self.name = name
        self.age = age
        self.per = per


class Student_Management:
    def __init__(self, org):
        self.org = org
        self.student_dict = {}
        print(f"{f'STUDENT MANAGEMENT SYSTEM OF [{self.org}]': ^150}")

    def student_management_menu(self):
        while True:
            print("\nEnter your choice : \n(1)-> Add New Student \n(2)-> Search Student\n(3)-> Remove Student\n(4)-> Update Information\n(5)-> Display Students")
            choice = self.get_intValue("\nEnter your choice : ")

            if choice >= 1 and choice <= 5:

                if choice == 1:
                    print("\n-> New Student Registration <-")
                    self.add_student()

                elif not self.student_dict:
                    print("-> No Students Data Found !")

                elif choice == 2:
                    print(
                        "\nEnter Searching Basis : \n(1)-> Student Name \n(2)-> Student ID : ")
                    s = self.get_intValue("\nEnter your choice : ")

                    if s == 1:
                        name = input("\nEnter Student Name : ").strip(
                            " ").capitalize()
                        self.search_student(s, name)

                    elif s == 2:
                        Id = input("\nEnter Student ID : ")
                        self.search_student(s, Id)

                    else:
                        print("\n-> Invalid choice to Search!!")

                elif choice == 3:
                    self.remove_student()

                elif choice == 4:
                    self.update_info()
                    print("\n-> Student Details Updated Successfully")

                elif choice == 5:
                    print("\n-> [Available Students Data : ]")
                    for student in self.student_dict.values():
                        self.display(student)

            else:
                return False

    def add_student(self):
        while True:
            Id = str(self.get_intValue("\nEnter Student ID : "))
            if Id not in self.student_dict:
                break
            print("This Id is already exist")
        name = input("Enter Student Name : ").strip(" ").capitalize()
        age = self.get_intValue("Enter Student Age : ")
        per = self.get_intValue("Enter Marks Percentage : ")
        new_student = Create_student(Id, name, age, per)
        self.student_dict[Id] = new_student

    def search_student(self, s, key):
        if s == 1:  # Search Name
            for student in self.student_dict.values():
                if student.name == key:
                    print(f"\n-> Student Name found successfully :")
                    self.display(student)
                    return
            print(f"\n-> Student Not Found with Name : {key} ")

        else:
            if key in self.student_dict:
                print(f"\n-> Student ID found successfully :")
                self.display(self.student_dict[key])
                return True
            else:
                print(f"\n-> Student Not Found with Id : {key} ")
                return False

    def remove_student(self):
        Id = input("\nEnter Student ID : ")
        if self.search_student(2, Id) is True:
            print(f"Student Removed Successfully : ID=[{Id}]")
            del (self.student_dict[Id])

    def update_info(self):
        Id = input("\nEnter Student ID : ")
        if self.search_student(2, Id):
            s = self.student_dict[Id]
            s.name = input("\nEnter Student Name : ").strip(" ").capitalize()
            s.age = self.get_intValue("Enter Student Age : ")
            s.per = self.get_intValue("Enter Marks Percentage : ")

    def display(self, s):
        print(
            f"\nStudent Id :[{s.Id}] , Name : [{s.name}] , Age : [{s.age}] , percentage : [{s.per}%] ")

    def get_intValue(self, Text):
        while True:
            try:
                value = int(input(Text))
                return value
            except ValueError:
                print("!! Invalid Input (Enter Integer Value)")



if __name__=="__main__": 
    s = Student_Management("Python")
    s.student_management_menu()
