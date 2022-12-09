import json
import time
filename = 'students.json'

# Visualization of the list

def view_data():
    with open(filename,"r") as f:
        temp = json.load(f)

        for entry in temp:
            university = entry["university"]
            id = entry["id"]

            for data in entry["info"]:
                first_name=data["first_name"]
                last_name=data["last_name"]
                student_id=data["student_id"]
                specialty=data["specialty"]

                print(f"University : {university}")
                print(f"Id : {id}")
                print(f"First Name : {first_name}")
                print(f"Last Name : {last_name}")
                print(f"Student Id : {student_id}")
                print(f"Specialty : {specialty}")
                print("\n")

# Add data to the list

def add_data():
    item_data = {}
    with open (filename, "r") as f:
        temp = json.load(f)

    university = item_data["universty"] = input("University: ")
    id = item_data["id"] = input("Id: ")
    first_name = item_data["first_name"] = input("First Name: ")
    last_name = item_data["last_name"] = input("Last Name: ")
    student_id = item_data["student_id"] = input("Student Id: ")
    specialty = item_data["specialty"] = input("Specialty: ")

    temp.append({"university": university, "id": int(id),"info":[{"first_name": first_name, "last_name": last_name, "student_id": int(student_id), "specialty": specialty}]})

    with open(filename,"w") as f:
        json.dump(temp,f,indent=4)

# Edit data

def edit_data():
    view_data()
    new_data = []
    with open (filename, "r") as f:
        temp = json.load(f)
        data_length = len(temp)-1
    print("Which index number would you like to edit?")
    edit_option = input(f"Select a number 0-{data_length} ")
    i=0
    for entry in temp:
        if i == int(edit_option):
            university = entry["university"]
            id = entry["id"]

            for data in entry["info"]:
                first_name=data["first_name"]
                last_name=data["last_name"]
                student_id=data["student_id"]
                specialty=data["specialty"]

            print(f"Current University : {university}")
            university=input("What would you like the new university to be? ")

            print(f"Current Id : {id}")
            id=input("What would you like the new id to be? ")

            print(f"Current First Name : {first_name}")
            first_name=input("What would you like the new first name to be? ")

            print(f"Current Last Name : {last_name}")
            last_name=input("What would you like the new last name to be? ")

            print(f"Current Student Id : {student_id}")
            student_id=input("What would you like the new student id to be? ")

            print(f"Current Specialty : {specialty}")
            specialty=input("What would you like the new specialty to be? ")

            new_data.append({"university": university, "id": int(id),"info":[{"first_name": first_name, "last_name": last_name, "student_id": int(student_id), "specialty": specialty}]})
            i=i+1
        else:
            new_data.append(entry)
            i=i+1
    with open(filename,"w") as f:
        json.dump(new_data,f,indent=4)

# Delete data from the list

def delete_data():
    view_data()
    new_data = []
    with open (filename, "r") as f:
        temp = json.load(f)
        data_length = len(temp)-1
    print("Which index number would you like to delete?")
    delete_option = input(f"Select a number 0-{data_length} ")
    i=0
    for entry in temp:
        if i == int(delete_option):
            pass
            i=i+1
        else:
            new_data.append(entry)
            i=i+1
    with open(filename,"w") as f:
        json.dump(new_data,f,indent=4)
        
# Search

def search_1():
    with open(filename,"r") as f:
            temp = json.load(f)

            entered_data = input("Enter University: ")

            for entry in temp:
                    university = entry["university"]

                    for data in entry["info"]:
                        first_name=data["first_name"]
                        last_name=data["last_name"]
                        student_id=data["student_id"]
                        specialty=data["specialty"]

                    if university == entered_data:
                        print(f"\nFirst Name : {first_name}")
                        print(f"Last Name : {last_name}")
                        print(f"Student Id : {student_id}")
                        print(f"Specialty : {specialty}")

def search_2():
    with open(filename,"r") as f:
            temp = json.load(f)

            entered_data = input("Enter Specialty: ")

            for entry in temp:

                    for data in entry["info"]:
                        first_name=data["first_name"]
                        last_name=data["last_name"]
                        student_id=data["student_id"]
                        specialty=data["specialty"]

                        if specialty == entered_data:
                            print(f"\nFirst Name : {first_name}")
                            print(f"Last Name : {last_name}")
                            print(f"Student Id : {student_id}")
                            print(f"Specialty : {specialty}")

def search_3():
    with open(filename,"r") as f:
            temp = json.load(f)
            count = 0
            for entry in temp:
                university = entry["university"]
                if university == "KNU":
                    count += 1
            print("The Number is: ", count)


def ChoicesSearch():
    print("(1) Find all Students of Entered University")
    print("(2) Find all Students of Entered Specialty")
    print("(3) Find the Number of Students KNU")

def search_data():
    ChoicesSearch()
    choice = input("\nEnter Number: ")
    print("\n")
    if choice == "1":
        search_1()
    elif choice == "2":
        search_2()
    elif choice == "3":
        search_3()

def Choices():
    print("-----------------------------------------------")
    print("           Students Management System")
    print("-----------------------------------------------")
    print("(1) View Data")
    print("(2) Add Data")
    print("(3) Edit Data")
    print("(4) Delete Data")
    print("(5) Search Data")
    print("(6) About the project")
    print("(7) Use Timer")
    print("(8) Exit")

def About():
    print("Name and Surname: Kseniya Gladkih")
    print("Course: 2")
    print("Group: K25")
    print("Year: 2022")
    print("Description: This is Student Management System with JSON using Python")

def Helper():

    # Count up timer

    start = input("Press enter to start the timer")

    print("The timer has started")

    begin = time.time()

    endtimer = input("Press enter to stop the timer")

    end = time.time()
    elapsed = end - begin
    elapsed = int(elapsed)

    print("The time elapsed is", elapsed, "seconds")

while True:
    Choices()
    choice = input("\nEnter Number: ")
    print("\n")
    if choice == "1":
        view_data()
    elif choice == "2":
        add_data()
    elif choice == "3":
        edit_data()
    elif choice == "4":
        delete_data()
    elif choice == "5":
        search_data()
    elif choice == "6":
        About()
    elif choice == "7":
        Helper()
    elif choice == "8":
        break
    else:
        print("You did not select a number, please read more carefully.")


