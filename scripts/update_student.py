import boto3
from decimal import Decimal

dynamodb = boto3.resource(
    'dynamodb',
    region_name='ap-southeast-2'
)

table = dynamodb.Table('student_performance')

student_id = "S1001"

response = table.update_item(
    Key={
        'student_id': student_id
    },
    UpdateExpression="""
        SET weekly_self_study_hours = :h,
            attendance_percentage = :a,
            class_participation = :p,
            total_score = :s,
            grade = :g
    """,
    ExpressionAttributeValues={
        ':h': Decimal('15.0'),
        ':a': Decimal('95.0'),
        ':p': Decimal('9.0'),
        ':s': Decimal('92.0'),
        ':g': 'A'
    },
    ReturnValues='UPDATED_NEW'
)

print("Student record updated successfully")
print(response['Attributes'])