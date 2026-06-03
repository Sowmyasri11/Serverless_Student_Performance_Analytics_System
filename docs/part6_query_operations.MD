# Part 6 – Query Operations Using DynamoDB

## Objective

The objective of this task is to retrieve and analyze student performance records stored in Amazon DynamoDB using different filtering conditions.

The implemented queries help identify:

- Students with high attendance.
- Students with strong self-study habits.
- Students who achieved excellent academic performance.

---

## Services Used

- Amazon DynamoDB
- Python
- Boto3

---

## DynamoDB Table Details

### Table Name

student_performance

### Primary Key

| Attribute  | Key Type      |
| ---------- | ------------- |
| student_id | Partition Key |

---

## Project Structure

```text
Serverless_Student_Performance_Analytics_System
│
├── scripts
│   ├── query_attendance.py
│   ├── query_study_hours.py
│   └── query_excellent_students.py
│
└── docs
    └── part6_query_operations.md
```

---

# Query 1 – Students with Attendance Percentage Greater Than 90

## Objective

Retrieve all students whose attendance percentage is greater than 90.

### File

scripts/query_attendance.py

### Query Condition

```python
Attr('attendance_percentage').gt(90)
```

### Description

The script scans the DynamoDB table and filters records where the attendance percentage is greater than 90.

### Result

Successfully retrieved all students with attendance percentage above 90.

---

# Query 2 – Students with Weekly Self-Study Hours Greater Than 10

## Objective

Retrieve all students who study more than 10 hours per week.

### File

scripts/query_study_hours.py

### Query Condition

```python
Attr('weekly_self_study_hours').gt(10)
```

### Description

The script scans the DynamoDB table and filters records where weekly self-study hours exceed 10.

### Result

Successfully retrieved all students whose weekly self-study hours are greater than 10.

---

# Query 3 – Students in Excellent Performance Category

## Objective

Retrieve all students classified under the Excellent performance category.

### File

scripts/query_excellent_students.py

### Query Condition

```python
Attr('performance_category').eq('Excellent')
```

### Description

The script scans the DynamoDB table and filters records whose performance category is Excellent.

### Result

Successfully retrieved all students categorized as Excellent performers.

---

## Query Processing Approach

The DynamoDB table uses only student_id as its partition key.

The attributes:

- attendance_percentage
- weekly_self_study_hours
- performance_category

are not indexed attributes.

Therefore, DynamoDB Scan operations with Filter Expressions were used to retrieve matching records.

### Generic Query Pattern

```python
response = table.scan(
    FilterExpression=<condition>
)
```

---

## Testing Performed

The following query scripts were executed and verified successfully:

| Script                      | Purpose                        | Status  |
| --------------------------- | ------------------------------ | ------- |
| query_attendance.py         | Attendance Percentage > 90     | Success |
| query_study_hours.py        | Weekly Self-Study Hours > 10   | Success |
| query_excellent_students.py | Excellent Performance Category | Success |

---

## Sample Query Conditions

| Query   | Condition                        |
| ------- | -------------------------------- |
| Query 1 | attendance_percentage > 90       |
| Query 2 | weekly_self_study_hours > 10     |
| Query 3 | performance_category = Excellent |

---

## Results

All query operations executed successfully and returned the expected student records from DynamoDB.

The queries enabled effective analysis of student performance based on attendance, study habits, and overall academic achievement.

---

## Outcome

The Student Performance Analytics System can now perform analytical queries on DynamoDB data.

Implemented capabilities include:

- Identifying students with high attendance.
- Identifying students with strong self-study habits.
- Identifying students with excellent academic performance.

This completes Part 6 – Query Operations.
