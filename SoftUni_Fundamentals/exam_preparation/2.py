company_employee = {}

while True:
    command = input()
    if command == "End":
        break
    company, employee = command.split(" -> ")
    if company not in company_employee:
        company_employee[company] = []
    if employee not in company_employee[company]:
        company_employee[company].append(employee)

for company, employees in company_employee.items():
    print(f"Company {company}:")
    for employee in employees:
        print(f"--{employee}")