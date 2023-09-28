import hashlib
import os 
def generate_hash():

    # generate a hash object for a randomly generated string
    hash_object = hashlib.sha1()
    hash_object.update(str(os.urandom(3)).encode())
    hash_id = hash_object.hexdigest()
    return hash_id
