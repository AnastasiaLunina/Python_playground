# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for each in student_scores.keys():
    score = student_scores[each]
    if score > 90:
        student_grades[each] = 'Outstanding'
    elif score > 80:
        student_grades[each] = 'Exceeds Expectations'
    elif score > 70:
        student_grades[each] = 'Acceptable'
    else:
        student_grades[each] = 'Fail'
    

print(student_grades)