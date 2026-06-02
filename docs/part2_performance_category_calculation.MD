# Part 2 – Performance Category Calculation

## Objective

The objective of this task is to automatically calculate a student's performance category based on the total score obtained in the weekly performance report. This calculation is performed by the AWS Lambda function before storing the student record in Amazon DynamoDB.

---

## Requirement

A new attribute named `performance_category` must be generated for every student record.

### Performance Category Rules

| Total Score | Performance Category |
| ----------- | -------------------- |
| >= 90       | Excellent            |
| 75 – 89     | Good                 |
| 60 – 74     | Average              |
| < 60        | Poor                 |

---

## Purpose

The performance category provides a quick assessment of a student's overall academic performance.

Instead of manually entering the category in the uploaded dataset, the AWS Lambda function calculates it automatically using the student's total score. This approach improves consistency, reduces manual effort, and minimizes data-entry errors.

---

## Processing Logic

When a student performance file is uploaded to Amazon S3:

1. AWS Lambda is triggered automatically.
2. Lambda reads each student record from the uploaded file.
3. The `total_score` value is extracted.
4. The score is evaluated against the predefined rules.
5. The appropriate `performance_category` is assigned.
6. The complete record is stored in the DynamoDB table.

---

## Examples

| Student ID | Total Score | Performance Category |
| ---------- | ----------- | -------------------- |
| 1          | 95          | Excellent            |
| 2          | 82          | Good                 |
| 3          | 68          | Average              |
| 4          | 45          | Poor                 |

---

## Expected DynamoDB Record

Example:

```json
{
  "student_id": "S101",
  "weekly_self_study_hours": 15,
  "attendance_percentage": 92,
  "class_participation": 8,
  "total_score": 95,
  "grade": "A",
  "performance_category": "Excellent"
}
```

---

## Outcome

After implementing this logic, every student record stored in DynamoDB will contain a calculated `performance_category` attribute. This enables easier querying, filtering, and analysis of student performance data.
