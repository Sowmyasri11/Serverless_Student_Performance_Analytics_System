import boto3
import csv
from io import StringIO
from decimal import Decimal

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table("student_performance")



def get_performance_category(total_score):
    if total_score >= 90:
        return "Excellent"
    elif total_score >= 75:
        return "Good"
    elif total_score >= 60:
        return "Average"
    else:
        return "Poor"
    
def lambda_handler(event, context):
    
    #Extract bucket name from S3 event notification
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    
    #extract uploaded file from S3
    file_key = event['Records'][0]['s3']['object']['key']
    
    #retieve uploaded file from S3
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    
    file_content = response['Body'].read().decode('utf-8')
    
    csv_reader = csv.DictReader(StringIO(file_content))
    
    processed_count= 0
    
    for row in csv_reader:
        total_Score = int(row['total_score'])
        
        performance_category = get_performance_category(total_Score)
        
        table.put_item(
            Item={
                
                'student_id': row['student_id'],
                
                'weekly_self_study_hours':
                    Decimal(row['weekly_self_study_hours']),
                    
                'attendance_percentage':
                    Decimal(row['attendance_percentage']),
                    
                'class_participation':
                    Decimal(row['class_participation']),
                    
                'total_score':
                    Decimal(str(total_score)),
                'grade':
                    row['grade'],
                'performance_category':
                    performance_category
            }
        )

        processed_count += 1

    return {
        'statusCode': 200,
        'records_processed': processed_count
    }