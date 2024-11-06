import Pyro4

# Create a class for the remote service
@Pyro4.expose
class RemoteService:
    def say_hello(self, name):
        return f"Hello, {name}! This is the RMI server."

def start_server():
    # Start the Pyro4 Daemon
    daemon = Pyro4.Daemon()  # Pyro4 daemon
    ns = Pyro4.locateNS()  # Locate the name server
    uri = daemon.register(RemoteService)  # Register the service
    ns.register("example.rmi", uri)  # Register the service with a name in the name server

    print(f"RMI Server started with URI: {uri}")
    daemon.requestLoop()  # Start the event loop for listening

start_server()

import Pyro4

@Pyro4.expose()
class custom():
    def say_hello(self,name):
        return f"Hello {name}"

def server():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(custom)
    ns.register('example.rmi',uri)

    print()
    daemon.requestLoop()

server()
