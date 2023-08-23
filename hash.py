import bcrypt


password = b'1234'

hashed_pswd = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed_pswd)
