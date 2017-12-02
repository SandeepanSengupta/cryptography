Segment = 5
number = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]

def distil(List):
    for pos,char in enumerate(List):
        if char =='\n':
            del List[pos]

    for i in range(0,len(List)):
        List[i] = int(List[i])

    return List

def chunkBlater(Input, CHUNK):

    """
    __HELP__

    type 'help(Serial)' in command window to get methods.

    """

    elements = len(Input)
    packets = elements/CHUNK
    offset = elements - packets*CHUNK

    from time import sleep

    from Serial import Serial

    print "\nInput:\t"+str(Input)


    COMPORT = Serial()
    COMPORT.begin('COM6', 9600)

    block = []
    received = []
    if packets > 0:
        for i in range(0, packets):
            block = Input[i*CHUNK:(i + 1)*CHUNK]

            print block
            j = 0
            for j in range(j, CHUNK):
                COMPORT.sprintln(block[j])

                capture = COMPORT.sread()
                received.extend(capture)

                print "Packet Index:\t"+str(i)+"\tChunk Index:\t"+str(j)+"\tReceived:\t"+capture


    if offset > 0:
        block = Input[elements - offset: elements]

        print block
        k = 0
        for k in range(k, offset):
            COMPORT.sprintln(block[k])

            capture = COMPORT.sread()
            received.extend(capture)

            print "Offset Index:\t"+str(k)+"\tReceived:\t"+capture
    return distil(received)

if __name__ == '__main__':
    print "Output:\t"+str(chunkBlater(number, Segment))

