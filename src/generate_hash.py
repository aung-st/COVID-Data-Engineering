import hashlib
import os 

def generate_hash(length):

    # generate a hash object for a randomly generated string
    hash_object = hashlib.sha1()
    hash_object.update(str(os.urandom(length)).encode())
    hash_id = hash_object.hexdigest()
    return hash_id
