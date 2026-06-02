# Part 5 – CRUD Operations Using DynamoDB

## Objective

The objective of this task is to implement CRUD (Create, Read, Update, Delete) operations on the `student_performance` DynamoDB table using Python and Boto3.

These operations enable the application to manage student performance records efficiently.

---

# Services Used

- Amazon DynamoDB
- Python
- Boto3

---

# DynamoDB Table

## Table Name

student_performance

## Primary Key

| Attribute  | Key Type      |
| ---------- | ------------- |
| student_id | Partition Key |

---

# Project Structure

```text
Serverless_Student_Performance_Analytics_System
│
├── scripts
│   ├── create_student.py
│   ├── read_student.py
│   ├── update_student.py
│   └── delete_student.py
│
└── docs
    └── part5_crud_operations.md
```

---

# Create Operation

## Purpose

Insert a new student record into the DynamoDB table.

## File

```text
scripts/create_student.py
```

## Implementation

The script uses the `put_item()` method to insert a new record into the table.

### Sample Record

| Attribute               | Value |
| ----------------------- | ----- |
| student_id              | S1001 |
| weekly_self_study_hours | 12.5  |
| attendance_percentage   | 90    |
| class_participation     | 8     |
| total_score             | 88    |
| grade                   | B     |
| performance_category    | Good  |

## Result

The student record was successfully inserted into DynamoDB.

---

# Read Operation

## Purpose

Retrieve a student record using the student_id.

## File

```text
scripts/read_student.py
```

## Implementation

The script uses the `get_item()` method to retrieve a record from DynamoDB.

### Search Key

```text
student_id = S1001
```

## Result

The student record was successfully retrieved and displayed.

---

# Update Operation

## Purpose

Update existing student performance information.

## File

```text
scripts/update_student.py
```

## Updated Fields

- weekly_self_study_hours
- attendance_percentage
- class_participation
- total_score
- grade

## Implementation

The script uses the `update_item()` method with an UpdateExpression.

### Updated Values

| Attribute               | New Value |
| ----------------------- | --------- |
| weekly_self_study_hours | 15        |
| attendance_percentage   | 95        |
| class_participation     | 9         |
| total_score             | 92        |
| grade                   | A         |

## Result

The student record was successfully updated.

---

# Delete Operation

## Purpose

Remove a student record from DynamoDB.

## File

```text
scripts/delete_student.py
```

## Implementation

The script uses the `delete_item()` method to remove the specified record.

### Deleted Record

```text
student_id = S1001
```

## Result

The student record was successfully deleted from the table.

---

# Testing Performed

The CRUD operations were tested in the following sequence:

1. Create a student record.
2. Read the inserted record.
3. Update the student information.
4. Read the updated record.
5. Delete the record.
6. Verify deletion by attempting another read.

---

# Test Results

| Operation | Status  |
| --------- | ------- |
| Create    | Success |
| Read      | Success |
| Update    | Success |
| Delete    | Success |

All CRUD operations executed successfully and produced the expected results.

---

# Outcome

The DynamoDB CRUD functionality was successfully implemented using Python and Boto3.

The system can now:

- Insert student records.
- Retrieve student records using student_id.
- Update existing student information.
- Delete student records.

This completes Part 5 – CRUD Operations.
