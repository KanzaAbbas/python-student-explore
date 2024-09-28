

def get_student_data():

    student_data = {
                "Mahir": {"age": "18", "grades": [54,87,90]},
                "Malaa": {"age": "16", "grades": [21,78,97]},
                "Mahi": {"age": "19", "grades": [45,81,89]},
                "Ebaad": {"age": "21", "grades": [56,78,96]},
                "Birbeel": {"age": "17", "grades": [34,60,88]}         
                } 
    return student_data

def check_student_data(student_data):
    print("Student Data Structure: ")
    for student, details in student_data.items():
        print(f"Student: {student}, Details: {details}")

student_data = get_student_data()
check_student_data(student_data)

def filter_students(student_data, threshold):
    filtered_students = []

    for student, details in student_data.items():
        grades = details.get("grades", [])
        
        avg = sum(grades) / len(grades) 

        print(f"Student: {student}, Grades: {grades},Average: {round(avg,2)}")
        

        if avg > threshold:
            filtered_students.append(student)

    return filtered_students

def calc_avg_grade(student_list):

    total_grade = 0
    total_students = len(student_list)

    for student in student_list:
        grades = student_data[student]["grades"]
        avg_grade = sum(grades) / len(grades)
        total_grade += sum(grades)

    if total_students > 0:
        avg_grade = total_grade / total_students
    else:
        avg_grade = 0

    return avg_grade
    
def sort_students(student_data):

    #sorts a list of students by their age

    students_with_age = []

    for student, details in student_data.items():
        age = details.get("age")
        students_with_age.append((student, age))
    
    n = len(students_with_age)
    for i in range(n):
        for j in range(0, n - i - 1):
            if students_with_age[j][1] > students_with_age[j+1][1]:
                students_with_age[j], students_with_age[j+1] = students_with_age[j+1], students_with_age[j] 
    
    sorted_students = []
    for student,age in students_with_age:
        sorted_students.append(student)
    
    return sorted_students

