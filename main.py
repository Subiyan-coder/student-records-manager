import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="student_db"
)
cursor = conn.cursor()

def add_student():
    name = input("Enter name: ")
    email = input("Enter email: ")
    course = input("Enter course: ")
    sql = "INSERT INTO students (name, email, course) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, email, course))
    conn.commit()
    print("Student added!")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_student():
    student_id = input("Enter student ID to update: ")
    name = input("Enter new name: ")
    email = input("Enter new email: ")
    course = input("Enter new course: ")
    sql = "UPDATE students SET name=%s, email=%s, course=%s WHERE id=%s"
    cursor.execute(sql, (name, email, course, student_id))
    conn.commit()
    print("Student updated!")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    print("Student deleted!")

while True:
    print("\n1. Add Student\n2. View Students\n3. Update Student\n4. Delete Student\n5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
