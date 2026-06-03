import boto3
import json
from decimal import Decimal

dynamodb = boto3.resource(
    'dynamodb',
    region_name='ap-southeast-2'
)

table = dynamodb.Table('student_performance')

response = table.scan()

items = response['Items']


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


with open(
    'exports/student_performance.json',
    'w'
) as file:

    json.dump(
        items,
        file,
        indent=4,
        cls=DecimalEncoder
    )

print("JSON export completed successfully")