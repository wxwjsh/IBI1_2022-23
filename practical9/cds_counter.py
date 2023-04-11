import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
a=seq.find('ATG')
print(len(re.findall(r'(TAG|TGA|TAA)',seq[a:])))

