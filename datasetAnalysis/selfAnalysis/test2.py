import csv
import pickle

c= csv.reader(open('covariates.csv'), delimiter=',')
yes_list=[]
no_list=[]
condition_dict={}
for row in c:
	if "human_id" not in row:
		condition_dict[row[0]]=row[1]
condition_list=(list((condition_dict.values())))
for i in range(len(condition_list)):
	if condition_list[i]=="0":
		no_list.append(i)
	else:
		yes_list.append(i)
#print(yes_list)
#print(no_list)

f= open("SNPdictionary.dat", "rb+")
dict1=pickle.load(f)
yes_dict={}
no_dict={}
for key in dict1.keys():
	yes_dict[key]=0
	no_dict[key]=0
	for i in yes_list:
		yes_dict[key]+=int(dict1[key][i])
	for j in no_list:
		no_dict[key]+=int(dict1[key][j])

snp_yes_file=open("PositiveDictionary.dat", "wb")
snp_no_file=open("NegativeDictionary.dat", "wb")

diff_dict={}
for key in dict1.keys():
	x=abs(yes_dict[key]- no_dict[key])
	if x>10:
		diff_dict[key]=x
print(diff_dict)

f2=open("diff.csv","w+")
columnTitleRow = "name, value\n"
f2.write(columnTitleRow)
d=list(diff_dict.keys())
for key in d:
	name = key
	value = diff_dict[key]
	row = name + "," + str(value) + "\n"
	f2.write(row)
f2.close()

pickle.dump(yes_dict,snp_yes_file)
pickle.dump(no_dict, snp_no_file)
snp_yes_file.close()
snp_no_file.close()
print("Done with exporting")
