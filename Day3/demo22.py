a = open('C:\\users\\karth\\emp.csv','r')
L = a.readlines()
a.close()

print(type(L),len(L))
print("") # empty line
print("Display file content")
print(L)