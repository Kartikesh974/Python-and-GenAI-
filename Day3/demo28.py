import time

def pin_test():
    a = open('pin_history.log','a')
    pin = 2000
    count = 0
    while(count < 3):
        p = input('Enter a pin No:')
        count = count + 1
        if(int(p) == pin):
            print(f'Success - {count}')
            a.write(f'Success - {count} pin input date/time:{time.ctime()}\n')
            break
        else:
            a.write(f'Failed - user input pin:{p} date/time:{time.ctime()}\n')
    if(int(p) != pin):
        print('Pin is blocked')
        fobj.write(f'Pin is blocked - {time.ctime()}\n')
    a.close()
    
pin_test()