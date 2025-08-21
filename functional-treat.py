marks = [56, 78, 45, 89, 65, 98, 35, 21, 67, 72, 81, 59, 92, 74, 88, 62, 49, 33, 77, 69]

total_students = len(marks)

highest = max(marks)
lowest = min(marks)

average = sum(marks) / total_students

passed = len([m for m in marks if m >= 33])
failed = total_students - passed

pass_percentage = (passed / total_students) * 100

sorted_marks = sorted(marks)

grade_A = len([m for m in marks if m >= 85])
grade_B = len([m for m in marks if 70 <= m < 85])
grade_C = len([m for m in marks if 50 <= m < 70])
grade_D = len([m for m in marks if 33 <= m < 50])
grade_F = len([m for m in marks if m < 33])


print(f"Total Students: {total_students}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")
print(f"Average Marks: {average:.1f}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Pass Percentage: {pass_percentage:.1f}%")
print(f"Sorted Marks: {sorted_marks}")
print(f"Grade A: {grade_A} Students")
print(f"Grade B: {grade_B} Students")
print(f"Grade C: {grade_C} Students")
print(f"Grade D: {grade_D} Students")
print(f"Grade F: {grade_F} Students")