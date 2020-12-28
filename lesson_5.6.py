subjects = {}

with open('task_6.txt', "r") as f_obj:
    for line in f_obj:
        subject, lecture, practice, lab = line.split()
        subjects[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subjects}')