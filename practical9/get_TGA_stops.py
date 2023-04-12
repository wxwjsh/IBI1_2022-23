import re
import os
os.chdir("/Users/jishuhan/.git/IBI1_2022-23/IBI1_2022-23/IBI1_2022-23/practical9")
#Open a known file and create a results file
dna=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r')
stop=open('TGA_genes.fa','w')
#Use the compile command to search for the first space up to >, defined as dna _name
dna_name=re.compile(r'>(\S+)')
#Create two new variables
finall_dna_name=''
finall_dna=''
#Circulation
with dna as ip, stop as op:
    for line in ip:
        if line.startswith('>'):
#Search for dna names starting with > in dna_name and group them out
           finall_dna_name=dna_name.search(line).group()
           finall_dna=''
        else:
#Merging dna sequences
             finall_dna+=line.strip()
             if finall_dna.endswith(r'TGA'):
#Output by dna name line feed ➕ dna sequence
                 op.write('{}\n{}\n\n'.format(finall_dna_name,finall_dna))
         
