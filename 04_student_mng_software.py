student = {}

## these are all the fields used in making the database
fields = ["GR#",
          "Full Name",
          "Age",
          "Father Name",
          "Address"]

# had to include a few sample student data to work with
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

'''Since I felt the need to display student info again and again, I decided to
make a function out of it'''
def display_student(ind):  ## "ind" refers to "index"
    for k, v in students[ind].items():
        if k == fields[0] or k == fields[2]: # some fields require 1 extra Tab to look presentable
            print (str(k) + ": \t\t" + str(v))
        else:
            print (str(k) + ": \t" + str(v))

''' the code below prints the items of the first Student in one single line'''
#print(students[0].items()) #used it to test something. Not needed anymore

print("\n----------> WELCOME <----------\n")

'''the WHILE statement below ensures that the program keeps on running forever (till 
we ask it to EXIT)'''

while True:
    print('1 to Add Student')
    print('2 to Delete Student')
    print('3 to Edit Student')
    print('4 to Search Student')
    print('5 to Display All Students')
    print('6 to Exit')
    
    option = input("Enter 1 to 6:\t")
    
    if option == '6': # EXIT --------------------------------------------------
        break
        '''Every time we use Break, the program comes out of the current
        conditional statement it is under'''
    
    elif option == "5": # Display ALL------------------------------------------
        for ind in range(len(students)):
            print()
            display_student(ind)
        
    elif option == "2": # Delete ----------------------------------------------
        Name = input("Enter Full Name of Student: \t")
        ind = 0
        for s in students:
            if s['Full Name'] == Name:
                del students[ind]
                print("\nDelete successful")
                break
            else:
                ind += 1
                
    elif option == '1': # Add -------------------------------------------------
        student['GR#'] = input ("Student's GR#: \t")
        student['Full Name'] = input ("Student's Full Name: \t")
        student['Age'] = input ("Student's Age: \t")
        student['Father Name'] = input ("Father's Name: \t")
        student['Address'] = input ("Address: \t")
        students.append(student)
        print("\nAddition Successful")

    elif option == "4": # Search ----------------------------------------------
        print("\nWhich Student's Details you would like to Search?")
        Name = input("Enter Student's Full Name:\t")
        print()
        ind = 0
        
        for s in students:
            if s['Full Name'] == Name:
                print("These are the student's current details")
                display_student(ind)
                break
            else:
                ind += 1

    elif option == "3": # Edit ------------------------------------------------
        print("\nWhich Student's Details you would like to Edit?")
        Name = input("Enter Student's Full Name:\t")
        print()
        ind = 0 
        
        for s in students:
            if s['Full Name'] == Name:
                print('------------------------------------------------------')
                print("These are the student's current details")
                display_student(ind)
                
                print("\nThese are the fields:")
                print(fields)
                print('------------------------------------------------------')
                
                field = input("\nWhich field of the student would you like to edit?\t")
                
                for f in fields:
                    if field == f:
                        entry = input("What would you like to change it to?\t")
                        s[f] = entry
                        print('==============================================')
                        print("\nEDIT SUCCESSFUL\n")
                        display_student(ind)
                        print('\n==============================================')
                        break
                    # else: do nothing, just go back into the for loop
            else:
                ind += 1 
