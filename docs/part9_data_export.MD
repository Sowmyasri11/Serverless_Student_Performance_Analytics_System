# Part 9 – Data Export

## Objective

The objective of this task is to export student performance records stored in Amazon DynamoDB into external file formats and store the exported files in Amazon S3.

The system should:

- Retrieve student records from DynamoDB.
- Export the records into JSON format.
- Export the records into CSV format.
- Upload the exported files to Amazon S3.
- Verify successful storage of exported files.

---

## Services Used

- Amazon DynamoDB
- Amazon S3
- Python
- Boto3

---

## Project Structure

```text
Serverless_Student_Performance_Analytics_System
│
├── exports
│   ├── student_performance.json
│   └── student_performance.csv
│
├── scripts
│   ├── export_to_json.py
│   └── export_to_csv.py
│
└── docs
    └── part9_data_export.md
```

---

## Source Table

### DynamoDB Table

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

# Export to JSON

## Objective

Export all student performance records from DynamoDB into a JSON file.

### File

```text
scripts/export_to_json.py
```

### Process

1. Connect to DynamoDB using Boto3.
2. Read all records using the Scan operation.
3. Convert Decimal values into JSON-compatible numeric values.
4. Write records into a JSON file.

### Output File

```text
exports/student_performance.json
```

### Sample Output

```json
[
  {
    "student_id": "1",
    "weekly_self_study_hours": 18.5,
    "attendance_percentage": 95.6,
    "class_participation": 3.8,
    "total_score": 97.9,
    "grade": "A",
    "performance_category": "Excellent"
  }
]
```

---

# Export to CSV

## Objective

Export all student performance records from DynamoDB into a CSV file.

### File

```text
scripts/export_to_csv.py
```

### Process

1. Retrieve records from DynamoDB.
2. Create a CSV file.
3. Write column headers.
4. Write all student records into the file.

### Output File

```text
exports/student_performance.csv
```

### Sample Output

```csv
student_id,weekly_self_study_hours,attendance_percentage,class_participation,total_score,grade,performance_category
1,18.5,95.6,3.8,97.9,A,Excellent
2,10.0,88.5,3.0,82.5,B,Good
```

---

# Uploading Exported Files to Amazon S3

## S3 Bucket

```text
student-performance-datasets
```

### Uploaded Files

```text
exports/student_performance.json
exports/student_performance.csv
```

### Upload Method

The exported JSON and CSV files were uploaded to the Amazon S3 bucket using the AWS Management Console.

---

# Verification

## DynamoDB Verification

The student_performance table was scanned successfully and all records were retrieved.

## JSON Verification

The generated JSON file was opened and validated to ensure that all records were exported correctly.

## CSV Verification

The generated CSV file was opened and validated to ensure that all records were exported correctly.

## S3 Verification

The uploaded files were verified in the S3 bucket after successful upload.

---

# Results

| Validation Check                | Status  |
| ------------------------------- | ------- |
| Records Retrieved from DynamoDB | Success |
| JSON File Generated             | Success |
| CSV File Generated              | Success |
| JSON Uploaded to S3             | Success |
| CSV Uploaded to S3              | Success |
| Files Verified in S3            | Success |

---

# Benefits of Data Export

- Enables backup of student records.
- Supports data sharing and reporting.
- Facilitates integration with external analytics tools.
- Provides portable storage formats for future use.

---

# Outcome

Student performance records were successfully exported from Amazon DynamoDB into JSON and CSV formats.

The exported files were uploaded and stored in Amazon S3, providing a portable and reusable dataset for reporting, analytics, and backup purposes.

This completes Part 9 – Data Export.
