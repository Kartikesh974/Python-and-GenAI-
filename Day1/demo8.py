app_name = input('Enter app name: ')

if app_name in 'crm application running':
    port = 5000
else:
    port = 8080
    
print(f"App Name is:{app_name} Running Port Number is:{port}")