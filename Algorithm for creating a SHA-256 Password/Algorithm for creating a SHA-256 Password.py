import hashlib
def hash_password(password):
    hash_object = hashlib.sha256()
    hash_object.update(password.encode())
    return hash_object.hexdigest()

password = "my$ecureP@ssw0rd"
hashed_password = hash_password(password)

print("The hashed password is: ", hashed_password)