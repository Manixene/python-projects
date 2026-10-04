# Unique Skill Track
Enter_Skill_list = [] #list of all skills

print("Welcome to Unique Skill tracker")

while True:
    print("=====SKILL TRACKER======")
    print("1.ADD Skill")
    print("2.VIEW ADDED SKILLS")
    print("3.UPDATE SKILL STATUS")
    print("4.DELETE SKILL")
    print("5.EXIT")

    choice = int(input("ENTER YOUR CHOICE: "))

#ADD SKILL
    if(choice==1):
        Enter_Skill = input("ADD SKILL: ")
        Status = str(input("KYA STATUS HA STARTED HA Y PENDING? "))
        Description = input("Kya Level Hai: ")


        Skill = {
            "Enter_Skill": Enter_Skill,
            "Status": Status,
            "Description":Description,   
        }

        Enter_Skill_list.append(Skill)
        print("\nDONE BRO")

        #VIEW ADDED SKILLS

    elif choice==2: 
        if(len(Enter_Skill_list)== 0):
            print("NO SKILL ADDED.")

        else:
            print("======= YE RA SARA RECORD======")
            count = 1
            for eachSkill in Enter_Skill_list:
                print(f"{count}. {eachSkill['Enter_Skill']}")
                print(f"   Status: {eachSkill['Status']}")
                print(f"   Description: {eachSkill['Description']}")
                count = count + 1

#--------UPDATE SKILL STATUS-----------

    elif choice == 3:
        print("\nYour Skills:")

        for i, skill in enumerate(Enter_Skill_list):
            print(i + 1, skill["Enter_Skill"], "-", skill["Status"])

        skill_choice = int(input("Choose skill number: "))

        new_status = input("Enter new status: ")

        Enter_Skill_list[skill_choice - 1]["Status"] = new_status

        print("Status updated successfully!")

#---------Delete Skill----------

    elif choice==4:
      print("/nYour Skill")

      for i, skill in enumerate(Enter_Skill_list):
              print(i + 1, skill["Enter_Skill"], "-", skill["Status"]) 

      select_skill =str(input("Select skill you want to delete: "))
      Enter_Skill_list.pop(0)
      print(Skill)
      print("skill deleted successfully")

#---------EXIT----------
    if (choice==5):
        print("THANKS TO USE ME")
        break
    


