import glob
import keystream_gen


def list2string(s):
  str1 = ""   
  return (str1.join(s))


def decrypt():
  #Ciphertext bitwise XOR with keystream (creating a binary string)
  bit = []
  bytetable = [("00000000"+bin(x)[2:])[-8:] for x in range(256)]
  for name in glob.glob("input.*.enc"):
    with open(name, 'rb') as file:
      bits = "".join(bytetable[x] for x in open(name, "rb").read())
  
  for i in range(len(bits)):
    bit.append(int(bits[i]))
  
  length = len(bit)
  out = []
  key = keystream_gen.keystream_gen(length)
  for i in range(length):
    out.append(str(bit[i] ^ key[i]))
  
  outs=list2string(out)
  
  bit_strings = [outs[i:i + 8] for i in range(0, len(outs), 8)]
  byte_list = [int(b, 2) for b in bit_strings]
  
  #creating decrypted file
  for format1 in glob.glob("input.*.enc"):
    format = str(format1.split('.')[1])
  name_out = "output." + format
  with open(name_out, 'wb') as f:
    f.write(bytearray(byte_list))
    
  print("Congratulation! Your Decrypted file is created in the directory!")
#Key Example:0011000011101010110111011110000110100101010001011110100010110101