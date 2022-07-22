def getkey():
    
    key = input('Enter a 64-bit binary key: ')
    if (checkkey(key)):
        rev_key = key [::-1]
        return rev_key
    else:
        while not checkkey(key):
            key = input('Your input is wrong, please Enter a 64-bit binary key: ')
        rev_key = key [::-1]
        return rev_key

def checkkey(string):
    flagb = True
    for char in string:
        if(char =='0' or char == '1'):
            continue
        else :
            flagb = False
            break
    if(flagb):
        if(len(string) == 64):
            flag = True
        else:
            flag = False
    else:
        flag = False
    return flag

reg19 = []
reg22 = []
reg23 = []

def key2reg(key) :
    
    for i in range(19):
        reg19.append(int(key[i]))
    
    for i in range(22):
        reg22.append(int(key[i+19]))

    for i in range(23):
        reg23.append(int(key[i+41]))
        
    return reg19,reg22,reg23



def majority(x, y, z):
    if x + y + z > 1:
        return 1
    else:
        return 0

def newbit(regno,reg1,reg2,reg3):
    if (regno == 19):
        new = reg1[18]^reg1[17]^reg1[16]^reg1[13]
    if (regno == 22):
        new = reg2[21]^reg2[20]
    if (regno ==23):
        new =reg3[22]^reg3[21]^reg3[20]^reg3[7]
    return new

def duplicate(source_list):
    dup_list = source_list[:]
    return dup_list


def keystream_gen(length):
    key2reg(getkey())
    LFSR19 = duplicate(reg19)
    LFSR22 = duplicate(reg22)
    LFSR23 = duplicate(reg23)
    keystream = []
    for i in range(length):
        maj = majority(LFSR19[8],LFSR22[10],LFSR23[10])

        if (LFSR19[8] == maj):
            newbit19 = newbit(19,LFSR19,LFSR22,LFSR23)
            LFSR19temp = duplicate(LFSR19)
            for j in range(19):
                LFSR19[j] = LFSR19temp[j-1]
            LFSR19[0] = newbit19

        if (LFSR22[10] == maj):
            newbit22 = newbit(22,LFSR19,LFSR22,LFSR23)
            LFSR22temp = duplicate(LFSR22)
            for k in range(22):
                LFSR22[k] = LFSR22temp[k-1]
            LFSR22[0] = newbit22

        if (LFSR23[10] == maj):
            newbit23 = newbit(23,LFSR19,LFSR22,LFSR23)
            LFSR23temp = duplicate(LFSR23)
            for l in range(23):
                LFSR23[l] = LFSR23temp[l-1]
            LFSR23[0] = newbit23
        
        outbit = LFSR19[18]^LFSR22[21]^LFSR23[22]
        keystream.insert(i,outbit)

    return keystream


#Key Example:0011000011101010110111011110000110100101010001011110100010110101