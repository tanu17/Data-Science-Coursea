"""
f=open("vcf/control/hu3F864B_variants.vcf","r+")
for l in f:
	print (l)
"""
import csv

c= csv.reader(open('covariates.csv'), delimiter=',')

condition_dict={}
for row in c:
	condition_dict[row[0]]=row[1]

snp_file= open("snpMat.txt",'r+')
snp_id=snp_file.readline().strip().split(" ")
# print (len(snp_num))
# 10643 SNPs
snp_lines=snp_file.readlines()
snp_dict={}
for i in range(len(snp_id)):
	snp_dict["snp"+str(i+1)]=[]
	for line in snp_lines:
		snp_dict["snp"+str(i+1)].append(line.strip().split(" ")[i])
print(snp_dict)
