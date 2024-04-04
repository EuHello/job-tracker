## job-tracker
Sick of keeping track of job application via spreadsheet?  
Prefer Command Line?  

This is a few simple scripts(bash, python) to track your job application, entering data via bash.  

### Pre-requisites
1. Bash
2. Python


### Getting Started
Run script to start entering data
```bash
$ ./add_job.sh
"Enter jobs applied in this format: date(blank=today or yyyy-mm-dd); job title; company name"  
# Sample job with no date, i.e. today
$ ; Junior Software Engineer; Big Company Dune

or 

# Sample job with date
$ 2024-04-01; Junior Software Engineer; Big Company Dune
```


Find previous job applications by *company name*
```bash
$ python3 find.py -c "Big Company"
```

Find previous job applications by *job title*
```bash
$ python3 find.py -j "engineer"
```