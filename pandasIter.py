import pandas

student_dict = {
    "students": ['Alex', 'Adem', 'Cathy', 'anesthesia'],
    "scores": [98, 84, 75, 99]
}

student_dict_df = pandas.DataFrame(student_dict)

for(index, row) in student_dict_df.iterrows():
    print(row.students)