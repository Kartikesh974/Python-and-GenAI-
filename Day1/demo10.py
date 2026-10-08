pin = 1234
count = 0
while(count < 3):
    user_pin = int(input("Enter your pin no: "))
    count += 1
    if(user_pin == pin):
        print(f"Pin No is Valid - count is:{count}")
        break

if pin != user_pin:
    print("Pin is blocked")
