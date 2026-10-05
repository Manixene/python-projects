# STUDENT RECORD
Student_Record = [] #list

print("Student Record System")

while True:
    print("=====Student Record=====")
    print("1.ADD STUDENT")
    print("2.VIEW STUDENT")
    print("3.UPDATE STUDENT")
    print("4.DELETE STUDENT")
    print("5.EXIT")

    Choice = int(input("Choose option: "))

#--------ADD STUDENT---------
    if(Choice==1):
         Name = input("Enter student name: ")
         Class = input("ENTER CLASS: ")
         Roll_No = int(input("ENTER ROLL NUMBER: "))
         age = int(input("ENTER AGE: "))

         Student = {
             "Name": Name,
             "Class": Class,
             "Roll_No": Roll_No,
             "age": age
         }

         Student_Record.append(Student)
         print("\nDONE.Student record added successfully")

#--------VIEW STUDENT---------
    if(Choice==2):
        if(len(Student)==0):
            print("NO student record added.add student record")

        else:
            print("1. VIEW ALL STUDENTS")
            print("2. VIEW SPECIFIC STUDENT")

            view_choice = int(input("ENTER CHOICE: "))
            if(view_choice==1):
                print("---- ALL STUDENT RECORD-----")
                count = 1
                for eachStudentrecord in Student_Record:
                     print(f"{count}. {eachStudentrecord['Name']}")
                     print(f"Class:   {eachStudentrecord['Class']}")
                     print(f"Roll_No: {eachStudentrecord['Roll_No']}")
                     print(f"age:     {eachStudentrecord['age']}")
                     count = count + 1

            if(view_choice==2):
                 print("veiw specific student record")
                 enter_student_name = str(input("Enter student Name: "))
                 found = False

                 for eachStudentrecord in Student_Record:
                    if eachStudentrecord["Name"].lower() == enter_student_name.lower():
                         print("Name:", Student["Name"])
                         print("Age:", Student["age"])
                         print("Class:", Student["Class"])
                         print("Roll_No:", Student["Roll_No"])
                         found = True

                    if found == False:
                     print("Student not found")
        
#--------UPDATE STUDENT RECORD----------
     
    if(Choice==3):
        enter_student_name = str(input("Enter student name: "))
        found = False
        for eachStudentrecord in Student_Record:
            

                if eachStudentrecord["Name"].lower() == enter_student_name.lower():

                   print("\nStudent Found")
                   print("Current Name:", eachStudentrecord["Name"])
                   print("Current class:", eachStudentrecord["Class"])
                   print("Current Rollno:", eachStudentrecord["Roll_No"])
                   print("Current AGE:", eachStudentrecord["age"])

                   new_name = input("Enter new name: ")
                   new_class = int(input("Enter new age: "))
                   new_rollno = input("Enter new course: ")
                   new_age = int(input("Enter new age"))

                   eachStudentrecord["Name"] = new_name
                   eachStudentrecord["Class"] = new_class
                   eachStudentrecord["Roll_No"] = new_rollno
                   eachStudentrecord["age"] = new_age

                   print("\nStudent record updated successfully!")

                   found = True
                   break

        if found == False:
            print("Student not found")

    #---------DELETE STUDENT RECORD-----------
    if(Choice==4):
        search_name = str(input("ENTER STUDENT NAME YOU WANT TO DELETE: "))
        found = False
        for eachStudentrecord in Student_Record:
            if eachStudentrecord["Name"].lower() == search_name.lower():
                Student_Record.remove(eachStudentrecord)
                print("Student record deleted successfully")
                found = True
                break
            if found == False:
                print("Student not found")

    #--------EXIT----------
    if(Choice==5):
       print("THANKS TO USE ME")
       break
