import os, string, binascii, sys

def get_input_str(n):
    inputfile = open(n, 'rb')
    filecontents = inputfile.read()
    filecontents = list(filecontents.strip())
    return filecontents

def write_to_file_bin(t,n):
    f = open(n, 'wb')
    # k = []
    for c in t:
        # k.append(c)
        f.write(c.encode())


def convert_ascii_to_bin(m):
    c = list()
    for a in m:
        c.append(bin(int(binascii.hexlify(a.encode()), 16)))
    return c

def gen(l):
    c = 0
    k = list()
    while (c < l):
        k.append(bin(int(binascii.hexlify(os.urandom(1)), 16)))
        c += 1
    write_to_file_bin(k, 'k.txt')
    return k

def enc():
    # Get message text
    mfilename = input('Enter name of the message file: ')
    inputfile = open(mfilename, 'r')
    filecontents = inputfile.read()
    filecontents = list(filecontents.strip())
    m = list()
    for a in filecontents:
        m.append(bin(int(binascii.hexlify(a.encode()), 16)))

    #generate key and write to k.txt
    k = list()
    for c in k:
        while (c < l):
            k.append(bin(int(binascii.hexlify(os.urandom(1)), 16)))
            c += 1
    f = open('k.txt', 'wb')
    for c in k:
        k.append(c)
        k.write(c.encode())



    # message = convert_ascii_to_bin(message)
    # # print(message)
    # # Get key length
    # m_length = len(message)
    # # Generate key and write it to file keyfile.txt
    # key = gen(m_length)
    # # print(message)
    # # print(key)
    # # Generate cypher text
    # c = [bin(int.from_bytes(a.encode(), 'big')) ^ bin(int.from_bytes(b.encode(), 'big')) for a,b in zip(message,key)]
    # # Write the cypher text into cyphertext.txt
    # write_to_file_bin(c,'cyphertext.txt')
    # return c
#
# def enc():
#     # Get message text
#     mfilename = input('Enter name of the message file: ')
#     message = get_input_str(mfilename)
#     message = convert_ascii_to_bin(message)
#     # print(message)
#     # Get key length
#     m_length = len(message)
#     # Generate key and write it to file keyfile.txt
#     key = gen(m_length)
#     # print(message)
#     # print(key)
#     # Generate cypher text
#     c = [bin(int.from_bytes(a.encode(), 'big')) ^ bin(int.from_bytes(b.encode(), 'big')) for a,b in zip(message,key)]
#     # Write the cypher text into cyphertext.txt
#     write_to_file_bin(c,'cyphertext.txt')
#     return c

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
