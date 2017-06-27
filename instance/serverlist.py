import connect
def list_server(conn):
    for server in conn.compute.servers():
        print server
list_server(conn=connect.democonn())

~                                            
