import hashlib

def make_pw_hash(password):
    return hashlib.sha256(str.encode(password)).hexdigest()
    

