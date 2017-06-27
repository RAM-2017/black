import connect
def create_server(conn):
        print 'create server:'
        image=conn.compute.find_image("openstack-cirros-image")
        flavor=conn.compute.find_flavor("m1.small")
        network=conn.network.find_network("Nw_1")
        keypair=conn.compute.find_keypair("mykey")

        server=conn.compute.create_server(name="first_cirros", image_id=image.id, flavor_id=flavor.id,
                networks=[{"uuid": network.id}], key_name=keypair.name)

        server=conn.compute.wait_for_server(server)

create_server(conn=connect.democonn())
~                                                                                                                                              
~                                                        
