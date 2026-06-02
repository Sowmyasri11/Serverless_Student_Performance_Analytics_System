import boto3

dynamodb = boto3.resource(
    'dynamodb',
    region_name='ap-southeast-2'
)

table = dynamodb.Table('student_performance')

student_id = "S1001"

response = table.get_item(
    Key={
        'student_id': student_id
    }
)

if 'Item' in response:
    print("Student Record Found:")
    print(response['Item'])
else:
    print("Student Record Not Found")