"""
f=open("vcf/control/hu3F864B_variants.vcf","r+")
for l in f:
	print (l)
"""
import csv
import pickle

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
	print(i)
	snp_dict["snp"+str(i+1)]=[]
	for line in snp_lines:
		snp_dict["snp"+str(i+1)].append(line.strip().split(" ")[i])

snp_dict_file=open("SNPdictionary.dat", "wb")
pickle.dump(snp_dict,snp_dict_file)
snp_dict_file.close()
print("Done with exporting")

"""
import pickle
import matplotlib.pyplot as plt
f= open("SNPdictionary.dat", "rb+")
dict1=pickle.load(f)
"""
