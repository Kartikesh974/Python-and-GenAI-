import pprint

def k1():
    network_parameters = {} 
    return network_parameters

def k2(network_parameters):
    with open('network.cfg','r') as fobj:
        for var in fobj.readlines():
            var = var.strip()
            K,V = var.split("=")
            network_parameters[K] = V 
    return network_parameters

def k3(network_parameters):
    pprint.pprint(network_parameters)

def k4(network_parameters):
    network_parameters['Interface'] = 'eth1'
    network_parameters['bootproto'] = 'static'
    network_parameters['onboot'] = 'yes'
    network_parameters['IPADD'] = '192.168.1.10'
    network_parameters['PREFIX'] = 24
    network_parameters['DNS1']= '122.33.344.555'
    return network_parameters

def k5(network_parameters):
    with open('new_network.cfg','w') as wobj:
        for var in network_parameters:
            wobj.write(f'{var} = {network_parameters.get(var)}\n')


rv1 = k1()
rv2 = k2(rv1)
k3(rv2)
rv3 = k4(rv2)
print("\nUpdated network details:-")
k3(rv3) 
k5(rv3)