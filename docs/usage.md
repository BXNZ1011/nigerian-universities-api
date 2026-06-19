# Usage Guide

This document shows how to use the Nigerian Universities dataset in different formats.

---

## SQL

Load the dataset in SQL:

```sql
SELECT * FROM universities
WHERE type = 'Federal';
```

## CSV

Load the dataset in Python:

```python
import pandas as pd

df = pd.read_csv("data/universities.csv")
print(df.head())
```

## JSON

Load the dataset in Python:
```python
import json

with open("data/universities.json") as f:
    universities = json.load(f)
    print(universities[0]["name"])
```

## API
🚀 How to Run It
Install Flask:
```python
 pip install flask
python api/server.py
 
