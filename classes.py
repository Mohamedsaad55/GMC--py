# Student Managment System ! 

class Student :
    def __init__ (self , name , age , grade):
        self.name = name 
        self.age = age 
        self.grade = grade 
class St_mg_sys:
    def __init__ (self):
        self.students = []
    
    def add_student (self,name,age,grade):
        student = Student(name , age , grade) 
        self.students.append(student)
        print("Added Succsffully !")
        
        
    def update (self, name , age , grade ):
        for student in self.students:
            if student.name == name:
                student.age = age 
                student.grade = grade 
                print("Updated !")
                return 
            print("Student Not Found !")
            
    def display (self):
        for student in self.students:
            print(f"Name:  {student.name} , Age : {student.age}, Grade : {student.grade}")
            
    def menu (self):
        print("1 : Add Student")
        print("2 : Update Student")
        print("3 : Display Students")
        print("4 : Quit")
        
    def run(self):
        while True :
            self.menu()
            choice = input("Please Select an Option ! from (1 : 4)\n")
            if choice == "1":
                name = input("Name : ")
                age = input("Age : ")
                grade = input("Grade :")
                self.add_student(name,age,grade)
            elif choice == "2":
                name = input("Name : ")
                age = input("Age : ")
                grade = input("Grade :")
                self.update(name , age , grade)
            elif choice == "3":
                self.display()
            elif choice =="4":
                break
            else : 
                print("You Choosed Wrong Option")