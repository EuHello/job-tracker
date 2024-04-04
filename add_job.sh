#!/bin/bash
# add_job.sh

intro="peptalk.sh"
if [ -e "$intro" ]; then
  source peptalk.sh
fi

backup_dir="./archive"
if [ ! -d "$backup_dir" ]; then
  mkdir $backup_dir
fi

data_file="data.csv"
if [ ! -f "$data_file" ]; then
  echo "Date;Job Title;Company" > $data_file
fi

echo "Enter jobs applied in this format: date(blank=today or yyyy-mm-dd); job title; company name"
read -r inputs
echo "$inputs" >> $data_file

cmd1=("maintain.py" "-m")
echo "Running ${cmd1[*]}"
python3 "${cmd1[@]}"


backup_date=$(date -d yesterday +%y%m%d)
backup_filepath="${backup_dir}/${backup_date}_${data_file}"
if [ ! -f "$backup_filepath" ]; then
  echo "backing up file to $backup_filepath"
  cp "$data_file" "$backup_filepath"
fi