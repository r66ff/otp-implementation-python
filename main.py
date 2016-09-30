import sys, random, string

def random_gen():
    k = random.SystemRandom()
    k =k.choice(string.ascii_uppercase)
    k = ord(k)
    return k

def get_input(n):
    inputfile = open(n, 'r')
    filecontents = inputfile.read()
    filecontents = list(filecontents.strip())
    return filecontents

def convert_to_ascii(arr):
    c = []
    for a in arr:
        c.append(ord(a))
    return c


def write_to_file(t,n):
    f = open(n, 'w')
    k = []
    for c in t:
        k.append(str(chr(c)))
    f.write(''.join(k))

def gen(l):
    c = 0
    k = []
    while (c < l):
        k.append(random_gen())
        c += 1
    write_to_file(k, 'keyfile.txt')
    return k

def enc():
    # Get message text
    mfilename = input('Enter name of the message file: ')
    message = get_input(mfilename)
    # Convert the text to ascii
    m = convert_to_ascii(message)
    # Get key length
    m_length = len(m)
    # Generate key and write it to file keyfile.txt
    key = gen(m_length)
    # Generate cypher text
    c = [a^b for a,b in zip(m,key)]
    # Write the cypher text into cyphertext.txt
    write_to_file(c,'cyphertext.txt')
    return c

def dec():
    # Get cypher text
    cfilename = input('Enter name of the cypher file: ')
    cypher = get_input(cfilename)
    # Convert the cypher text to ascii
    c = convert_to_ascii(cypher)
    # Get the key text
    key = get_input('keyfile.txt')
    # Convert the key text to ascii
    k = convert_to_ascii(key)
    # Generate plain text
    pt = [a^b for a,b in zip(c,k)]
    # Write the plain text into plaintext.txt
    write_to_file(pt,'plaintext.txt')
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
