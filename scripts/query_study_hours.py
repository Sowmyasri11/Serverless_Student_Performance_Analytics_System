import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource(
    'dynamodb',
    region_name ='ap-southeast-2'
)

table = dynamodb.Table('student_performance')

response = table.scan(
    FilterExpression = Attr('weekly_self_study_hours').gt(10)
    
)
student = response['Items']

print("Students with study hours > 10\n")

for student in student :
    print(student)