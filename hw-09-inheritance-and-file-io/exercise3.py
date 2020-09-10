import csv

# Employees is a list of dictionaries.
# The keys in these dictionaries will be the header fields of your spreadsheet.
employees = [
  {
    'first_name': 'Bill',
    'last_name': 'Lumbergh',
    'job_title': 'Vice President',
    'hire_date': 1985,
    'performance_review': 'excellent'
  },
  {
    'first_name': 'Michael',
    'last_name': 'Bolton',
    'job_title': 'Programmer',
    'hire_date': 1995,
    'performance_review': 'poor'
  },
  {
    'first_name': 'Peter',
    'last_name': 'Gibbons',
    'job_title': 'Programmer',
    'hire_date': 1989,
    'performance_review': 'poor'
  },
  {
    'first_name': 'Samir',
    'last_name': 'Nagheenanajar',
    'job_title': 'Programmer',
    'hire_date': 1974,
    'performance_review': 'fair'
  },
  {
    'first_name': 'Milton',
    'last_name': 'Waddams',
    'job_title': 'Collator',
    'hire_date': 1974,
    'performance_review': 'does he even work here?'
  },
  {
    'first_name': 'Bob',
    'last_name': 'Porter',
    'job_title': 'Consultant',
    'hire_date': 1999,
    'performance_review': 'excellent'
  },
  {
    'first_name': 'Bob',
    'last_name': 'Slydell',
    'job_title': 'Consultant',
    'hire_date': 1999,
    'performance_review': 'excellent'
  }
]

for items in employees:
    items["review_finished"] = "yes"

for items in employees:
    if items['first_name'] == 'Bill' and items['last_name'] == 'Lumbergh' or items['job_title'] == 'Consultant':
        items["performance_review"] = "Poor"
    else:
        items["performance_review"] = "Excellent"
        
def main():
  # Write your code here
    with open('tps_report.csv', 'w') as csv_file:  
      dict_writer = csv.DictWriter(csv_file, employees[0].keys())
      dict_writer.writeheader()
      dict_writer.writerows(employees)
         
main()