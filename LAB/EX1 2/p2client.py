import Pyro4

def rmi_client():
    # Locate the RMI server by the name 'example.rmi'
    remote_service = Pyro4.Proxy("PYRONAME:example.rmi")
    
    # Call the remote method
    response = remote_service.say_hello("Client")
    print(f"Server says: {response}")

rmi_client()


import Pyro4

def client():
    remote = Pyro4.Proxy("PYRONAME:example.rmi")
    response = remote.say_hello("Sujay")
    print(response)
client()