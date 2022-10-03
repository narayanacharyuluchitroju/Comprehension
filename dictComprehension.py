import random

names = ['Alex', 'Adem', 'Cathy', 'anesthesia']

student_dict = {name: random.randint(1, 100) for name in names}
passed_student = {name: scores for (name, scores) in student_dict.items() if scores > 75}
print(student_dict)
print(passed_student)
