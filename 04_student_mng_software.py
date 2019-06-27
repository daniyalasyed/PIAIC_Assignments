student = {}

## these are all the fields used in making the database
fields = ["GR#",
     "Full Name",
     "Age",
     "Father Name",
     "Address"]

students = [{
        "GR#" :         1,
        "Full Name" :   "Daniyal",
        "Age" :         12,
        "Father Name" : "Ajaz",
        "Address" :     "Flat-123, Block ABC"
        } , {
        "GR#" :         2,
        "Full Name" :   "Shahrukh Khan",
        "Age" :         9,
        "Father Name" : "Ajeeb Khan",
        "Address" :     "Khan Mansion"
        } , {
        "GR#" :         3,
        "Full Name" :   "Saad",
        "Age" :         15,
        "Father Name" : "Mukarram",
        "Address" :     "Sindhi Muslim"
        }]

def display_student(ind):
    for k, v in students[ind].items():
        if k == fields[0] or k == fields[2]: 
            print (str(k) + ": \t\t" + str(v))
        else:
            print (str(k) + ": \t" + str(v))


#print(students[0].items()) #this prints the items of Daniyal in one single line

while True:
    print("\n")
    print('1 to Add Student')
    print('2 to Delete Student')
    print('3 to Edit Student')
    print('4 to Search Student')
    print('5 to Display All Students')
    print('6 to Exit')
    
    option = input("Enter 1 to 5:\t")
    
    if option == '6': # EXIT
        break
    
    elif option == "5": # Display ALL
        for ind in range(len(students)):
            print(ind)
            display_student(ind)
        
    elif option == '1': # Add
        student['GR#'] = input ("Student's GR#: \t")
        student['Full Name'] = input ("Student's Full Name: \t")
        student['Age'] = input ("Student's Age: \t")
        student['Father Name'] = input ("Father's Name: \t")
        student['Address'] = input ("Address: \t")
        students.append(student)
        
    elif option == "2": # Delete
        Name = input("Enter Full Name of Student: \t")
        ind = 0
        for s in students:
            if s['Full Name'] == Name:
                del students[ind]
                print()
                print("Delete successful")
                break
            else:
                ind += 1
    
    elif option == "3": # Edit
        print("\nWhich Student's Details you would like to edit?")
        Name = input("Enter Student's Full Name:\t")
        print()
        ind = 0 #the index value is needed to start from 0 as usual
        for s in students:
            if s['Full Name'] == Name:
                print("These are the student's current details")
                display_student(ind)
#                for k, v in students[ind].items():
#                    if k == fields[0] or k == fields[2]: 
#                        print (str(k) + ": \t\t" + str(v))
#                    else:
#                        print (str(k) + ": \t" + str(v))
                
                field = input("\nWhich field would you like to edit?\t")
                for f in fields:
                        if field == f:
                            entry = input("What would you like to change it to?\t")
                            s["Age"] = entry
                            display_student(ind)
                print("\nEdit successful")
                break
            else:
                ind += 1 
                '''if the current index wasn't the one desired then it will 
                increase by 1 and the program will go through the loop again'''
        
    elif option == "4": # Search
        print("To be coded :) ")
