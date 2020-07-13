#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 2020

@author: Aaron Ayllon Benitez
@description: Hackathon ISMB 2020 - Team 3A - Task 1
"""
import sys, getopt
import xml.etree.ElementTree as ET
import json

def returnNumeric(s):
    if s !=None :
        x = s.split(".")
        if(x[0].isdigit() or  ("-" in x[0] and x[0].split("-")[1].isdigit())):
            try: 
            
                return int(s)
            except ValueError:
                return float(s)
        else:
            return s
    else:
        return s

def getJSON(r,export):
    r = json.dumps(r,indent=2)
    #loaded_r = json.loads(r)
    #loaded_r['identifiers'] #Output 3.5
    #type(r) #Output str
    #type(loaded_r) #Output dict
    f = open(export, "w")
    f.write(r)
    f.close()
def recursiveTags(elem):

    if(list(elem)[0].tag in elem.tag):
        dic = {}
        for e in list(elem):
            if len(list(e))>0:
                dic[e.attrib["id"]] = recursiveTags(e)
            else:
                if e.text!=None and len(e.items())>1:
                    dicItems = {}
                    for t in e.items():
                        if t[0] != "id":
                            dicItems[t[0]] = returnNumeric(t[1])
                    dicItems["value"] = returnNumeric(e.text)
                    
                    dic[e.attrib["id"]] = dicItems
                else:
                    dic[e.attrib["id"]] = returnNumeric(e.text)
        return dic
    else:
        dic = {}
        for e in list(elem):
            if len(list(e))>0:
                dic[e.tag] = recursiveTags(e)
            else:
                dic[e.tag] = returnNumeric(e.text)
        return dic



def parseXML(file_name,output):
   # Parse XML with ElementTree
   tree = ET.ElementTree(file=file_name)
   root = tree.getroot()

   # get the information via the children!
   print("-" * 25)
   print("Parsing PILP XML result to json")
   print("-" * 25)
   dicF={}
   dicF["bindingsites"] = {}
   #dicF["covlinkages"]  = {}
   users =list(root)
   for user in users:
      if user.tag == "bindingsite" :
          dicF["bindingsites"][user.attrib["id"]] = {}
          dicF["bindingsites"][user.attrib["id"]]["has_interactions"] = returnNumeric(user.attrib["has_interactions"])
          dicF["bindingsites"][user.attrib["id"]] = recursiveTags(user)
         
      elif user.tag == "covlinkages" and len(list(user))>0:
           dicF[user.tag]= recursiveTags(user)
      elif user.tag == "pdbid":
          dicF[user.tag] = user.text
        
   getJSON(dicF,output)

def main(argv):
   xmlF = ''
   jsonF = ''
   try:
     # opts, args = getopt.getopt(argv,"hx:j:",["xmlfile=","jsonfile="])
     opts, args = getopt.getopt(argv,"hx:",["xmlfile="])
   except getopt.GetoptError:
      print('[error] xmlToJSON.py -x <xmlfile> [-j <jsonfile>]')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('xmlToJSON.py -x <xmlfile> -j <jsonfile>')
         print("-" * 25)
         print('-x --xmlfile:\tPILP xml file input')
         print('-j --jsonfile:\t [OPT] json file output. Default: [xmlfileName.json]')
         
         
         sys.exit()
      elif opt in ("-x", "--xmlfile"):
         xmlF = arg
      elif opt in ("-j", "--jsonfile"):
         jsonF = arg
   if jsonF == "":
        jsonF = xmlF.split(".")[0]+".json"
   parseXML(xmlF,jsonF)

if __name__ == "__main__":
   main(sys.argv[1:])