hosts = {} 
print(f"No of elements in the dict:{len(hosts)}") # display no of elements in the dict

count = 0
while(count < 5):
    k = input("Enter a hostname:")
    ip = input("Enter a IP address:")
    hosts[k] = ip # add the hostname and IP address to the dict
    count += 1

print(f"No of elements in the dict:{len(hosts)}") # display no of elements in the dict

for var in hosts:
    print(f"Hostname:{var}\t IP Address:{hosts[var]}") # iterate through the dict and display each hostname and IP address

k = input("Enter a hostname:")
if h in hosts:
    hosts[k] = "127.0.0.1" # Modify the IP address for the existing hostname 
else:
    print("sorry hostname {k} is not exists")
    hosts[k] = "127.0.0.1"
    print("Updated dict")

for var in hosts:
    print(f"\nHostname:{var}\t IP Address:{hosts[var]}")