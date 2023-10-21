import hashlib
import os 

def create_hash(length:int) -> str:
    
    """
    Create a hash id by encoding a string of random bytes of size length.

    Parameters:
    length (int): size of random bytes

    Returns:
    A hash id of length 40
    """

    # generate a hash object for a randomly generated string
    hash_object = hashlib.sha1()
    hash_object.update(str(os.urandom(length)).encode())
    hash_id = hash_object.hexdigest()
    return hash_id

