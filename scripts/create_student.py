import boto3
from decimal import Decimal

dynamodb = boto3.resource(
    'dynamodb',
    region_name='ap-southeast-2'
)

table = dynamodb.Table('student_performance')

response = table.put_item(
    Item={
        'student_id': 'S1001',
        'weekly_self_study_hours': Decimal('12.5'),
        'attendance_percentage': Decimal('90.0'),
        'class_participation': Decimal('8.0'),
        'total_score': Decimal('88.0'),
        'grade': 'B',
        'performance_category': 'Good'
    }
)

print("Student record inserted successfully")
print(response)