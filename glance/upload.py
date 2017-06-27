import connect
#from examples.connect import EXAMPLE_IMAGE_NAME
def upload_image(conn):
        print "upload image"
        imagefile="/home/controller/Desktop/ciross1.qcow2"
        data=open(imagefile)

        #image_attrs={'name':'openstack-cirros-image','data':data,'disk_format':'raw','container_format':'bare','visability':'public'}
        image_attrs={'name':'openstack-cirros-image','data':data,'disk_format':'qcow2','container_format':'bare','visability':'public'}
        conn.image.upload_image(**image_attrs)
upload_image(conn=connect.conn())
