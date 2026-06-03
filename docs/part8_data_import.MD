# Part 8 – Data Import

## Objective

The objective of this task is to validate the scalability of the serverless data processing pipeline by importing a large dataset and automatically storing the records in DynamoDB.

The system should:

- Accept a dataset containing at least 200 student records.
- Upload the dataset to Amazon S3.
- Trigger AWS Lambda automatically.
- Process all records.
- Store the processed records in DynamoDB.

---

## Services Used

- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- Python
- Boto3

---

## Dataset Preparation

A dataset containing more than 200 student performance records was generated for testing the serverless analytics pipeline.

### Dataset Attributes

| Attribute               |
| ----------------------- |
| student_id              |
| weekly_self_study_hours |
| attendance_percentage   |
| class_participation     |
| total_score             |
| grade                   |

### Dataset File

```text
student_performance_200.csv
```

---

## Dataset Upload

The generated dataset was uploaded to the Amazon S3 bucket.

### S3 Bucket Name

```text
student-performance-datasets
```

### Upload Process

1. Open Amazon S3 Console.
2. Navigate to the bucket:

   ```
   student-performance-datasets
   ```

3. Click **Upload**.
4. Select the file:

   ```
   student_performance_200.csv
   ```

5. Upload the file successfully.

---

## Serverless Processing Flow

```text
Student Dataset
       |
       v
Amazon S3 Bucket
       |
       v
S3 Event Notification
       |
       v
AWS Lambda Function
       |
       v
Amazon DynamoDB
```

---

## Lambda Processing

After the file was uploaded:

1. Amazon S3 generated an ObjectCreated event.
2. The event automatically triggered the Lambda function.
3. Lambda retrieved the CSV file from S3.
4. Student records were parsed.
5. Performance categories were calculated.
6. Records were inserted into the DynamoDB table.

### Performance Category Rules

| Total Score | Performance Category |
| ----------- | -------------------- |
| >= 90       | Excellent            |
| 75 - 89     | Good                 |
| 60 - 74     | Average              |
| < 60        | Poor                 |

---

## DynamoDB Storage

### Table Name

```text
student_performance
```

### Stored Attributes

- student_id
- weekly_self_study_hours
- attendance_percentage
- class_participation
- total_score
- grade
- performance_category

---

## Verification

### Lambda Verification

CloudWatch Logs were used to verify successful Lambda execution after the file upload.

The logs confirmed:

- Successful file retrieval from S3.
- Successful processing of records.
- Successful insertion into DynamoDB.

### DynamoDB Verification

The DynamoDB table was inspected using the **Explore Table Items** feature.

Verification confirmed that all uploaded student records were successfully stored.

---

## Results

| Validation Check               | Status  |
| ------------------------------ | ------- |
| Dataset Created                | Success |
| Dataset Uploaded to S3         | Success |
| Lambda Triggered Automatically | Success |
| Student Records Processed      | Success |
| Records Stored in DynamoDB     | Success |

---

## Outcome

A dataset containing more than 200 student records was successfully imported into the Serverless Student Performance Analytics System.

The upload triggered AWS Lambda automatically through Amazon S3 event notifications. Lambda processed all student records, calculated performance categories, and stored the data in DynamoDB.

This task demonstrated the ability of the serverless architecture to process large datasets efficiently and automatically without manual intervention.

---

## Conclusion

Part 8 successfully validated the end-to-end serverless workflow:

- Data uploaded to Amazon S3.
- Automatic event-based Lambda execution.
- Processing of large datasets.
- Storage of processed records in DynamoDB.

The system is now capable of handling large-scale student performance datasets using a fully serverless architecture.
