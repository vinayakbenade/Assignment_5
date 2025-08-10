student_dict = {'vinayak': 10 , 'Anusha': 25 }
student_name = input("enter the student name:")
if student_name in student_dict:
    print(f"{student_name}'s", 'marks:', student_dict[student_name])
else:
    print("student not found")