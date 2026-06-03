import boto3

dynamodb = boto3.resource(
    'dynamodb',
    region_name='ap-southeast-2'
)

table = dynamodb.Table('student_performance')

response = table.scan()

print("Total Records:", len(response['Items']))