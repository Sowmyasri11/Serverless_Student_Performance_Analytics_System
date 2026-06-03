import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource(
    'dynamodb',
    region_name ='ap-southeast-2'
)

table = dynamodb.Table('student_performance')

response = table.scan(
    FilterExpression = Attr('performance_category').eq('Excellent')
)

students = response['Items']

print("Excellent Students\n")

for student in students:
    print(student)
