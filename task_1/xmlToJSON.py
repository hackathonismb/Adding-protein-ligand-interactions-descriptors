import xml.etree.ElementTree as ET
import json

def returnNumeric(s):
    try: 
        
        return int(s)
    except ValueError:
        return float(s)

def getJSON(r,export):
    r = json.dumps(r,indent=2)
    #loaded_r = json.loads(r)
    #loaded_r['identifiers'] #Output 3.5
    #type(r) #Output str
    #type(loaded_r) #Output dict
    f = open(export+".json", "w")
    f.write(r)
    f.close()
def recursiveTags(elem,dic):
    for e in list(elem):
        if len(list(e))>0:
            dic[e.tag] = {}
            recursiveTags(e,dic[e.tag])
        else:
            if e.text!=None and len(e.items())>0:
                dic[e.tag] = {}
                
                x = e.text.split(".")
                if(x[0].isdigit() or  ("-" in x[0] and x[0].split("-")[1].isdigit())):
                    dic[e.tag]["value"] = returnNumeric(e.text)
                else:
                    dic[e.tag]["value"] = e.text
                dic[e.tag]["atr"] = {}
                for i in e.items():
                    dic[e.tag]["atr"][i[0]] = i[1]
            elif e.text!=None:
                x = e.text.split(".")
                if x[0].isdigit() or ("-" in x[0] and x[0].split("-")[1].isdigit()):
                    dic[e.tag] = returnNumeric(e.text)
                else:
                     dic[e.tag] = e.text
               


def parseXML(file_name):
   # Parse XML with ElementTree
   tree = ET.ElementTree(file=file_name)
   root = tree.getroot()

   # get the information via the children!
   print("-" * 25)
   print("Parsing PILP XML result to json")
   print("-" * 25)
   dicF={}
   dicF["bindingsites"] = {}
   dicF["covlinkages"]  = {}
   users =list(root)
   for user in users:
      if user.tag == "bindingsite":
          dic={}
          user_children = list(user)
          dicF["bindingsites"][user.items()[0][1]]={}
          dicF["bindingsites"][user.items()[0][1]]["has_interactions"]=user.items()[1][1]
          
          
          for user_child in user_children:
             if user_child.tag == "identifiers": 
                dic["identifiers"] = {} 
                recursiveTags(list(user_child),dic["identifiers"])
             if user_child.tag == "lig_properties":
                 dic["lig_properties"] = {} 
                 recursiveTags(list(user_child),dic["lig_properties"])
             if user_child.tag == "interacting_chains":
                 dic["interacting_chains"] = {} 
                 recursiveTags(list(user_child),dic["interacting_chains"])
             if user_child.tag == "bs_residues":
                 dic["bs_residues"] = {} 
                 recursiveTags(list(user_child),dic["bs_residues"])    
             if user_child.tag == "interactions":
                 dic["interactions"] = {} 
                 recursiveTags(list(user_child),dic["interactions"])  
             if user_child.tag == "mappings":
                 dic["mappings"] = {} 
                 recursiveTags(list(user_child),dic["mappings"])
          dicF["bindingsites"][user.items()[0][1]]["information"]=dic
      if user.tag == "covlinkages":
          dicF["covlinkages"]={}
          user_children = list(user)
          
          for user_child in user_children:
              
              dicF["covlinkages"][user_child.items()[0][1]]={}
              recursiveTags(list(user_child),dicF["covlinkages"][user_child.items()[0][1]])
          
        
   getJSON(dicF,file_name.split(".")[0])

if __name__ == "__main__":
   parseXML("test_data/2hu4.xml")