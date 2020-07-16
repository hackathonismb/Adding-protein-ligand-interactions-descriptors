#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 2020

@author: Aaron Ayllon Benitez
@description: Hackathon ISMB 2020 - Team 3A - Task 1 - file 2
"""

import sys, getopt
import atomium as at
import json

def JSONtoDIC(r):
    with open(r, 'r') as j:
        loaded_r = json.load(j)
    #loaded_r['identifiers'] #Output 3.5
    #type(r) #Output str
    #type(loaded_r) #Output dict
    return(loaded_r)
def getJSON(r,export):
    r = json.dumps(r,indent=2)
    #loaded_r = json.loads(r)
    #loaded_r['identifiers'] #Output 3.5
    #type(r) #Output str
    #type(loaded_r) #Output dict
    f = open(export, "w")
    f.write(r)
    f.close()
    
def run(file,bn):
    dic = JSONtoDIC(file)
    
    pdbID = dic["pdbid"]
    
    print(pdbID)
    pdb = at.open(bn)
    dic["pdbname"] = pdb.title
    atoms = pdb.model.atoms() # interest variable is .id, .name, .het (.het.name) 
    dicAt = {}
    for a in atoms:
        dicAt[a.id] = a.name
            
    #full_name, formula, synonym
    dicLig={}
    for b in pdb.model.ligands():
        dicLig[b.name] = [b.full_name, b.formula]
    
    for b,binfo in dic["bindingsites"].items():
        binfo["identifiers"]["het_fullname"] = dicLig[binfo["identifiers"]["hetid"]][0]
        binfo["identifiers"]["formula"] = dicLig[binfo["identifiers"]["hetid"]][1]
        for i,inter in binfo["interactions"].items():
            if( inter !=None):
                for d, desc in  inter.items():
                    tmpDic = {}
                    for r in desc:
                        if("idx" in r and "list" not in r and "water" not in r):
                            t = r.replace("idx", "atom")
                            tmpDic[t] = dicAt[desc[r]]
                        elif("list" in r):
                            t = r.replace("idx", "atom")
                            tmpDic[t] = {}
                            for e in desc[r]:
                                tmpDic[t][e] = dicAt[desc[r][e]]

                    desc.update(tmpDic)
                    
     
    getJSON(dic, file)
   
def main(argv):
   jsonF = ''
   pdbF  = ''

   try:
     # opts, args = getopt.getopt(argv,"hx:j:",["xmlfile=","jsonfile="])
     opts, args = getopt.getopt(argv,"hj:p:",["jsonfile=","pdbfile="])
   except getopt.GetoptError:
      print('[error] modifyJSON.py -j <jsonfile> -p <pdbfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('modifyJSON.py -j <jsonfile> -p <pdbfile>')
         print("-" * 25)
         print('-j --jsonfile:\t json file input.')
         print('-p --pdbfile:\t PDB file input.')
         
         
         sys.exit()
      elif opt in ("-j", "--jsonfile"):
         jsonF = arg
      elif opt in ("-p", "--pdbfile"):
         pdbF = arg
   run(jsonF,pdbF) 
if __name__ == "__main__":
   main(sys.argv[1:])