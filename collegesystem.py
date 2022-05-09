import mysql.connector as mysql
db = mysql.connect(host = "localhost", user = "root", password="", database="college")
command_hanler = db.cursor(buffered=True)
def admin_section():
    while 1:
        print("")
        print("1. Resgister a new student")
        print("2. Resgister a new teacher")
        print("3. Delete a new student")
        print("4. Delete a teacher")
        print("Log out")
        user_option = input(str("Enter an option: "))
        if user_option == "1":
            print("")
            print("Resgister a new student")
            username = input(str("Enter a username: "))
            password = input(str("Enter a password: "))
            query_values = (username, password)
            command_hanler.execute("INSERT INTO users (username, password, privilege) VALUES(%s,%s,'student')",query_values)
            db.commit()
            print(username + " has been register as a new student ")
        elif user_option =="2":
            print("")
            print("Resgister a new teacher")
            username = input(str("Enter a username: "))
            password = input(str("Enter a password: "))
            query_values = (username, password)
            command_hanler.execute("INSERT INTO users (username, password, privilege) VALUES(%s,%s,'teacher')",query_values)
            db.commit()
            print(username + " has been register as a new teacher ")
        elif user_option =="3":
            print("")
            print("Delete the student")
            username = input(str("Enter a username: "))
            query_values = (username, "student")
            command_hanler.execute("DELETE FROM users WHERE username = %s and privilege=%s", query_values)
            db.commit()
            if command_hanler.rowcount <1:
                print("Nothing to be deleted")
            else:
                print(username + " has been deleted")
        elif user_option =="4":
            print("")
            print("Delete the teacher")
            username = input(str("Enter a username: "))
            query_values = (username, "teacher")
            command_hanler.execute("DELETE FROM users WHERE username = %s and privilege=%s", query_values)
            db.commit()
            if command_hanler.rowcount <1:
                print("Nothing to be found")
            else:
                print(username + " has been deleted")
        elif user_option =="5":
            break
        else:
            print("No valid input")
def auth_admin():
    print("")
    print("Admin login: ")
    print("")
    username = input(str("Enter your username: "))
    password = input(str("Enter your password: "))
    if(username =="admin"):
        if password == "password":
            admin_section()
        else:
            print("Entered invalid password")
    else:
        print("Not an admin")

def main():
    while 1:
        print("Welcome to the college systerm");
        print("")
        print("1. Log in as student")
        print("2. Log in as teacher")
        print("3. Log in as admin")
        user_option = input(str("Option: "))
        if user_option == "1":
            print("Student login ")
        elif user_option == "2":
            print("Teacher login ")
        elif user_option == "3":
            auth_admin()
        else:
            print("No valid input login")
main()

