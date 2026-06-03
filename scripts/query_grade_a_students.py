import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource(
    'dynamodb',
    region_name='ap-southeast-2'
)

table = dynamodb.Table('student_performance')

response = table.query(
    IndexName='grade-total_score-index',
    KeyConditionExpression=Key('grade').eq('A'),
    ScanIndexForward=False
)

print("Top Students in Grade A\n")

for student in response['Items']:
    print(student)