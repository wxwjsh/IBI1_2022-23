import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
start=seq.find('ATG')
print(len(re.findall(r'(TAG|TGA|TAA)',seq[start:])))

