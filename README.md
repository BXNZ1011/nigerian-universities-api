# Nigerian Universities API

## 📖 Overview
This repository provides a structured dataset of Nigerian universities, polytechnics, and colleges.  
The data is available in multiple formats (JSON, SQL, CSV) to make it easy to integrate into applications, research, and civic tech projects.

## 📂 Contents
- `data/universities.json` → JSON dataset
- `data/universities.sql` → SQL insert script
- `data/universities.csv` → CSV dataset
- `docs/usage.md` → Documentation and usage examples

## 🚀 Usage

### SQL
in sql
\i universities/universities.sql
SELECT * FROM universities WHERE type='Federal';

### CSV
in python 
import pandas as pd
df = pd.read_csv("universities/universities.csv")
print(df.head())

### JSON
Load the dataset in Python:
```python
import json
with open("data/universities.json") as f:
    universities = json.load(f)
    print(universities[0]["name"])
