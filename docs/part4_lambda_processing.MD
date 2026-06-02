# Part 4 – Lambda Processing

## Objective

The objective of this task is to automate the processing of student performance datasets uploaded to Amazon S3 using AWS Lambda.

The Lambda function reads the uploaded dataset, calculates the performance category for each student, and stores the processed records in Amazon DynamoDB.

---

## Services Used

- AWS Lambda
- Amazon S3
- Amazon DynamoDB
- IAM
- Python
- Boto3

---

## Workflow Architecture

```text
Student Dataset Upload
          |
          v
      Amazon S3
          |
          | (S3 Event Trigger)
          v
     AWS Lambda
          |
          | Process Records
          v
   Amazon DynamoDB
```

---

## Lambda Function Responsibilities

The Lambda function performs the following tasks:

1. Receives an S3 upload event.
2. Identifies the uploaded CSV file.
3. Reads the file from Amazon S3.
4. Parses the CSV data.
5. Extracts student records.
6. Calculates the performance category based on the total score.
7. Inserts processed records into DynamoDB.
8. Returns the number of records processed.

---

## Performance Category Rules

| Total Score | Performance Category |
| ----------- | -------------------- |
| >= 90       | Excellent            |
| 75 – 89     | Good                 |
| 60 – 74     | Average              |
| < 60        | Poor                 |

---

## Input Dataset Structure

The uploaded CSV file contains the following attributes:

| Attribute               |
| ----------------------- |
| student_id              |
| weekly_self_study_hours |
| attendance_percentage   |
| class_participation     |
| total_score             |
| grade                   |

The Lambda function generates an additional attribute:

| Generated Attribute  |
| -------------------- |
| performance_category |

---

## DynamoDB Table

### Table Name

```text
student_performance
```

### Attributes Stored

- student_id
- weekly_self_study_hours
- attendance_percentage
- class_participation
- total_score
- grade
- performance_category

---

## Lambda Implementation

### S3 File Processing

The Lambda function retrieves the uploaded file using:

```python
response = s3.get_object(
    Bucket=bucket_name,
    Key=file_key
)
```

### CSV Parsing

The CSV file is parsed using Python's built-in CSV module:

```python
csv_reader = csv.DictReader(StringIO(file_content))
```

### Performance Category Calculation

A helper function is used to classify students:

```python
def get_performance_category(total_score):
```

Categories are assigned according to the predefined score ranges.

### DynamoDB Insertion

Each processed student record is inserted into the DynamoDB table using:

```python
table.put_item(
    Item={...}
)
```

---

## Testing Performed

### Test Procedure

1. Created and deployed the Lambda function.
2. Connected Amazon S3 as the trigger source.
3. Uploaded the dataset file to the S3 bucket.
4. Verified automatic Lambda execution.
5. Confirmed records were inserted into DynamoDB.
6. Verified the generated performance_category values.

### Result

The Lambda function executed successfully after the dataset upload.

The processed student records were inserted into the DynamoDB table with the calculated performance categories.

---

## Challenges Encountered

### Initial Issue

The uploaded dataset contained a large number of records, causing:

- Lambda timeout errors
- Memory limit issues

### Resolution

Testing was performed using a smaller sample dataset to validate:

- S3 trigger functionality
- Lambda execution
- DynamoDB insertion
- Performance category calculation

The workflow executed successfully after configuration adjustments.

---

## Outcome

The serverless data processing pipeline was successfully implemented and tested.

Whenever a dataset is uploaded to Amazon S3:

1. AWS Lambda is triggered automatically.
2. Student records are processed.
3. Performance categories are calculated.
4. Records are stored in DynamoDB.

This completes the implementation of Part 4 – Lambda Processing.
