import boto3
import csv

dynamodb = boto3.resource(
    'dynamodb',
    region_name='ap-southeast-2'
)

table = dynamodb.Table('student_performance')

response = table.scan()

items = response['Items']

with open(
    'exports/student_performance.csv',
    'w',
    newline=''
) as file:

    writer = csv.writer(file)

    writer.writerow([
        'student_id',
        'weekly_self_study_hours',
        'attendance_percentage',
        'class_participation',
        'total_score',
        'grade',
        'performance_category'
    ])

    for item in items:

        writer.writerow([
            item['student_id'],
            item['weekly_self_study_hours'],
            item['attendance_percentage'],
            item['class_participation'],
            item['total_score'],
            item['grade'],
            item['performance_category']
        ])

print("CSV export completed successfully")