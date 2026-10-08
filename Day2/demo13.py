Emps = ['201,john,sale,2000','102,ram,prod,2000','103,raju,mr,4000','104,bibu,sales,4000']

total = 0
for var in Emps:
    if 'sales' in var:
        eid,ename,edept,ecost = var.split(',')
        print(f"Emps Name:{ename.title()}\t Emps Dept:{edept.upper()}")
        total = total +int(ecost)
    
print(f"\nTotal Salary:{total}")
