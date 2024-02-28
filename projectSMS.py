from tkinter import *
from tkinter import ttk, messagebox
import psycopg2

class Student:
    def __init__(self, root):
        # variables 
        self.Roll_var = StringVar()
        self.Name_var = StringVar()
        self.Gender_var = StringVar()
        self.Dob_var = StringVar()
        self.Contact_var = StringVar()
        self.Course_var = StringVar()
        self.Semester_var = StringVar()
        self.Email_var = StringVar()
        self.Father_var = StringVar()
        self.Address_var = StringVar()

        # Search by variable 
        self.searchBy_var = StringVar()
        self.searchTxt_var = StringVar()

        # frames 
        self.manage_frame = None
        self.btn_frame = None
        self.detail_frame = None
        self.table_frame = None

        # creating gui 
        self.setup_ui(root)
        self.create_widgets()

    def setup_ui(self, root):
        root.title("Student Management System")
        root.geometry("700x300+400+200")

    def create_widgets(self):
        self.create_title_frame()
        self.create_manage_frame()
        self.create_button_frame()
        self.create_detail_frame()
        self.create_table_frame()

    def create_title_frame(self):
        self.title_frame = Frame(root, bd=2, relief=FLAT, bg="#46699F")
        self.title_frame.place(x=0, y=0, width=root.winfo_screenwidth(), height=62)
        self.title_frame.config(highlightbackground="#302F5F", highlightthickness=3)

        title = Label(self.title_frame, text="Student Management System", bd=8, relief=FLAT,
                      font=("Bitter SemiBold", 20, "bold"), bg="Black", fg="#766A9D", padx=5, pady=5)
        title.pack(side=TOP, fill=X)


    def create_manage_frame(self):
        self.manage_frame = Frame(root, bd=4, relief=FLAT, bg="#766A9D")
        self.manage_frame.place(x=0, y=62, width=700, height=775)
        self.manage_frame.config(highlightbackground="#574786", highlightthickness=3)

        m_title = Label(self.manage_frame, text="Manage Student", bd=3, font=("Bitter SemiBold", 20, "bold"), bg="#766A9D", fg="Black")
        m_title.grid(row=0, columnspan=2)

        
        # ---- Student roll no.--------------------------------------------------------------------------------------------- 
        Lbl_roll = Label(self.manage_frame, text="Roll No.", bd=4, font=("Bitter SemiBold", 14, "bold"), bg="#766A9D", fg="#2F2446")
        Lbl_roll.grid(row=1, column=0, pady=10, sticky="w")
        
        Txt_roll=Entry(self.manage_frame, textvariable=self.Roll_var, bd=4, font=("Bitter SemiBold", 13), relief=FLAT)
        Txt_roll.grid(row=1, column=1, padx=20, pady=10, sticky="w")


        # ---- Student name ------------------------------------------------------------------------------------------------- 
        Lbl_sName = Label(self.manage_frame, text="Student Name", bd=4, font=("Bitter SemiBold", 14, "bold"), bg="#766A9D", fg="#2F2446")
        Lbl_sName.grid(row=2, column=0, pady=10, sticky="w")
        
        Txt_sName=Entry(self.manage_frame, textvariable=self.Name_var, bd=4, font=("Bitter SemiBold", 13), relief=FLAT)
        Txt_sName.grid(row=2, column=1, padx=20, pady=10, sticky="w")


        # ---- Student DOB ------------------------------------------------------------------------------------------------- 
        Lbl_dob = Label(self.manage_frame, text="DOB", bd=4, font=("Bitter SemiBold", 14, "bold"), bg="#766A9D", fg="#2F2446")
        Lbl_dob.grid(row=3, column=0, pady=10, sticky="w")
        
        Txt_dob=Entry(self.manage_frame, textvariable=self.Dob_var, bd=4, font=("Bitter SemiBold", 13), relief=FLAT)
        Txt_dob.grid(row=3, column=1, padx=20, pady=10, sticky="w")



        # ---- Student Gender ------------------------------------------------------------------------------------------------ 
        Lbl_gen = Label(self.manage_frame, text="Gender", bd=4, font=("Bitter SemiBold", 14, "bold"), bg="#766A9D", fg="#2F2446")
        Lbl_gen.grid(row=4, column=0, pady=10, sticky="w")

        combo_gen = ttk.Combobox(self.manage_frame, textvariable=self.Gender_var, font=("Bitter SemiBold", 12), state="readonly")
        combo_gen['values']=("Male", "Female", "Other")
        combo_gen.grid(row=4, column=1, padx=20, pady=10, sticky="w")


        # ---- Student phone no. ---------------------------------------------------------------------------------------------- 
        Lbl_phone = Label(self.manage_frame, text="Contact", bd=4, font=("Bitter SemiBold", 14, "bold"), bg="#766A9D", fg="#2F2446")
        Lbl_phone.grid(row=5, column=0, pady=10, sticky="w")
        
        Txt_phone=Entry(self.manage_frame, textvariable=self.Contact_var, bd=4, font=("Bitter SemiBold", 13), relief=FLAT)
        Txt_phone.grid(row=5, column=1, padx=20, pady=10, sticky="w")
        validate_phone_number = root.register(self.validate_phone_number)
        Txt_phone.config(validate="key", validatecommand=(validate_phone_number, '%P'))


        # ---- Student course ---------------------------------------------------------------------------------------------- 
        Lbl_course = Label(self.manage_frame, text="Course", bd=4, font=("Bitter SemiBold", 14, "bold"), bg="#766A9D", fg="#2F2446")
        Lbl_course.grid(row=6, column=0, pady=10, sticky="w")
        
        Txt_course = ttk.Combobox(self.manage_frame, textvariable=self.Course_var, font=("Bitter SemiBold", 12), state="readonly")
        Txt_course['values']=("BA", "BBA", "BCA", "B.Com", "LLB", "B.Pahrma" , "MBA", "MCA", "M.Com", "B.Ed")
        Txt_course.grid(row=6, column=1, padx=20, pady=10, sticky="w")



        # ---- Student sem -------------------------------------------------------------------------------------------------- 
        Lbl_sem = Label(self.manage_frame, text="Semester", bd=4, font=("Bitter SemiBold", 14, "bold"), bg="#766A9D", fg="#2F2446")
        Lbl_sem.grid(row=7, column=0, pady=10, sticky="w")
        
        Txt_sem=Entry(self.manage_frame, textvariable=self.Semester_var, bd=4, font=("Bitter SemiBold", 13), relief=FLAT)
        Txt_sem.grid(row=7, column=1, padx=20, pady=10, sticky="w")

        
        # ---- Student email -------------------------------------------------------------------------------------------------- 
        Lbl_email = Label(self.manage_frame, text="Email id", bd=4, font=("Bitter SemiBold", 14, "bold"), bg="#766A9D", fg="#2F2446")
        Lbl_email.grid(row=8, column=0, pady=10, sticky="w")
        
        Txt_email=Entry(self.manage_frame, textvariable=self.Email_var, bd=4, font=("Bitter SemiBold", 13), relief=FLAT)
        Txt_email.grid(row=8, column=1, padx=20, pady=10, sticky="w")


        # ---- Student father name -------------------------------------------------------------------------------------------------- 
        Lbl_fName = Label(self.manage_frame, text="Father Name", bd=4, font=("Bitter SemiBold", 14, "bold"), bg="#766A9D", fg="#2F2446")
        Lbl_fName.grid(row=9, column=0, pady=10, sticky="w")
        
        Txt_fName=Entry(self.manage_frame, textvariable=self.Father_var, bd=4, font=("Bitter SemiBold", 13), relief=FLAT)
        Txt_fName.grid(row=9, column=1, padx=20, pady=10, sticky="w")


        # ---- Student address -------------------------------------------------------------------------------------------------- 
        Lbl_addr = Label(self.manage_frame, text="Address", bd=4, font=("Bitter SemiBold", 14, "bold"), bg="#766A9D", fg="#2F2446")
        Lbl_addr.grid(row=10, column=0, pady=10, sticky="w")
        
        self.Txt_addr=Text(self.manage_frame, width=21, height=3, font=("Bitter SemiBold", 13))
        self.Txt_addr.grid(row=10, column=1, padx=20, pady=10, sticky="w")



    def create_button_frame(self):
        self.btn_frame = Frame(self.manage_frame, bd=1, relief=FLAT, bg="#30264A")
        self.btn_frame.place(x=8, y=700, width=425)

        add_btn = Button(self.btn_frame, text="Add", width=10, height=2, command=self.add_student).grid(row=0, column=0, padx=12, pady=10)
        update_btn = Button(self.btn_frame, text="Update", width=10, height=2, command=self.update_student).grid(row=0, column=1, padx=12, pady=10)
        delete_btn = Button(self.btn_frame, text="Delete", width=10, height=2, command=self.delete_student).grid(row=0, column=2, padx=12, pady=10)
        clear_btn = Button(self.btn_frame, text="Clear", width=10, height=2, command=self.clear_fields).grid(row=0, column=3, padx=12, pady=10)

    def create_detail_frame(self):
        self.detail_frame = Frame(root, bd=4, relief=FLAT, bg="#30264A")
        self.detail_frame.place(x=450, y=62, width=1000, height=775)
        self.detail_frame.config(highlightbackground="#574786", highlightthickness=3)

        lbl_search = Label(self.detail_frame, text="Search_By", bd=10, font=("Bitter SemiBold", 15, "bold"), bg="#30264A", fg="White")
        lbl_search.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        combo_search = ttk.Combobox(self.detail_frame, textvariable=self.searchBy_var, width=20, font=("Bitter SemiBold", 13), state="readonly")
        combo_search['values'] = ("Roll_no", "Student_Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        txt_search = Entry(self.detail_frame, textvariable=self.searchTxt_var, bd=5, width=20, font=("Bitter SemiBold", 10), relief=FLAT)
        txt_search.grid(row=0, column=2, padx=20, pady=10, sticky="w")

        search_btn = Button(self.detail_frame, text="Search", width=10, height=1, pady=5, command=self.search_student).grid(row=0, column=3, padx=10, pady=10)
        show_all_btn = Button(self.detail_frame, text="Search All", width=10, height=1, pady=5, command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

    def create_table_frame(self):
        self.table_frame = Frame(self.detail_frame, bd=4, relief=FLAT, bg="#766A9D")
        self.table_frame.place(x=30, y=80, width=930, height=670)
        self.table_frame.config(highlightbackground="#574786", highlightthickness=3)

        scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(self.table_frame, columns=("Roll", "Name", "DOB", "Gender", "Contact", "Course", "Semester", "Email", "Father", "Address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Roll", text="Roll no.")
        self.student_table.heading("Name", text="Student Name")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Contact", text="Contact")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Email", text="Email ID")
        self.student_table.heading("Father", text="Father's Name")
        self.student_table.heading("Address", text="Address")
        
        self.student_table.column("Roll", width=100)
        self.student_table.column("Name", width=120) 
        self.student_table.column("DOB", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Contact", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Father", width=120)
        self.student_table.column("Address", width=150)

        self.student_table['show']='headings'
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    def add_student(self):
        try:
            # Validate all fields to be filled 
            if not all([
                self.Roll_var.get(),
                self.Name_var.get(),
                self.Dob_var.get(),
                self.Gender_var.get(),
                self.Contact_var.get(),
                self.Course_var.get(),
                self.Semester_var.get(),
                self.Email_var.get(),
                self.Father_var.get(),
                self.Txt_addr.get(1.0, END).strip()
            ]):
                    messagebox.showerror("Error", "All input fields must be filled")
                    return

            # Validate phone number
            contact = self.Contact_var.get()
            if not contact.isnumeric() or len(contact) != 10:
                messagebox.showerror("Error", "Phone number must be a 10-digit integer!")
                return
            

            # Check if student with the same Roll_no already exists
            conn =  psycopg2.connect(host="localhost", user="postgres", password="123456", database="StudentMGT")

            with conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM studenttable WHERE Roll_no = %s", (self.Roll_var.get(),))
                    existing_Roll = cursor.fetchone()

                    if existing_Roll:
                        messagebox.showerror("Error", "Student with this ID already exists!")
                    else:
                    # Check if the phone number exist
                        cursor.execute("SELECT * FROM studenttable WHERE Contact = %s", (contact,))
                        existing_Contact = cursor.fetchone()

                        if existing_Contact:
                            messagebox.showerror("Error", "Phone number already in use.")
                        else:
                            query = "INSERT INTO studenttable (Roll_no, Student_name, Dob, Gender, Contact, Course, Semester, Email, Father_name, Address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            data = (self.Roll_var.get(), self.Name_var.get().capitalize(), self.Dob_var.get(), self.Gender_var.get(), contact, self.Course_var.get(), self.Semester_var.get(), self.Email_var.get(), self.Father_var.get().capitalize(), self.Txt_addr.get(1.0, END).capitalize().strip())

                            cursor.execute(query, data)
                            conn.commit()
                            self.fetch_data()
                            self.clear_fields()
                            messagebox.showinfo("Success", "Student added successfully!")

        except Exception as e:
            messagebox.showerror("Error", "An error occurred while adding the student.")


    def validate_phone_number(self, P):
        if P.isdigit() and len(P) <= 10 or P == "":
            return True
        else:
            messagebox.showwarning("Warning", "Phone number must be a 10-digit integer!")
            return False
        


    def fetch_data(self):
        try:
            conn = psycopg2.connect(host="localhost", user="postgres", password="123456", database="StudentMGT")
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM studenttable ORDER BY Roll_no")
                    rows = cursor.fetchall()
                    self.update_table(rows)
        except Exception as e:
            messagebox.showerror("Error", "An error occurred while fetching data.")

    def update_table(self, rows):
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
        else:
            self.student_table.delete(*self.student_table.get_children())


    def clear_fields(self):
        self.Roll_var.set("")
        self.Name_var.set("")
        self.Dob_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.Course_var.set("")
        self.Semester_var.set("")
        self.Email_var.set("")
        self.Father_var.set("")
        self.Txt_addr.delete(1.0, END)
        self.searchBy_var.set("")
        self.searchTxt_var.set("")


    def get_cursor(self, event):
        RowRecord = self.student_table.focus()
        contents = self.student_table.item(RowRecord)
        row = contents['values']
        self.Roll_var.set(row[0])
        self.Name_var.set(row[1])
        self.Dob_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.Course_var.set(row[5])
        self.Semester_var.set(row[6])
        self.Email_var.set(row[7])
        self.Father_var.set(row[8])
        self.Txt_addr.delete(1.0, END)  # Clear the address field
        self.Txt_addr.insert(END, row[9])


    def update_student(self):
        try:
            conn = psycopg2.connect(host="localhost", user="postgres", password="123456", database="StudentMGT")
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute("UPDATE studenttable SET Student_name=%s, Dob=%s, Gender=%s, Contact=%s, Course=%s, Semester=%s, Email=%s, Father_name=%s, Address=%s WHERE Roll_no=%s", 
                    (self.Name_var.get().capitalize(), self.Dob_var.get(), self.Gender_var.get(), self.Contact_var.get(), self.Course_var.get(), self.Semester_var.get(), self.Email_var.get(), self.Father_var.get().capitalize(), self.Txt_addr.get(1.0, END).capitalize().strip(), self.Roll_var.get()))
                    if cursor.rowcount > 0:
                        conn.commit()
                        self.fetch_data()
                        messagebox.showinfo("Success", "Student record updated successfully.")
                    else:
                        messagebox.showwarning("Warning", "Student with Roll number {} does not exist.".format(self.Roll_var.get()))

        except Exception as e:
            messagebox.showerror("Error", "An error occurred while updating data.")


    def delete_student(self):
        try:
            conn = psycopg2.connect(host="localhost", user="postgres", password="123456", database="StudentMGT")
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute("DELETE FROM studenttable WHERE Roll_no=%s", (self.Roll_var.get(),))
                    conn.commit()
                    self.fetch_data()
                    messagebox.showinfo("Success", "Student record deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", "An error occurred while deleting data.")

    def search_student(self):
        try:
            conn = psycopg2.connect(host="localhost", user="postgres", password="123456", database="StudentMGT")
            with conn:
                with conn.cursor() as cursor:
                    column_name = self.searchBy_var.get()
                    query = f"SELECT * FROM studenttable WHERE {column_name} = %s"
                    cursor.execute(query, (self.searchTxt_var.get().capitalize(),))
                    rows = cursor.fetchall()
                    self.update_table(rows)
        except Exception as e:
            messagebox.showerror("Error", f"Error Occured while Searching Stduent Details")
 
root = Tk()
student_app = Student(root)
root.mainloop()