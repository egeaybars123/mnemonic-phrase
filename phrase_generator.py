import secrets as sc #generating secure random numbers with entropy
import hashlib as hb #hashing algorithms
bit_count = 256
count = 0
bits_str = ""
fourbits_list = []
word_list = []
binaryToHex = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', 
              '0100': '4', '0101': '5', '0110': '6', '0111': '7', 
              '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', 
              '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
hexToBinary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 
                'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

def binary_to_hex(l1):
    hexa_str = ""
    for hexa in l1:
        new_str = ""
        for bits in hexa:
            bits = str(bits)
            new_str += bits
        hexa_str += binaryToHex[new_str]
        
    return hexa_str

def hex_to_binary(l1):
    bits_str = ""
    for bits in l1:
        new_str = ""
        for hexa in bits:
            hexa = str(hexa)
            new_str += hexa
        bits_str += hexToBinary[new_str]    
    
    return bits_str

#generating a list of 256 bits

while count < bit_count:
    z = sc.randbelow(2)
    bits_str += str(z)
    count += 1

#implementation of sha-256 hashing algorithm 
#on the random 256 bits
hash_bits = bits_str.encode()
hashed = hb.sha256(hash_bits).hexdigest()

#creating a checksum from the first two letters 
#of the hashed string and adding to the original 256 bits

for i in range(2):
    num = hashed[i]
    bits_str += hex_to_binary(num)


#grouping the 264 bits into groups of 11 bits
#and converting each into base 10 decimal numbers.
#base 10 decimal numbers are used to find the corresponding
#number on the BIP-39 English word list.
print(bits_str)
word_file = open("word_list.txt", "r")


for i in range(0, len(bits_str)-10, 11):
    number = 0
    base_10 = int(bits_str[i:i+11], base = 2)
    word_file.seek(0)
    
    for number, line in enumerate(word_file):
        if str(number) == str(base_10):
            word_list.append(line.strip("\n"))
            break
                
word_file.close()
        

print("Your mnemonic phrase is: ")
for i in word_list:
    print(i, end = " ")
    
    