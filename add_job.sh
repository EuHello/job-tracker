#!/bin/bash
# add_job.sh

intro="./peptalk.sh"
if [ -e "$intro" ]; then
  source peptalk.sh
fi

echo "Enter jobs applied in this format: date(blank=today or yyyy-mm-dd); job title; company name"
read -r inputs
echo "$inputs" >> "data.csv"

cmd1=("maintain.py" "-m")
echo "Running ${cmd1[*]}"
python3 "${cmd1[@]}"
