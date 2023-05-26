#           input data
print("    ")
print ("PUNNET SQUARE MAKER--------------------------")
print("this program calculates offspring genotype frequencies and generates a punnet square in latex")
print("when entering the genotypes of each parent, include both alleles of the gene: 'Aa', not 'A a'")

p1 = input("input the genotype of the first parent: ")
p2 = input("input the genotype of the second parent: ")

#           generate alleles
p1a1 = (p1[:1])
p1a2 = (p1[1:2])

p2a1 = (p2[:1])
p2a2 = (p2[1:2])

#           generate offspring
offspring11 = (p1a1 + p2a1)
offspring12 = (p1a1 + p2a2)
offspring21 = (p1a2 + p2a1)
offspring22 = (p1a2 + p2a2)

#           generate genotypes
genotypes = []
ngenotypes = 1
genotype1 = offspring11
genotypes.append(genotype1)

if offspring12 != offspring11:
    genotype2 = offspring12
    ngenotypes += 1
    genotypes.append(genotype2)
else:
    genotype2 = ""

if offspring21 != offspring12 and offspring21 != offspring11:
    genotype3 = offspring21
    ngenotypes += 1
    genotypes.append(genotype3)
else:
    genotype3 = ""
    
if offspring22 != offspring21 and offspring22 != offspring12 and offspring22 != offspring11:
    genotype4 = offspring22
    ngenotypes += 1
    genotypes.append(genotype4)
else:
    genotype4 = ""
    
    genotype1 = genotypes[0]
    genotype2 = genotypes[1] if ngenotypes >= 2 else None
    genotype3 = genotypes[2] if ngenotypes >= 3 else None
    genotype4 = genotypes[3] if ngenotypes == 4 else None
    
#           convert data
Genotypes = str(genotypes)
Offspring = (offspring11, offspring12, offspring21, offspring22)

#           print latex table
print('')
print('')
print('Latex Punnet square output:')
print('')
print('\\begin{table}[]')
print('\\begin{tabular}{lll}')
print('    &' + p1a1 + '&' + p1a2 + '\\\\')
print(p2a1 + '&' + offspring11 + '&' + offspring21 + '\\\\')
print(p2a2 + '&' + offspring12 + '&' + offspring22)
print('\n\\end{tabular}\n\\end{table}')

#       calculate genotype ratios
g1a = 0
g2a = 0
g3a = 0
g4a = 0
g1a = Offspring.count(genotype1)
g2a = Offspring.count(genotype2) if ngenotypes >= 2 else None
g3a = Offspring.count(genotype3) if ngenotypes >= 3 else None
g4a = Offspring.count(genotype4) if ngenotypes >= 4 else None

#       print genotype ratios
print('')
print('')
print('Offspring genotype frequencies:')
print('')
print(str(g1a/4*100) + "% " + genotype1)
print(str(g2a/4*100) + "% " + genotype2) if ngenotypes >= 2 else None
print(str(g3a/4*100) + "% " + genotype3) if ngenotypes >= 3 else None
print(str(g4a/4*100) + "% " + genotype4) if ngenotypes == 4 else None