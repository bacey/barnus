import xmlrpc.client

#SERVER_IP = '192.168.0.19'
SERVER_IP = 'localhost'

s = xmlrpc.client.ServerProxy(f'http://{SERVER_IP}:8000')
print(s.pow(2,3))  # Returns 2**3 = 8
print(s.hoppala())  # Returns 5*2 = 10

# Print list of available methods
print(s.system.listMethods())