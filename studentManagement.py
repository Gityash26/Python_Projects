class student:
    def __init__(self,name,roll,age,per):
        self.name=name
        self.rolnum=roll
        self.age=age
        self.percent=per

class student_management:
    Org="\nWELCOME TO COE (Python Course)"

    def __init__(self):
        self.id=0
        print(self.Org)
        self.student_list=[]
    
    def create(self,name,roll,age,per):
        new_student=student(name,roll,age,per)
        self.student_list.append(new_student)
    
    def display(self,s):
        print(f"\nID no. : {s.rolnum}")
        print(f"Name   :{s.name}")
        print(f"Age    :{s.age} ")
        print(f"Percentage:{s.percent}%\n")

    def search(self):
        key=input("\nOn Which Basis You Wants to Search a Student : \n(1)Student ID\n(2)Student Name\n==>Enter your choice : ")

        if key== '1':
            r=int(input("\nEnter the Id No.: "))
            for i,val in enumerate(self.student_list):
                if val.rolnum==r:
                    print("\n--> Student Data found <-- ")
                    self.display(val)
                    return i
            print(f"\n--> No Data found of Student ID  {r} <--")
            
                    
        elif key== '2':
            n=input("\nEnter the Student Name : ")
            for i,val in enumerate(self.student_list):
                if val.name==n:
                    print("\n--> Student Data found <--")
                    self.display(val)
                    return i
            print(f"\n--> No Data found of Student Name : {n} <--")
        
        else:
            print("\n--> Invalid choice")
            self.search()

    def delete(self):
        i=self.search()
        if i!=None:
            print(f"{self.student_list[i].name} Removed Successfully")
            self.student_list.remove(self.student_list[i])

    def update(self):
        i=self.search()
        if i!=None:
            choice=input("\nWhat you wants to Update : \n(1)Student name \n(2)Student Age\n(3)Student Percenage\n==>Enter your choice:")
            if choice=='1':
                self.student_list[i].name=input("\nEnter New Name : ")
                print("Name changed successfully")
            elif choice=='2':
                self.student_list[i].age=input("\nEnter new age : ")
                print("Age changed successfully")
            elif choice=='3':    
                self.student_list[i].percentage=input("\nEnter new percentage : ")
                print("Percentage changed successfully")

        
COE=student_management()

while True:
    print("\n(1) Add New Student\n(2) Remove a Student\n(3) Display Students\n(4) Search Student \n(5)Update Student Info")

    try:
        choice = int(input("==>Enter your choice : "))
    except:
        print("\nONLY INTEGERS ALLOWED")
        continue

    if choice == 1:
        COE.id=COE.id+1
        print("\n--> New Student Registration <--")
        name = input("\nEnter student name: ")
        age = input("Enter student age: ")
        per = input("Enter student percentage: ")
        COE.create(name, COE.id, age, per)

    elif choice>=2 and choice<=5:

        if not COE.student_list:
            print("\nCurrently No Student Found")

        elif choice == 2:
            COE.delete()        

        elif choice == 3: 
            print("\n--> Class Students <--")
            for s in COE.student_list:
                COE.display(s)

        elif choice == 4:
            COE.search()

        elif choice == 5:
            COE.update()

    else:
        print("\nInvalid Choice!")
        break










            



