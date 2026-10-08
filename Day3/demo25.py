import time 

devices = ['switches','routers','ethernet','rs232']
config = {'ID':'A-123','app':'demoApp','port':3030,'fname':'/etc/app.cfg'}

a = open("r2.log","w")
for var in devices:
    a.write(f"Device name:{var}\n")

a.write("---- done -----\n")

for var in config:
    a.write(f"{var} = {config[var]}\n")

a.write("-------- Done -------\n")
a.write(f"Created on {time.ctime()}\n")
a.close()