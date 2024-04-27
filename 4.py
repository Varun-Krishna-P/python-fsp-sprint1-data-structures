import ast

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
Create class Person
Initialize the class with first_name,last_name
Create a member function "Name" that returns the Full name of the person
Type of first_name - str
Type of last_name - str
'''
class Person:
    
    
    
    
    
    
    
'''
Create another class Student that inherits the proporties of class Person
Initialize the class variable "count" with value 0
Initialize the class with fist_name,last_name,rollno,mark1,mark2
class variable count should have the number of students
Create a member function "GetStudent" that returns the fullname,rollno,total marks seperated by commas
Type of first_name - str
Type of last_name -str
Type of rollno - int
Type of mark1 - int
Type of mark2 - int
'''    

class Student(Person):
    
    
    
    
    
    
    
    
    
    
    
'''
Create another class Staff that inherits the proporties of class Person
Initialize the class variable "count" with value 0
Initialize the class with fist_name,last_name,staffnum
class variable count should have the number of staffs
Create a member function "GetStaff" that returns the fullname and staffnumber seperated by comma
Type of first_name - str
Type of last_name -str
Type of staffnum - int
'''    
  
    
class Staff(Person):   
    
    
    
    
    
    

if __name__=='__main__':
    students = ast.literal_eval(input())
    staff = ast.literal_eval(input())
    t = []
    s = []
    for i in staff:
        t.append(Staff(i[0],i[1],i[2]))
    for i in students:
        s.append(Student(i[0],i[1],i[2],i[3],i[4]))
    
    for i in t:
        print(i.GetStaff())
    print(Staff.count)

    for i in s:
        print(i.GetStudent())
    print(Student.count)