import time

def pin_t(arg):
    pin = 1234
    if(int(arg) == pin):
        return 1
    
for var in range(3):
    p = input('Enter a pin Number:')
    if(pin_t(p)):
        print(f'Success - input pin is matched entry date/time is: {time.ctime()}')
        break
    else:
        print(f'Sorry input pin number is not matched: date/time is: {time.ctime()}')
    

if(var >2):
    print(f'pin is blocked - date/time is:{time.ctime()}')