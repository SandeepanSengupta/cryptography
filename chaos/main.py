# -*- coding: utf-8 -*-
"""
@author: Sandeepan
"""

from configurator import configurator as cfgr
SIGMA, BETA, RHO, ALPHA, GAMMA, DT, MSG_FILE = cfgr('setup.cfg')


def hide(info):

    from binascii import hexlify
    from numpy import zeros

    input_information = info

    hex_data = hexlify(input_information)
    temp = zeros(len(hex_data)).astype('str')
    for i in range(len(hex_data)):
        temp[i] = hex_data[i]
    for j in range(len(temp)):
        if temp[j] == '0': temp[j] = '0000'
        if temp[j] == '1': temp[j] = '0001'
        if temp[j] == '2': temp[j] = '0010'
        if temp[j] == '3': temp[j] = '0011'
        if temp[j] == '4': temp[j] = '0100'
        if temp[j] == '5': temp[j] = '0101'
        if temp[j] == '6': temp[j] = '0110'
        if temp[j] == '7': temp[j] = '0111'
        if temp[j] == '8': temp[j] = '1000'
        if temp[j] == '9': temp[j] = '1001'
        if temp[j] == 'a': temp[j] = '1010'
        if temp[j] == 'b': temp[j] = '1011'
        if temp[j] == 'c': temp[j] = '1100'
        if temp[j] == 'd': temp[j] = '1101'
        if temp[j] == 'e': temp[j] = '1110'
        if temp[j] == 'f': temp[j] = '1111'

    bin_out = zeros(4*len(temp)).astype('uint32')
    for i in range(len(temp)):
        for j in range(4):
            bin_out[4*i+j] = temp[i][j]
    return bin_out

def unhide(bindata):

    from binascii import unhexlify
    from numpy import zeros

    bin_data = bindata
    data = zeros(len(bin_data)/4).astype('str')

    for i in range(len(bin_data)/4):
        data[i] = 1000*bin_data[4*i]+100*bin_data[4*i+1]+10*bin_data[4*i+2]+bin_data[4*i+3]
        #print "data["+str(i)+"] = "+data[i]

    for j in range(len(data)):
        if data[j] == '0'   : data[j] = '0'
        if data[j] == '1'   : data[j] = '1'
        if data[j] == '10'  : data[j] = '2'
        if data[j] == '11'  : data[j] = '3'
        if data[j] == '100' : data[j] = '4'
        if data[j] == '101' : data[j] = '5'
        if data[j] == '110' : data[j] = '6'
        if data[j] == '111' : data[j] = '7'
        if data[j] == '1000': data[j] = '8'
        if data[j] == '1001': data[j] = '9'
        if data[j] == '1010': data[j] = 'a'
        if data[j] == '1011': data[j] = 'b'
        if data[j] == '1100': data[j] = 'c'
        if data[j] == '1101': data[j] = 'd'
        if data[j] == '1110': data[j] = 'e'
        if data[j] == '1111': data[j] = 'f'

    hex_string = ''

    for j in range(len(data)):
        hex_string = hex_string + data[j]
    output_information = unhexlify(hex_string)
    #return output_information
    return (output_information)

def randgen(key, image_size):

    from numpy import zeros, remainder, uint8
    dt = DT
    n = image_size

    xs = zeros((n + 1,))
    ys = zeros((n + 1,))
    zs = zeros((n + 1,))

    xs[0], ys[0], zs[0] = key[0], key[1], key[2]

    for i in xrange(n) :
        from chaos import chen as chen
        x_dot, y_dot, z_dot = chen(xs[i], ys[i], zs[i])
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)

    Xs =  remainder(abs(xs*10**14), 2).astype(uint8)
    Ys =  remainder(abs(ys*10**14), 2).astype(uint8)
    Zs =  remainder(abs(zs*10**14), 2).astype(uint8)

    rand_array = Xs ^ Ys ^ Zs

    return rand_array

def removeSpaces(string):
    list = []
    string= string.replace("[","")
    string = string.replace("]","")
    for i in xrange(len(string)):
        if string[i] != ',':
            list.append(string[i])
    return ' '.join(list)

'''
Sample Usage
.........................................
encrypt("msg.txt",[0.01,2.0232,-4])
decrypt("cipher.txt",[0.01,2.0232,-4])
.........................................
'''

def encrypt(file_name=MSG_FILE,password=[0.01,2.0232,-4]):
    import os
    from numpy import uint32,zeros,append

    msg =""
    if os.path.isfile(file_name) and os.access(file_name, os.R_OK):
        f = open(file_name,'r')
        msg = f.read()
        f.close()

    enc_bin_data = hide(msg)#message binary form
    msg_length = len(enc_bin_data)
    keys = password
    rand = randgen(keys,msg_length)#keys binary form
    enc_bin_data_1 = append(enc_bin_data,zeros(1))
    cipher = enc_bin_data_1.astype(uint32)^rand
    list=[]
    for i in range(len(cipher)):
        list.append(str(cipher[i]))
    encryptedMsg ="["+','.join(list)+"]"

    if os.path.isfile('cipher.txt') and os.access('cipher.txt', os.W_OK):
        f=open('cipher.txt','w')
        f.write(encryptedMsg)
        print "\nMessage Encryption successful!"
        f.close()
    else:
        f=open('cipher.txt','w')
        f.write(encryptedMsg)
        print "\nFile created: cipher.txt\nMessage Encryption successful!"
        f.close()


def decrypt(file_name='cipher.txt',key=[0.01,2.0232,-4]):
    from numpy import uint32,zeros,append
    import os

    msg = []

    if os.path.isfile(file_name) and os.access(file_name, os.R_OK):
        f = open(file_name,'r')
        msg = f.read()
        f.close()

    msg = removeSpaces(msg)
    cipher_array = [int(n) for n in msg.split()]
    cipher_data = cipher_array
    password = key
    #password = key
    msg_length = len(cipher_data)
    rand = randgen(password,msg_length)#keys binary form
    cipher_data_1 = append(cipher_data,zeros(1))
    msg = cipher_data_1.astype(uint32)^rand
    dec_cipher = unhide(msg)
#    print "Msg: "+str(dec_cipher)
    if os.path.isfile('output.txt') and os.access('output.txt', os.W_OK):
        f=open('output.txt','w')
        f.write(dec_cipher)
        print "\nMessage Decryption successful!"
        f.close()
    else:
        f=open('output.txt','w')
        f.write(dec_cipher)
        print "\nFile created: output.txt\nMessage Decryption successful!"
        f.close()



if __name__ == '__main__':
    encrypt()
    decrypt()
