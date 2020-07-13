#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 2020

@author: Rachita and Aaron Ayllon Benitez
@description: Hackathon ISMB 2020 - Team 3A - Task 1
"""
# Comparing interactions for two ligands at the same residues: MultiIndexing: Interaction specific
# 
# 

import json
import pandas as pd
import sys, getopt


def run(file1, file2, output):    
    with open(file1, 'r') as j:
         lig1= json.load(j)
    with open(file2, 'r') as json2:
         lig2= json.load(json2)
    
    
    
    Ligands=[lig1,lig2]
    all_ligand_data=pd.DataFrame()
    for lig in Ligands:
        hp_df=pd.DataFrame(columns=["PDB ID","Ligand","Binding Site","resnr","restype","reschain","resnr_lig","restype_lig","reschain_lig","dist","ligcarbonidx","protcarbonidx","ligcoo_x","ligcoo_y","ligcoo_z","protcoo_x","protcoo_y","protcoo_z"])
        hyd_df=pd.DataFrame(columns=["PDB ID","Ligand","Binding Site","resnr","restype","reschain","resnr_lig","restype_lig","reschain_lig", "sidechain","dist_h-a","dist_d-a","don_angle","protisdon","donoridx","donortype","acceptoridx","acceptortype","ligcoo_x","ligcoo_y","ligcoo_z","protcoo_x","protcoo_y","protcoo_z"])         
        sb_df=pd.DataFrame(columns=["PDB ID","Ligand","Binding Site","resnr","restype","reschain","resnr_lig","restype_lig","reschain_lig","dist", "protispos","lig_group","ligcoo_x","ligcoo_y","ligcoo_z","protcoo_x","protcoo_y","protcoo_z"])         
        metco_df=pd.DataFrame(columns=["PDB ID","Ligand","Binding Site","resnr","restype","reschain","resnr_lig","restype_lig","reschain_lig","metal_idx","metal_type","target_idx","target_type","coordination","dist", "location","rms","geometry","complexnum","metalcoo_x","metalcoo_y","metalcoo_z","targetcoo_x","targetcoo_y","targetcoo_z"])         
        wb_df=pd.DataFrame(columns=["PDB ID","Ligand","Binding Site","resnr","restype","reschain",
                                          "resnr_lig","restype_lig","reschain_lig","dist_a-w","dist_d-w","don_angle",
                                          "water_angle","protisdon","donor_idx","donortype","acceptor_idx","acceptortype",
                                          "water_idx","ligcoo_x","ligcoo_y","ligcoo_z","protcoo_x","protcoo_y","protcoo_z","watercoo_x","watercoo_y","watercoo_z"])         
    
        hp_all=pd.DataFrame()
        hyd_all=pd.DataFrame()
        sb_all=pd.DataFrame()
        metco_all=pd.DataFrame()
        wb_all=pd.DataFrame()
        data=pd.DataFrame()
        data_by_interactions=pd.DataFrame()
        for bs,bs_info in lig['bindingsites'].items():
            
            hydrophobic=bs_info['interactions']['hydrophobic_interactions']
            if(hydrophobic):
                for i, j in hydrophobic.items():
                    array=[]
                    array.append(lig['pdbid'])
                    array.append(lig['bindingsites'][bs]['identifiers']['longname'])
                    array.append(bs)
                    #print(i)
                    for prop in j.keys():
                        if(prop=='ligcoo' or prop=='protcoo'):
                            array.extend(j[prop].values())
                        else:
                            array.append(j[prop])
                    hp_df.loc['hydrophobic',:]=array
                    data=pd.concat([data,hp_df])
                    hp_all=pd.concat([hp_all,hp_df])
    
            hydrogen=bs_info['interactions']['hydrogen_bonds']
            if(hydrogen):
                for i, j in hydrogen.items():
                    array=[]
                    array.append(lig['pdbid'])
                    array.append(lig['bindingsites'][bs]['identifiers']['longname'])
                    array.append(bs)
                    #print(i)
                    for prop in j.keys():
                        if(prop=='ligcoo' or prop=='protcoo'):
                            array.extend(j[prop].values())
                        else:
                            array.append(j[prop])
                    hyd_df.loc['hydrogen',:]=array
                    data=pd.concat([data,hyd_df])
                    hyd_all=pd.concat([hyd_all,hyd_df])
    
            pi_stacks=bs_info['interactions']['pi_stacks']
            if(pi_stacks):
                for i, j in pi_stacks.items():
                    array=[]
                    array.append(lig['pdbid'])
                    array.append(lig['bindingsites'][bs]['identifiers']['longname'])
                    array.append(bs)
                    #print(i)
                    '''for prop in j.keys():
                        if(prop=='ligcoo' or prop=='protcoo'):
                            array.extend(j[prop].values())
                        else:
                            array.append(j[prop])
                    hyd_df.loc['hydrogen',:]=array
                    hyd_all=pd.concat([hyd_all,hyd_df])'''
    
    
            pi_cation=bs_info['interactions']['pi_cation_interactions']
            if(pi_cation):
                for i, j in pi_cation.items():
                    array=[]
                    array.append(lig['pdbid'])
                    array.append(lig['bindingsites'][bs]['identifiers']['longname'])
                    array.append(bs)
                    #print(i)
                    '''for prop in j.keys():
                        if(prop=='ligcoo' or prop=='protcoo'):
                            array.extend(j[prop].values())
                        else:
                            array.append(j[prop])
                    hyd_df.loc['hydrogen',:]=array
                    hyd_all=pd.concat([hyd_all,hyd_df])'''
            halogen=bs_info['interactions']['halogen_bonds']
            if(halogen):
                for i, j in halogen.items():
                    array=[]
                    array.append(lig['pdbid'])
                    array.append(lig['bindingsites'][bs]['identifiers']['longname'])
                    array.append(bs)
                    #print(i)
                    '''for prop in j.keys():
                        if(prop=='ligcoo' or prop=='protcoo'):
                            array.extend(j[prop].values())
                        else:
                            array.append(j[prop])
                    hyd_df.loc['hydrogen',:]=array
                    hyd_all=pd.concat([hyd_all,hyd_df])'''
            metal_complexes=bs_info['interactions']['metal_complexes']
            if(metal_complexes):
                for i, j in metal_complexes.items():
                    array=[]
                    array.append(lig['pdbid'])
                    array.append(lig['bindingsites'][bs]['identifiers']['longname'])
                    array.append(bs)
                    #print(i)
                    for prop in j.keys():
                        if(prop=='metalcoo' or prop=='targetcoo'):
                            array.extend(j[prop].values())
                        else:
                            array.append(j[prop])
                    metco_df.loc['metal complex',:]=array
                    data=pd.concat([data,metco_df])
                    metco_all=pd.concat([metco_all,metco_df])
    
            water_bridges=bs_info['interactions']['water_bridges']
            if(water_bridges):
                for i, j in water_bridges.items():
                    array=[]
                    array.append(lig['pdbid'])
                    array.append(lig['bindingsites'][bs]['identifiers']['longname'])
                    array.append(bs)
                    #print(i)
                    for prop in j.keys():
                        if(prop=='ligcoo' or prop=='protcoo' or prop=='watercoo'):
                            array.extend(j[prop].values())
                        else:
                            array.append(j[prop])
                    wb_df.loc['water bridge',:]=array
                    data=pd.concat([data,wb_df])
                    wb_all=pd.concat([wb_all,wb_df])
    
            salt_bridges=bs_info['interactions']['salt_bridges']
            if(salt_bridges):
                for i, j in salt_bridges.items():
                    array=[]
                    array.append(lig['pdbid'])
                    array.append(lig['bindingsites'][bs]['identifiers']['longname'])
                    array.append(bs)
                    #print(i)
                    for prop in j.keys():
                        if(prop!='lig_idx_list'):
                            if(prop=='ligcoo' or prop=='protcoo'):
                                array.extend(j[prop].values())
                            else:
                                array.append(j[prop])
                    sb_df.loc['salt bridge',:]=array
                    data=pd.concat([data,sb_df])
                    sb_all=pd.concat([sb_all,sb_df])
            data_by_interactions=pd.concat([hp_all,hyd_all,metco_all,sb_all,wb_all])
            #print(data_by_interactions)
        all_ligand_data=pd.concat([all_ligand_data,data_by_interactions])
    
    
    # In[141]:
    
    
    all_ligand_data.to_csv(output)
    

def main(argv):
   json1F = ''
   json2F = ''
   output = ''
   try:
     # opts, args = getopt.getopt(argv,"hx:j:",["xmlfile=","jsonfile="])
     opts, args = getopt.getopt(argv,"hj1:j2:o:",["jsonfile1=","jsonfile2=","outputCsv="])
   except getopt.GetoptError:
      print('[error] DiffAnalysis.py -j1 <jsonfile1> -j2 <jsonfile2> -o <outputCsv>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('xmlToJSON.py -j1 <jsonfile1> -j2 <jsonfile2> -o <outputCsv>')
         print("-" * 25)
         print('-j1 --jsonfile1:\tFirst JSON file obtained by xmlToJSON.py script')
         print('-j2 --jsonfile2:\tSecond JSON file obtained by xmlToJSON.py script')
         print('-o --outputCsv:\tCSV output file') 
         
         
         sys.exit()
      elif opt in ("-j1", "--jsonfile1"):
         json1F = arg
      elif opt in ("-j2", "--jsonfile2"):
         json2F = arg
      elif opt in ("-o", "--outputCsv"):
         output = arg
   
   run(json1F,json2F,output)

if __name__ == "__main__":
   main(sys.argv[1:])  
    
    
