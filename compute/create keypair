def create_keypair(conn):
    keypair = conn.compute.find_keypair(KEYPAIR_NAME)

    if not keypair:
        print("Create Key Pair:")

        keypair = conn.compute.create_keypair(name=KEYPAIR_NAME)

        print(keypair)

        try:
            os.mkdir(SSH_DIR)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise e

        with open(PRIVATE_KEYPAIR_FILE, 'w') as f:
            f.write("%s" % keypair.private_key)

        os.chmod(PRIVATE_KEYPAIR_FILE, 0o400)

    return keypair
