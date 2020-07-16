import { Template } from 'meteor/templating';
import { Session } from 'meteor/session';
import { Meteor } from 'meteor/meteor';
import "./body.html";

function Table() {
    //sets attributes
    this.header = [];
    this.data = [[]];
    this.tableClass = '';
    this.tableID = '';
}

Table.prototype.setHeader = function(keys) {
    //sets header data
    this.header = keys
    return this
}

Table.prototype.setData = function(data) {
    //sets the main data
    this.data = data
    return this
}

Table.prototype.setTableClass = function(tableClass) {
    //sets the table class name
    this.tableClass = tableClass
    return this
}
Table.prototype.setTableID = function(tableID) {
    //sets the table class name
    this.tableID = tableID;
    return this
}

Table.prototype.build = function(container) {

    //default selector
    container = container || '#tableResult'

    //creates table
    var table = $('<table id="' +this.tableID +'" class="'+this.tableClass+'"></table>').addClass(this.tableClass)

    var tr = $('<tr></tr>') //creates row
    var th = $('<th class="all"></th>') //creates table header cells
    var thN = $('<th class="none"></th>') //creates table header cells
    var td = $('<td></td>') //creates table cells

    var header = tr.clone() //creates header row

    //fills header row
    this.header.forEach(function(d) {

            var thClone = th.clone();
        	thClone.text(d);
            header.append(thClone);




    })

    //attaches header row
    table.append($('<thead></thead>').append(header))

    //creates
    var tbody = $('<tbody></tbody>')

    //fills out the table body
    this.data.forEach(function(d) {
        var row = tr.clone() //creates a row
        d.forEach(function(e,j) {
            row.append(td.clone().text(e)) //fills in the row
        })
        tbody.append(row) //puts row on the tbody
    })

    $(container).append(table.append(tbody)) //puts entire table in the container
    console.log(table.html());
    return table.html();
}




if (Meteor.isClient) {
    Session.setDefault('page', 'home');
    Session.setDefault('Myprots', null);
        Template.body.helpers({
            currentPage: function(page){
                return Session.get('page')
            }
        });

        Template.body.events({
            'click .clickChangesPage': function(event, template){
                Session.set('page', event.currentTarget.getAttribute('data-page'))
            }
        });

    Template.task1.events({

     'submit form': function(event) {
        event.preventDefault();
        var prot1 = event.target.prot1.value;
        var prot2 = event.target.prot2.value;
        console.log(prot1);
        console.log(prot2);
        var sameF = event.target.sameForm.value;
        console.log(sameF);
        event.target.prot1.value = "";
        event.target.prot2.value = "";
        Session.set('page', "loading")
        Meteor.call('runPlip', prot1, prot2, function(err, res) {
          if(err) console.error(err);
          //else console.log(res);
          Session.set("Myprots",res);
          Session.set('page','result1');
   });
     }
  });
  Template.firstProtein.helpers({
    pdb(){
      if(Session.get("Myprots")!=null){
        return Session.get("Myprots")[0].pdbid;
      }
    },
  name(){
      if(Session.get("Myprots")!=null){
    return  Session.get("Myprots")[0].pdbname ;
  }
    },
  icn3d(){
      if(Session.get("Myprots")!=null){
        return "https://www.ncbi.nlm.nih.gov/Structure/icn3d/full.html?mmdbid="+Session.get("Myprots")[0].pdbid+"&width=600&height=600&showcommand=0&mobilemenu=1&showtitle=0";

    }
    }
  });
  Template.secondProtein.helpers({
    pdb(){
      if(Session.get("Myprots")!=null){
return  Session.get("Myprots")[1].pdbid;
}
},
name(){
  if(Session.get("Myprots")!=null){
return  Session.get("Myprots")[1].pdbname ;
}
},
  icn3d(){
      if(Session.get("Myprots")!=null){

        return "https://www.ncbi.nlm.nih.gov/Structure/icn3d/full.html?mmdbid="+Session.get("Myprots")[1].pdbid+"&width=600&height=600&showcommand=0&mobilemenu=1&showtitle=0";
              }
    }
  });


  Template.commonProts.onRendered(function () {
      var table = new Table();
      console.log(table);
      console.log("hola");
      console.log(Session.get("Myprots")[2]);
      var t = table
      .setHeader(Session.get("Myprots")[2])
      .setData(Session.get("Myprots")[3])
      .setTableClass('table table-striped table-bordered')
      .setTableID('tableMod')
      .build("#com");

  });



}
