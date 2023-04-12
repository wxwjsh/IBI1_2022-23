import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
#First find the start codon ATG
start=seq.find('ATG')
#Find the termination codon ATG again
print(len(re.findall(r'(TAG|TGA|TAA)',seq[start:])))

