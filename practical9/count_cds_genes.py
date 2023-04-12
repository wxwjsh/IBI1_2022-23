import re
#Asking for input
stop_codon=input("Please input a stop codon(TAA/TAG/TGA):")
#Open the original file and define the variable name file
import os
os.chdir("/Users/jishuhan/.git/IBI1_2022-23/IBI1_2022-23/IBI1_2022-23/practical9")
dna=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r')
data = open("{}_stop_genes.fa".format (stop_codon), "w")
#Use the compile command to search for the first space up to >, defined as 
dna _name
dna_name=re.compile(r'>(\S+)')
#Defining variables and initial count values
finall_dna_name=''
finall_dna=''
count=0
#Circulation
with dna as ip, data as op:
    for line in ip:
        #Cut dna sequence name
        if line.startswith('>'):
            finall_dna_name=dna_name.search(line).group()
            finall_dna=''
        else:
            #Merging dna sequences
            finall_dna+=line.strip()
            if finall_dna.endswith(stop_codon):
                #Calculate the number of stop_codons ending in stop_codon
                count=len(re.findall(stop_codon,finall_dna))
                #Output documents
                op.write('{}   
{}\n{}\n\n'.format(finall_dna_name,count,finall_dna))
