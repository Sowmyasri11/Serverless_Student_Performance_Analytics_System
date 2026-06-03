import csv
import random

with open('student_performance_200.csv', 'w', newline='') as file:

    writer = csv.writer(file)

    writer.writerow([
        'student_id',
        'weekly_self_study_hours',
        'attendance_percentage',
        'class_participation',
        'total_score',
        'grade'
    ])

    for i in range(1, 201):

        score = round(random.uniform(40, 100), 1)

        if score >= 90:
            grade = 'A'
        elif score >= 75:
            grade = 'B'
        elif score >= 60:
            grade = 'C'
        else:
            grade = 'D'

        writer.writerow([
            str(i),
            round(random.uniform(2, 20), 1),
            round(random.uniform(60, 100), 1),
            round(random.uniform(1, 5), 1),
            score,
            grade
        ])

print("200 student records generated successfully")