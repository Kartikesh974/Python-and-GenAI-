host = []
print(f"Number of elements in the list:{len(host)}") # display no of elements in the list

c = 0
while c < 5:
    h = input("Enter a hostname:")
    host.append(h) # append the hostname to the list
    c = c + 1

print(f"\nNumber of elements in the list:{len(host)}") # display no of elements in the list

for var in host:
    print(var) # iterate through the list and display each hostname
    

host_name  = input("Enter a hostname:")
if host_name in host:
    host[-1] = host_name 
else:
    host.append(host_name) # add the hostname to the list

print("\n") # empty line
for var in host:
    print(var)
    