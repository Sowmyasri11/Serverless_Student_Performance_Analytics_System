# Part 1 – DynamoDB Table Design

## Objective

Create an Amazon DynamoDB table to store student performance records that will be processed by AWS Lambda after file uploads to Amazon S3.

---

## Table Name

student_performance

---

## Attributes

The table stores the following student-related information:

| Attribute Name          | Description                                         |
| ----------------------- | --------------------------------------------------- |
| student_id              | Unique identifier for a student                     |
| weekly_self_study_hours | Number of hours spent on self-study per week        |
| attendance_percentage   | Student attendance percentage                       |
| class_participation     | Participation score in classroom activities         |
| total_score             | Overall score obtained by the student               |
| grade                   | Academic grade assigned                             |
| performance_category    | Performance classification derived from total score |

---

## Primary Key Configuration

Partition Key:

student_id (String)

No Sort Key is required.

---

## Steps Performed

1. Logged in to AWS Management Console.

2. Opened Amazon DynamoDB service.

3. Selected "Create Table".

4. Entered table name as:

   student_performance

5. Configured partition key:

   student_id (String)

6. Selected On-Demand billing mode.

7. Clicked Create Table.

8. Verified that the table status became Active.

---

## Table Configuration Summary

| Setting       | Value               |
| ------------- | ------------------- |
| Table Name    | student_performance |
| Partition Key | student_id          |
| Key Type      | String              |
| Billing Mode  | On-Demand           |
| Status        | Active              |

---

## Outcome

The DynamoDB table was successfully created and is ready to receive student performance records from AWS Lambda.
