A = open('C:\\users\\karth\\emp.csv','r')
s = A.read()
A.close()

print(type(s),len(s))
print("") 
print("Display file content")
print(s)s