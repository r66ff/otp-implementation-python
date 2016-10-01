import os
f=open("key.txt", "wb")
f.write(os.urandom(32))
f.close()
