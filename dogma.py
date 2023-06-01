# determine whether input is a DNA or RNA sequence, or an incorrect input
isSeq = False
isDNA = False

nucalph = set('ATGCU')
DNAalph = set('ATCG')
RNAalph = set('AUCG')
protalph = set('ATCGRNDEQHILKMFPSWYV')

# determine if sequence is valid
while isSeq == False:
    seq = input("enter your sequence: ").upper() # .upper converts seq to uppercase

    for nt in seq:
        if nt == 'A' or nt == 'T' or nt == 'G' or nt == 'C' or nt == 'U':
            isSeq = True 
        else:
            print("the sequence contains non-nucleotide digits, please check your input")
            break

# convert str into list
seq = [*seq]
            
# functions -----------------------------------------------

# DNA to mRNA
def transcription(seq):
    seq = seq.upper()
    strand = ""
    
    for i in seq:
        if i == "A":
            strand += "T"
        elif i == "T":
            strand += "A"
        elif i == "G":
            strand += "C"
        elif i == "C":
            strand += "G"
    
    return strand.replace("T", "U")

# convert mRNA into ORF reading frames
def orf(seq, order, direction): # order = 1, 2, 3; direction = f/r (forward/reverse)
    revseq = seq[:: -1] 
    
    if order == '1' and direction == 'f':
        return [seq[i : i + 3] for i in range(0, len(seq), 3)]
    if order == '2' and direction == 'f':
        return [seq[i : i + 3] for i in range(1, len(seq), 3)]
    if order == '2' and direction == 'f':
        return [seq[i : i + 3] for i in range(2, len(seq), 3)]
    
    if order == '1' and direction == 'r':
        return [revseq[i : i + 3] for i in range(0, len(revseq), 3)]
    if order == '2' and direction == 'r':
        return [revseq[i : i + 3] for i in range(1, len(revseq), 3)]
    if order == '2' and direction == 'r':
        return [revseq[i : i + 3] for i in range(2, len(revseq), 3)]
    
    
def translation(seq):
    prot = "" 
    protseq = ""
    
    for i in seq:
        protseq += 1
    
    codon = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
            "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
            "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
            "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
            "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
            "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
            "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
            "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
            "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
            "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
            "UAA": "_", "CAA": "Q", "AAA": "K", "GAA": "E",
            "UAG": "_", "CAG": "Q", "AAG": "K", "GAG": "E",
            "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
            "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
            "UGA": "_", "CGA": "R", "AGA": "R", "GGA": "G",
            "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
            }
    
    if len(protseq) % 3 == 0: # check if length divisible by 3, codon pairs
        for i in range(0, len(seq)):
            prot += codon[seq[i]]
        return protseq
    else:
        for i in range(0, len(seq) -1):
            prot += codon[seq[i]]