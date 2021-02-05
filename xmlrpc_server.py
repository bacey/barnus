from xmlrpc.server import SimpleXMLRPCServer

from blinkt import set_pixel, set_brightness, show, clear, set_all, set_clear_on_exit, get_pixel

# SERVER_IP = '192.168.0.19'
# SERVER_IP = '192.168.0.73'
SERVER_IP = 'localhost'

with SimpleXMLRPCServer((SERVER_IP, 8000), allow_none=True) as server:
    server.register_introspection_functions()

    server.register_function(set_brightness)
    server.register_function(clear)
    server.register_function(show)
    server.register_function(set_all)
    server.register_function(get_pixel)
    server.register_function(set_pixel)
    server.register_function(set_clear_on_exit)

    server.serve_forever()
