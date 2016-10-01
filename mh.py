import sys, string, os, binascii

def get_input(n):
    inputfile = open(n, 'r')
    filecontents = inputfile.read()
    filecontents = list(filecontents.strip())
    return filecontents

def get_input_split(n):
    inputfile = open(n, 'r')
    filecontents = inputfile.read()
    filecontents = filecontents.split(", ")
    return filecontents

def convert_str_to_hex(m):
    c = []
    for a in m:
        c.append(binascii.hexlify(a.encode()).decode())
    return c

def convert_hexstr_to_hex(c):
    f = []
    for a in c:
        f.append(binascii.unhexlify(a))
        #f.append(binascii.hexlify(a.encode()).decode())
    return f

def convert_byte_to_int(k):
    c = []
    for g in k:
        c.append(int.from_bytes(g, byteorder='big', signed=False))
    return c

def convert_int_to_hex(c):
    f = []
    for a in c:
        f.append('{:x}'.format(a))
    return f

def write_to_file(t,n):
    f = open(n, 'w')
    for c in t:
        f.write('%s, ' % str(c))

# def write_to_file_k(t,n):
#     f = open(n, 'w')
#     for c in t:
#         f.write('%s ' % c)

def gen(l):
    c = 0
    k = []
    while (c < l):
        k.append(binascii.hexlify(os.urandom(1)).decode())
        c += 1
    write_to_file(k, 'k.txt')
    return k

def enc():
    # Get message text
    mfilename = input('Enter name of the message file: ')
    message = get_input(mfilename)
    # Convert the text to hex
    m = convert_str_to_hex(message)
    # Get key length
    m_length = len(m)
    # Generate key and write it to file keyfile.txt
    key = gen(m_length)
    # Generate cypher text in int form
    c = [int(a, 16)^int(b, 16) for a,b in zip(m,key)]
    # Convert cypher from int to hex
    c = convert_int_to_hex(c)
    # Write the cypher text into c.txt
    write_to_file(c,'c.txt')
    return c

def dec():
    # Get cypher text
    cfilename = input('Enter name of the cypher file: ')
    cypher = get_input_split(cfilename)
    n = 1
    del cypher[-n]
    # Convert the cypher text to ascii
    c = convert_hexstr_to_hex(cypher)
    # Get the key text
    key = get_input_split('k.txt')
    # Convert the key str to hex
    # k = convert_str_to_hex(key)
    # print(k)
    # Generate plain text
    # pt = [int(a, 16)^int(b, 16) for a,b in zip(c,key)]
    print(cypher)
    # print(c)
    # print(pt)
    # # Write the plain text into plaintext.txt
    # write_to_file(pt,'p.txt')
    # return pt

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
