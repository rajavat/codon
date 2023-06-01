input = input("input a string to be encoded: ")

# convert text to binary
binary = ''.join(format(x, '08b') for x in bytearray(input, 'utf-8'))

for i in range(0, len(binary), 2):
    binary = binary[i:i+2]


# convert binary to nucleotides
# 00 = "A" (adenine)
# 01 = "G" (guanine)
# 10 = "C" (cytosine)
# 11 = "T" (thymine)

nt = {
    "00": "A",
    "01": "G",
    "10": "C",
    "11": "T"
} 

DNA = []
for num in binary:
    for key in list(nt.keys()):
        if num == key:
            DNA.append(nt.get(key))

seq = "".join(DNA)

       
print(seq)