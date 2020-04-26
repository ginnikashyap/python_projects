student_list=[]

def create_student():
    student_name=input("Enter your name: ")
    student_data = {"name": student_name,
               "marks": []
                }
    return student_data



def appendMarks(student,mark):
    student['marks'].append(mark)


def calculateAverageMarks(student):

    number=len(student['marks'])
    if number==0 :
       return 0
    total = sum(student['marks'])
    avg=total/number
    return avg



def student_details(student):
    print("Student {} has average marks {}".format(student['name'],
                                                   calculateAverageMarks(s)))


def print_student_details(stds):
    for i, std in enumerate(stds):
        print("studnet ID {}".format(i))
        student_details(std)

def menu():
    selection = input("Enter 'p' for print out studnet details "
                    "Enter 's' to add new student "
                    "Enter 'a' for adding the marks to student "
                    "Enter  'q' to quit the application ")


    while selection!='q':

        if selection == 'p':
            print_student_details(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Select the student  id for adding mark"))
            student_selection = student_list[student_id]
            new_mark = int(input("Enter the new mark to be added to the student"))
            appendMarks(student_selection, new_mark)

        selection=input("Enter 'p' for print out studnet details "
                        "Enter 's' to add new student "
                        "Enter 'a' for adding the marks to student "
                        "Enter  'q' to quit the application ")


menu()
