# Part 3 – S3 Upload and Dataset Storage

## Objective

The objective of this task is to create an Amazon S3 bucket for storing student performance datasets and prepare the system for automatic processing through AWS Lambda when files are uploaded.

---

## S3 Bucket Creation

An Amazon S3 bucket was created to store student performance datasets uploaded by faculty members.

### Bucket Details

| Property      | Value                              |
| ------------- | ---------------------------------- |
| Bucket Name   | student-performance-datasets       |
| Service       | Amazon S3                          |
| Purpose       | Store student performance datasets |
| Access        | Private                            |
| Event Trigger | To be configured with AWS Lambda   |

---

## Dataset Preparation

A CSV dataset containing student performance records was prepared and stored in the project directory.

### Local File Location

```text
dataset/student_performance.csv
```

### Dataset Attributes

The dataset contains the following columns:

- student_id
- weekly_self_study_hours
- attendance_percentage
- class_participation
- total_score
- grade

The performance_category attribute is not included in the dataset because it will be calculated dynamically by the AWS Lambda function during processing.

---

## Dataset Upload

The student performance dataset was uploaded to the Amazon S3 bucket.

### Uploaded File

```text
student_performance.csv
```

### Upload Process

1. Opened the Amazon S3 bucket.
2. Selected the Upload option.
3. Chose the student_performance.csv file from the local project directory.
4. Uploaded the file successfully to the bucket.

---

## Event Notification Configuration

The project requirement specifies that an S3 event notification should trigger an AWS Lambda function whenever a new file is uploaded.

At this stage, the event notification was not configured because the Lambda function has not yet been created.

The event trigger configuration will be completed after the Lambda function is developed in the upcoming project phase.

---

## Outcome

The Amazon S3 bucket was successfully created and the student performance dataset was uploaded successfully. The bucket is now ready for integration with AWS Lambda to support automated file processing in the serverless architecture.
