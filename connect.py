from openstack import connection
def conn():
    auth_arg={'auth_url':'http://192.168.100.10:5000/v3','project_name':'admin','username':'admin','password':'Open@123','user_domain_name':'default','project_domain_name':'default'}
    con=connection.Connection(**auth_arg)
    return con

def democonn():
    auth_arg={'auth_url':'http://192.168.100.10:5000/v3','project_name':'demo','username':'demo','password':'Open@123','user_domain_name':'default','project_domain_name':'default'}
    con=connection.Connection(**auth_arg)
    return con

