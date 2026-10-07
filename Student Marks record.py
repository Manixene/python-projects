#Student Marks Database
Student ={
    "Manish": { 
        "Account": 96,
        "Maths": 81,
        "Business": 94,
        "English": 94,
        "computer":94
    },

     "Rudar":{
         "History": 90,
         "Geography":95,
         "Poltical":87,
         "English":67,
         "Hindi": 90
     },

     "Shiva": {
         "Maths": 90,
         "History":98,
         "Poltical":97,
         "Economic": 95,
         "Hindi":90
     },

     "Sahu": {
         "Chemistry":98,
         "Physics":90,
         "Biology":95,
         "Maths":90,
         "English":100
     }

}

   
while True:
    print("=====Student Record=====")
    print("1.Show Existing Student Name")
    print("2.SHOW Marks of student")
    print("3.Add Student Data: ")
    print("4.View result")
    print("5.EXIT")

    Choice = int(input("Enter your choice: "))
#------Show Existing student name-------

    if(Choice==1):
        for student_name in Student:
          print(student_name)

#------Show Marks of student-------
    if(Choice==2):
        print("1. VIEW ALL STUDENTS")
        print("2. VIEW SPECIFIC STUDENT")

        view_choice = int(input("Enter view choice: "))
        

        
        if(view_choice==1):

            for student_name, marks in Student.items():
                print("\nStudent:",student_name)

                for subject, mark in marks.items():
                    print(subject,":",mark)

        elif view_choice==2:
            Enter_Student_Name = str(input("Enter Student Name: "))
            found = False

            for student_name ,marks  in Student.items():
                if student_name.lower() == Enter_Student_Name.lower():
                    print("\nStudent: ",student_name)

                    for subject,mark in marks.items():
                        print(subject,":",mark)
                    found = True
            if found == False:
                print("Student not found")

#-----Add Student------
    if(Choice==3):
        student_name = str(input("Enter Student Name: "))
        marks = {}

        while True:
            Subject = input("Enter Subject Name: ")
            mark = int(input("Enter subject Marks: "))
            marks[Subject]=mark
            again = input("Add another subject? yes/no: ").lower()
            if again== "no":
               break
        Student[student_name] = marks
        print("Student added successfully")

#--------View result--------
    if(Choice==4):
        print("1.View all student result")
        print("2.view specific student result")

        result_choice = int(input("Enter choice: "))

        if result_choice ==1:
            for student_name, marks in Student.items():
                total = 0

                for subject, mark in marks.items():
                    total = total+mark

                total_subjects = len(marks)
                percentage = (total/(total_subjects*100))*100

                print("\nStudent:",student_name)
                print("Total Marks:", total)
                print("Percentage:", percentage, "%")
        elif result_choice == 2:

         result_choice = input("Enter student Name: ")

         for student_name, marks in Student.items():

            if student_name.lower() == result_choice.lower():

                total = 0

                for subject, mark in marks.items():
                    total = total + mark

                total_subjects = len(marks)
                percentage = (total / (total_subjects * 100)) * 100

                print("\nStudent:", student_name)
                print("Total Marks:", total)
                print("Percentage:", percentage, "%")

#------------EXIT-------------
    if(Choice==5):
       print("Thank to use me")
       break 


                    

