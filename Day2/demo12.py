Emp = ['101,john,sales,1000','102,ram,prod,2000','103,raju,hr,3000','104,bibu,sales,4000']

total = 0
for var in Emp:
    eid,ename,edept,ecost = var.split(',')
    print(f"Emp Name:{ename.title()}\t Emp Dept:{edept.upper()}") # display empName in title case and emp department in upper case
    total = total +int(ecost)
    
print(f"\nTotal Salary:{total}") # display the total salary
