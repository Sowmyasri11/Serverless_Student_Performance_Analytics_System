# Part 7 – Global Secondary Index (GSI)

## Objective

The objective of this task is to improve query performance in DynamoDB by creating a Global Secondary Index (GSI).

The GSI allows efficient retrieval of:

- Students belonging to a specific grade.
- Top-performing students based on total score.
- Highest-scoring students within a grade category.

---

## Services Used

- Amazon DynamoDB
- Python
- Boto3

---

## DynamoDB Table Details

### Table Name

```text
student_performance
```

### Primary Key

| Attribute  | Key Type      |
| ---------- | ------------- |
| student_id | Partition Key |

---

## Why Global Secondary Index is Required

The primary key of the table is:

```text
student_id
```

Using the primary key, records can only be queried efficiently by student ID.

However, the project requirements involve retrieving:

- Students belonging to Grade A.
- Students with the highest scores.

Since these queries depend on:

```text
grade
total_score
```

a Global Secondary Index (GSI) was created.

---

# Global Secondary Index Configuration

### Index Name

```text
grade-total_score-index
```

### Index Keys

| Key Type      | Attribute   | Data Type |
| ------------- | ----------- | --------- |
| Partition Key | grade       | String    |
| Sort Key      | total_score | Number    |

### Projection Type

```text
ALL
```

This projection type ensures that all table attributes are available through the index.

---

## Project Structure

```text
Serverless_Student_Performance_Analytics_System
│
├── scripts
│   ├── query_grade_a_students.py
│   └── query_highest_Scores.py
│
└── docs
    └── part7_secondary_index.md
```

---

# Query 1 – Retrieve Top Students in Grade A

## Objective

Retrieve all students belonging to Grade A and display them in descending order of total score.

### File

```text
scripts/query_grade_a_students.py
```

### Implementation

```python
response = table.query(
    IndexName='grade-total_score-index',
    KeyConditionExpression=Key('grade').eq('A'),
    ScanIndexForward=False
)
```

### Explanation

- Uses the Global Secondary Index.
- Filters records where grade = A.
- Sorts results by total_score in descending order.

---

# Query 2 – Retrieve Highest Scoring Students

## Objective

Retrieve the highest-scoring students from Grade A.

### File

```text
scripts/query_highest_Scores.py
```

### Implementation

```python
response = table.query(
    IndexName='grade-total_score-index',
    KeyConditionExpression=Key('grade').eq('A'),
    ScanIndexForward=False,
    Limit=3
)
```

### Explanation

- Uses the Global Secondary Index.
- Retrieves Grade A students.
- Sorts by total_score descending.
- Returns only the top 3 students.

---

# Testing Performed

The following scripts were executed successfully.

| Script                    | Purpose                           | Status  |
| ------------------------- | --------------------------------- | ------- |
| query_grade_a_students.py | Retrieve Grade A students         | Success |
| query_highest_Scores.py   | Retrieve highest-scoring students | Success |

---

# Sample Output

### Highest Scoring Students

| Rank | Student ID | Total Score | Grade |
| ---- | ---------- | ----------- | ----- |
| 1    | 1          | 97.9        | A     |
| 2    | 9          | 96.4        | A     |
| 3    | 5          | 91.2        | A     |

The results were returned in descending order of total score using the GSI sort key.

---

# Benefits of Using GSI

- Faster query execution.
- Eliminates full table scans.
- Enables efficient retrieval based on non-primary-key attributes.
- Supports analytical and reporting requirements.

---

# Outcome

A Global Secondary Index was successfully created and configured on the student_performance table.

The index enabled efficient retrieval of:

- Grade-wise student records.
- Top-performing students.
- Highest-scoring students.

This completes Part 7 – Global Secondary Index (GSI).
