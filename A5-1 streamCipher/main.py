from decrypt import decrypt
from encrypt import encrypt
from keystream_gen import keystream_gen
import os
import glob


def choice_input(): 
    print("Please choose one of the below functions:")
    choicef = str(input('1 : Encryption\n2 : Decryption\nPress 1 or 2: '))
    if (choicef == '1' or choicef == '2'):
        return choicef
    else:
        while(choicef != '1' or choicef != '2'):
            if (choicef == '1' or choicef == '2'):
                return choicef
            choicef = str(input('1 : Encryption\n2 : Decryption\nPlease choose  1 or 2: '))
    return choicef

def checkfile_en():
    name = glob.glob("input.*")
    if (len(name)==0):
        return 0
    else:
        if os.path.isfile(name[0]):
            return 1
        else:
            return 0
            
def checkfile_de():
    name = glob.glob("input.*.enc")
    if (len(name)==0):
        return 0
    else:
        if os.path.isfile(name[0]):
            return 1
        else:
            return 0   

def main():
    choice = choice_input()
    if (choice == '1'):
        if (checkfile_en()==1):
            encrypt()
        else:
            print("input.* doesn't exist")
    elif (choice == '2'):
        if (checkfile_de()==1):
            decrypt()
        else:
            print("input.*.enc doesn't exist")


main()
#Key Example : 0011000011101010110111011110000110100101010001011110100010110101
