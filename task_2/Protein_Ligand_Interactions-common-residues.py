#!/usr/bin/python3
# -*- coding: utf-8 -*-

# In[59]:


import json
import pandas as pd
import sys, getopt


# In[60]:



def run(file1, file2, output):  
    print(file1)
    with open(file1, 'r') as j:
         lig1= json.load(j)
    with open(file2, 'r') as json2:
         lig2= json.load(json2)
    
    all_res_list=[]
    for lig in [lig1,lig2]:
        all_residues=[]
        res_list=[]
        for bs, bs_info in lig['bindingsites'].items():
            residues=[]
            for k, l in bs_info['bs_residues'].items():
                residues.append(l['value'])
            all_residues.extend(residues)   
    
        all_inter_residues=[]
        info=[]
        for bs, bs_info in lig['bindingsites'].items():
            for j,i in bs_info['interactions'].items():
                if(i):
                    for key,value in i.items():
                        res=str(value['resnr'])+str(value['reschain'])
                        all_inter_residues.append(str(value['resnr'])+str(value['reschain']))
                        if(res in all_residues):
                            res_list.append((value['resnr'],value['reschain'],value['restype']))
                            info_dict={"Protein residue number":value['resnr'],"Protein residue chain":value['reschain'],"Protein residue type":value['restype'],"Interaction type":j,"Ligand residue number":value['resnr_lig'],"Ligand residue chain":value['reschain_lig'],"Ligand residue type":value['restype_lig']}
                    
                            info.append(info_dict)
                        
        all_res_list.append(res_list)
    
        
    
    list1=set(all_res_list[0])
    list2=set(all_res_list[1])
    common_residues=list1&list2
    
    
    # In[66]:
    
    
    data=[]
    
    for lig in [lig1,lig2]:
        info=[]
        for bs, bs_info in lig['bindingsites'].items():
            for j,i in bs_info['interactions'].items():
                if(i):
                    for key,value in i.items():
                        if((value['resnr'],value['reschain'],value['restype']) in common_residues):
                            info_dict={"Protein residue number":value['resnr'],"Protein chain":value['reschain'],"Protein residue type":value['restype'],"Interaction type":j,"Ligand residue number":value['resnr_lig'],"Ligand residue chain":value['reschain_lig'],"Ligand residue type":value['restype_lig']}
                            info.append(info_dict)
                        
    
        index=[]
        
        for i in range(0,len(info)):
            index.append(lig['pdbid'])
        df=pd.DataFrame(info,index=index)
    
        data.append(df)
    
    
    # In[72]:
    
    
    write=pd.concat(data)
    
    write.to_csv(output)


def main(argv):
   json1F = ''
   json2F = ''
   output = ''
   try:
     # opts, args = getopt.getopt(argv,"hx:j:",["xmlfile=","jsonfile="])
     opts, args = getopt.getopt(argv,"hf:s:o:",["jsonfile1=","jsonfile2=","outputCsv="])
   except getopt.GetoptError:
      print('[error] DiffAnalysis.py -f <jsonfile1> -s <jsonfile2> -o <outputCsv>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('xmlToJSON.py -f <jsonfile1> -s <jsonfile2> -o <outputCsv>')
         print("-" * 25)
         print('-f --jsonfile1:\tFirst JSON file obtained by xmlToJSON.py script')
         print('-s --jsonfile2:\tSecond JSON file obtained by xmlToJSON.py script')
         print('-o --outputCsv:\tCSV output file') 
         
         
         sys.exit()
      elif opt in ("-f", "--jsonfile1"):
         json1F = arg
      elif opt in ("-s", "--jsonfile2"):
         json2F = arg
      elif opt in ("-o", "--outputCsv"):
         output = arg
   
   run(json1F,json2F,output)

if __name__ == "__main__":
   main(sys.argv[1:])  
    
    

# In[ ]:




