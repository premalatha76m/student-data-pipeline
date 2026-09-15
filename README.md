# Student Data Processing Pipeline

## Project Description

A Python-based data processing pipeline that reads student data from a CSV file, cleans and validates the data, handles missing and invalid values, transforms the data, calculates average marks and grades, and generates a structured output file.

## Features

- Read student data from CSV
- Clean and validate data
- Handle missing values
- Convert data types
- Handle invalid marks
- Handle marks outside the valid range
- Calculate average marks
- Generate student grades
- Configuration management using JSON
- Logging of pipeline activities
- Generate processed CSV output

## Technologies Used

- Python
- Pandas
- CSV
- JSON
- Logging
- GitHub

## Project Structure

```text
student-data-pipeline/
├── config/
│   └── config.json
├── data/
│   ├── input/
│   │   └── students.csv
│   └── output/
├── src/
│   ├── cleaner.py
│   ├── logger.py
│   ├── pipeline.py
│   ├── reader.py
│   └── transformer.py
├── .gitignore
├── README.md
└── requirements.txt
