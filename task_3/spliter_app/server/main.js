import { Meteor } from 'meteor/meteor';

Meteor.startup(() => {
  var exec = require('child_process').exec;
  var execSync = require('child_process').execSync;
  const parse = require('csv-parse/lib/sync')

  // code to run on server at startup
  Meteor.methods({
    runPlip(arg1, arg2) {
      console.log("running protein: "+arg1);
      execSync("../../../../../server/src/plip_v2.1.3.simg -i "+arg1+" -vx -o "+arg1, function (error, stdout, stderr) {
      if (error !== null) {
          console.log('exec error: ' + error);
       }
       });
       execSync("../../../../../xmlToJSON.py -x "+arg1+"/report.xml", function (error, stdout, stderr) {
        if (error !== null) {
          console.log('exec error: ' + error);
     }
    });
    execSync("../../../../../modifyJSON.py -j "+arg1+"/report.json -p "+arg1+"/"+arg1+".pdb", function (error, stdout, stderr) {
     if (error !== null) {
       console.log('exec error: ' + error);
  }
 });
  console.log("running protein: "+arg2);
   execSync("../../../../../server/src/plip_v2.1.3.simg -i "+arg2+" -vx -o "+arg2, function (error, stdout, stderr) {
      if (error !== null) {
        console.log('exec error: ' + error);
   }
});
    execSync("../../../../../xmlToJSON.py -x "+arg2+"/report.xml", function (error, stdout, stderr) {
    if (error !== null) {
      console.log('exec error: ' + error);
 }
});

execSync("../../../../../modifyJSON.py -j "+arg2+"/report.json -p "+arg2+"/"+arg2+".pdb", function (error, stdout, stderr) {
if (error !== null) {
  console.log('exec error: ' + error);
}
});
execSync("../../../../../Protein_Ligand_Interactions-common-residues.py -f "+arg1+"/report.json -s "+arg2+"/report.json -o common.csv", function (error, stdout, stderr) {
if (error !== null) {
  console.log('exec error: ' + error);
}
});

var common = execSync("cat common.csv", function (error, stdout, stderr) {
if (error !== null) {
  console.log('exec error: ' + error);
}
return stdout;
});

var prot1 = execSync("cat "+arg1+"/report.json", function (error, stdout, stderr) {
if (error !== null) {
  console.log('exec error: ' + error);
}
return stdout;
});
var prot2 = execSync("cat "+arg2+"/report.json", function (error, stdout, stderr) {
if (error !== null) {
  console.log('exec error: ' + error);
}
return stdout;
});
var prot1 = JSON.parse(prot1);
var prot2 =JSON.parse(prot2);
const records = parse(common, {
  delimiter: [",","\t"],
  trim: true,
  columns: true,
})

var h =["pdbID","Protein residue number","Protein chain","Protein residue type","Interaction type",
"Ligand residue number","Ligand residue chain","Ligand residue type"];
   var r = [];
records.forEach((rec,index) => {

  var cells = [];
  Object.entries(rec).forEach(([key, value]) => {
    cells.push(value);
  })
  r.push(cells);
})

exec("rm -R "+arg2+ " " + arg1+" common.csv", function (error, stdout, stderr) {
    if (error !== null) {
      console.log('exec error: ' + error);
 }
});
    var prots = [prot1,prot2,h,r];

      return prots;
    }
});


});
