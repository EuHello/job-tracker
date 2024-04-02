#!/bin/bash
# add_job.sh

source peptalk.sh

echo "Enter jobs applied in this format: date(blank=today or yyyy-mm-dd); job title; company name"
read inputs
echo "$inputs" >> "data.csv"

cmd1="maintain.py -m"
echo "Running $cmd1"
python3 $cmd1
