def list_images(conn):
    print("List Images:")

    for image in conn.image.images():
        print(image)
