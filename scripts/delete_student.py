import boto3

dynamodb = boto3.resource(
    'dynamodb',
    region_name='ap-southeast-2'
)

table = dynamodb.Table('student_performance')

student_id = "S1001"

table.delete_item(
    Key={
        'student_id': student_id
    }
)

print("Student record deleted successfully")