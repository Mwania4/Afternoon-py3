from database import User, Student, Teacher

# Try to save users in the table

try:
    User.create(name="mwania", email="zonia3@gmail.com", password="123")
except:
    print("Please use a different email")

# Display all users saved in the database on the table called Users
users = User.select()
# Write a loop to display all the users
for user in users:
    print(user.name, user.email, user.password)


# Try to save students in the table

try:
    Student.create(name="zonia", adm_no="ADM", course="python")
except:
    print("Enter correct data")

students = Student.select()
# Write a loop to display all the students
for student in students:
    print(student.name, student.adm_no, student.course)


try:
    Teacher.create(name="mwania", profession="Music", reg_no="YT33")
except:
    print("Fill in correctly")

teachers = Teacher.select()

for teacher in teachers:
    print(teacher.name, teacher.profession, teacher.reg_no)
