import pprint

network_parameters = {}

with open('network.cfg','r') as a:
    for var in fobj.readlines():
        var = var.strip()
        K,V = var.split("=")
        network_parameters[K] = V 
        
        
pprint.pprint(network_parameters)

network_parameters['Interface'] = 'eth1'
network_parameters['bootproto'] = 'static'
network_parameters['onboot'] = 'yes'
network_parameters['IPADD'] = '192.168.1.10'
network_parameters['PREFIX'] = 24
network_parameters['DNS1']= '122.33.344.555'

print('\nUpdated Dict details:-')
pprint.pprint(network_parameters)

with open('new_network.cfg','w') as a:
    for var in network_parameters:
        a.write(f'{var} = {network_parameters.get(var)}\n')