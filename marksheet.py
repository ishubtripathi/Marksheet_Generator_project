def calculate_percentage(total_marks, max_marks):
    return (total_marks / max_marks) * 100

def calculate_grade(percentage):
    if percentage > 90 and percentage <= 100:
        return 'A+'
    elif percentage > 80 and percentage <= 90:
        return 'A'
    elif percentage > 70 and percentage <= 80:
        return 'B+'
    elif percentage > 60 and percentage <= 70:
        return 'B'
    elif percentage > 50 and percentage <= 60:
        return 'C'
    elif percentage > 40 and percentage <= 50:
        return 'D'
    elif percentage > 0 and percentage <= 40:
        return 'Fail'
    else:
        return 'Invalid Percentage'

def marksheet():
    print("-------------------------- All India Institute of Fire Technology and Safety Management---------------------\n")
    print("Associated with Technical and Paramedical Education Council An Autonomous Institution by Goverment Of India \n")
    
    name = input("Enter name of Student - ")
    reg_number = input("Enter registration number  - ")
    enroll_number = input("Enter enrollment number - ")
    print("Course Name | Diploma in Fire and Safety Management \nCourse Code | DFS012\n")
    
    print("                 Subject Code     |           Subject Name                    Max Marks     |   Obtained Marks")
    subjects = [" DFS012-101  | Fire and Science and Technology               100       |       ",
                " DFS012-102  | Fire Prevention and Investigation             100       |       ",
                " DFS012-103  | Fire Protection and Survey                    100       |       ",
                " DFS012-104  | Fire Extinction and Control                   100       |       ",
                " DFS012-105  | Industrial Safety Management                  100       |       "]
    practicals = [" DFS012-106  | Practical 1                                   100       |       ",
                  " DFS012-107  | Practical 2                                   100       |       ",
                  " DFS012-108  | Practical 3                                   100       |       "]
    
    total_subject_marks = 0
    max_subject_marks = len(subjects) * 100
    total_practical_marks = 0
    max_practical_marks = len(practicals) * 100
    
    input_marks = []
    
    for subject in subjects:
        marks = int(input(f"Enter marks for |    {subject} "))
        input_marks.append(marks)
        total_subject_marks += marks
        
    for practical in practicals:
        marks = int(input(f"Enter marks for |    {practical} "))
        input_marks.append(marks)
        total_practical_marks += marks
  

    total_marks = total_subject_marks + total_practical_marks
    max_total_marks = max_subject_marks + max_practical_marks
    percentage = calculate_percentage(total_marks, max_total_marks)
    grade = calculate_grade(percentage)
    print("\n")
    
    print("                                                MARKSHEET                                                   \n")
    print("--------------------------- ALL INDIA INSTITUTE OF FIRE TECHNOLOGY AND SAFETY MANAGEMENT -------------------\n")
    print("Associated with Technical and Paramedical Education Council An Autonomous Institution by Goverment Of India \n")
    print("                                         ANNUAL STATEMENT OF MARKS                                          \n")
    print(f"Name: {name}")
    print(f"Enrollment Number: {enroll_number}")
    print("Course Name | Diploma in Fire and Safety Management \nCourse Code | DFS012\n")
    
    print("\n------------------------------------------------------------------------------------------------------------\n")
    print("Subject Code |         Subject Name                      Max Marks     |   Obtained Marks")
    for i, subject in enumerate(subjects, start=1):
        print(f"{subject} {input_marks[i - 1]}")
    for i, practical in enumerate(practicals, start=1):
        print(f"{practical} {input_marks[len(subjects) + i - 1]}")
    
    print("\n---------------------------------------------------- Results -----------------------------------------------")
    print(f"Total Marks: {total_marks} / {max_total_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    
    print("\n------------------------------------------------------------------------------------------------------------")
    
marksheet()
input("Press Enter to exit...")
