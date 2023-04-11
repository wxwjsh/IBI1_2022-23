import re
seq = ‘ATGCAATCGACTACGATCTGAGAGGGCCTAA’
a=seq.find('ATG')
count=seq.count(r'(TAG|TGA|TAA)',a)
print(len(re.findall(r'(TAG|TGA|TAA)',seq[a:])))

