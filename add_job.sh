#!/bin/bash
# add_job.sh

echo "Enter jobs applied in this format: date(blank=today or yyyy-mm-dd), job title, company name"
read inputs
echo "$inputs" >> "data.csv"

echo "Running maintain.py"
python3 maintain.py
