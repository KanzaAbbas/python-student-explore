from module import get_student_data, filter_students, calc_avg_grade, sort_students

student_data = get_student_data()

threshold = 70
filtered_students = filter_students(student_data, threshold)
print("Filtered Students: ", filtered_students)

avg = calc_avg_grade(filtered_students)

sorted_students = sort_students(student_data)


print("Average Grade: ", round(avg,2))
print("Sorted Students By Age: ", sorted_students)