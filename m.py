import sys, string, os

def get_input(n):
    inputfile = open(n, 'r')
    filecontents = inputfile.read()
    filecontents = list(filecontents.strip())
    return filecontents

def convert_str_to_int(m):
    c = []
    for a in m:
        c.append(ord(a))
    return c

def convert_byte_to_int(k):
    c = []
    for g in k:
        c.append(int.from_bytes(g, byteorder='big', signed=False))
    return c

def write_to_file(t,n):
    f = open(n, 'w')
    for c in t:
        f.write('%s, ' % str(c))

def write_to_file_b(t,n):
    f = open(n, 'wb')
    for c in t:
        f.write(c)

def gen(l):
    c = 0
    k = []
    while (c < l):
        k.append(os.urandom(1))
        c += 1
    write_to_file_b(k, 'k.txt')
    return k

def enc():
    # Get message text
    mfilename = input('Enter name of the message file: ')
    message = get_input(mfilename)
    # Convert the text to ascii
    m = convert_str_to_int(message)
    # Get key length
    m_length = len(m)
    # Generate key and write it to file keyfile.txt
    key = gen(m_length)
    # Covert the key into integers
    k = convert_byte_to_int(key)
    # Generate cypher text
    c = [a^b for a,b in zip(m,k)]
    # Write the cypher text into c.txt
    write_to_file(c,'c.txt')
    return c

def dec():
    # Get cypher text
    cfilename = input('Enter name of the cypher file: ')
    cypher = get_input(cfilename)
    # Convert the cypher text to ascii
    c = convert_str_to_int(cypher)
    # Get the key text
    key = get_input('k.txt')
    # Convert the key text to ascii
    k = convert_byte_to_int(key)
    # Generate plain text
    pt = [a^b for a,b in zip(c,k)]
    # Write the plain text into plaintext.txt
    write_to_file(pt,'p.txt')
    return pt

def main():
    operation = input('Hi:) What would you like to do? enc/dec: ')
    if operation == 'enc':
        enc()
        print('Encrypted! Your key is stored in keyfile.txt and cypher is in cyphertext.txt')
    elif operation == 'dec':
        dec()
        print('Decripted! Your message is stored in plaintext.txt')
    else:
        input('Error, try again')

main()
