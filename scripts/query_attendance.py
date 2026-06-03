import boto3

from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource(
    'dynamodb',
    region_name ='ap-southeast-2'
    
)

table = dynamodb.Table('student_performance')

response = table.scan(
    FilterExpression = Attr('attendance_percentage').gt(90)
    
)

students = response['Items']
print("Student with Attendace > 90 \n")

for student in students :
    print(student)