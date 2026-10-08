appName = input('Enter app name: ')

if(appName == "flask"):
    port = 5000
elif(appName == "fastAPI"):
    port = 8080
elif(appName == "prometheus"):
    port = 9090
else:
    appName = "web2.0"
    port = 8000

print(f"App Name is:{appName} Running Port Number is:{port}")