elogin_status = True

ename = input("Employee name: ")

eage = input(f"Enter {ename} age: ")

ecost = input(f"Enter {ename} salary: ")

tax = float(ecost) * 0.18 
gs = tax + float(ecost)

print(f'''Employee Name:{ename}
---------------------------------------
{ename} Age is:{eage}
---------------------------------------
{ename} Salary is:{ecost}
---------------------------------------
{ename} Login Status :{elogin_status}
-----------------------------------------
Tax :{tax}
-----------------------------------------
Total Salary is:{gs}
----------------------------------------''')