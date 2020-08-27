#!/usr/bin/python3

import cgi
import cgitb
import datetime
import hashlib
import pymongo

class Block:
    def __init__(self, index, data, timestamp, p_hash):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.p_hash = p_hash
        self.hash = self.hashing()

    def hashing(self):
        h = hashlib.sha256()
        h.update(str(self.index).encode("UTF-8"))
        h.update(str(self.data).encode("UTF-8"))
        h.update(str(self.timestamp).encode("UTF-8"))
        h.update(str(self.p_hash).encode("UTF-8"))
        return h.hexdigest()

class Chain:
    def __init__(self):
        self.blocks = [self.initial_block()]

    def chain_size(self):
        return len(self.blocks) - 1

    def add_block(self, data):
        self.blocks.append(Block(len(self.blocks),
            data,
            datetime.datetime.utcnow(),
            self.blocks[len(self.blocks) - 1].hash))

    def initial_block(self):
        return Block(0, "Blockchain starts here!",
            datetime.datetime.utcnow(), "Hash Code!")

cgitb.enable()
form = cgi.FieldStorage()

companyname = None
businesstype = None
organizationsize = None
numberofworkstations = None
numberofservers = None
editor = None
typeofpolicy = None
result = None
gen = None
hashcode = None
find = None

if form.getvalue("companyname"):
    companyname = form.getvalue("companyname")

if form.getvalue("businesstype"):
    businesstype = form.getvalue("businesstype")

if form.getvalue("organizationsize"):
    organizationsize = form.getvalue("organizationsize")

if form.getvalue("numberofworkstations"):
    numberofworkstations = form.getvalue("numberofworkstations")

if form.getvalue("numberofservers"):
    numberofservers = form.getvalue("numberofservers")

if form.getvalue("editor"):
    editor = form.getvalue("editor")

if form.getvalue("typeofpolicy"):
    typeofpolicy = form.getvalue("typeofpolicy")

if form.getvalue("gen"):
    gen = form.getvalue("gen")

if form.getvalue("hashcode"):
    hashcode = form.getvalue("hashcode")

if form.getvalue("find"):
    find = form.getvalue("find")

if companyname\
        and businesstype\
        and organizationsize\
        and numberofworkstations\
        and numberofservers\
        and editor\
        and typeofpolicy:
    filled = 1
else:
    filled = 0

if gen == "Generate" and filled == 1:
    document = Chain()
    document.add_block(companyname)
    document.add_block(businesstype)
    document.add_block(organizationsize)
    document.add_block(numberofworkstations)
    document.add_block(numberofservers)
    document.add_block(editor)
    document.add_block(typeofpolicy)
    result = "empty"
    document.add_block(result)
    
    hashcode = document.blocks[document.chain_size()].hashing()



print("Content-type:text/html\r\n\r\n")

print("""
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Security Regulation Generator</title>
<style type="text/css">
    #CompanyInformation {
        width: 800px;
        margin: 50px auto;
    }
    
    table, th, td {
        border: 1px solid white;
        border-collapse: collapse;
    }
    
    th, td {
        padding: 5px;
        text-align: left;
    }
</style>
</head>
""")

print("""
<body>
<div id="CompanyInformation">
    <form method="post">
    <fieldset>
    <legend>Enter company information</legend>
        <table style="width:100%;">
        <tr>
        <td colspan="2">
        <label for="companyname">Name of Company</label>
        <br />
""")

if companyname != None:
    print(f"""
        <input type="text" id="companyname" name="companyname" style="width:100%;" value="{companyname}" />
    """)
else:
    print(f"""
        <input type="text" id="companyname" name="companyname" style="width:100%;" />
    """)

print("""
        </td>
        </tr>
        <tr>
        <td style="width:50%;">
        <label for="businesstype">Type of Business</label>
        <br />
        <select id="businesstype" name="businesstype" style="width:150px;">
            <option value="">-</option>
""")

if businesstype == "Education":
    print("""<option selected value="Education">Education</option>""")
else:
    print("""<option value="Education">Education</option>""")

if businesstype == "Retail":
    print("""<option selected value="Retail">Retail</option>""")
else:
    print("""<option value="Retail">Retail</option>""")

if businesstype == "IT Services":
    print("""<option selected value="IT Services">IT Services</option>""")
else:
    print("""<option value="IT Services">IT Services</option>""")

if businesstype == "Other":
    print("""<option selected value="Other">Other</option>""")
else:
    print("""<option value="Other">Other</option>""")

print("""
        </select>
        </td>
        <td style="width:50%;">
        <label for="organizationsize">Size of Organization</label>
        <br />
        <select id="organizationsize" name="organizationsize" style="width:150px;">
            <option value="">-</option>
""")

if organizationsize == "10":
    print("""<option selected value="10">< 10 employees</option>""")
else:
    print("""<option value="10">< 10 employees</option>""")

if organizationsize == "11~50":
    print("""<option selected value="11~50">11 ~ 50 employees</option>""")
else:
    print("""<option value="11~50">11 ~ 50 employees</option>""")

if organizationsize == "51~200":
    print("""<option selected value="51~200">51 ~ 200 employees</option>""")
else:
    print("""<option value="51~200">51 ~ 200 employees</option>""")

if organizationsize == "201":
    print("""<option selected value="201">> 201 employees</option>""")
else:
    print("""<option value="201">> 201 employees</option>""")

print("""
        </select>
        </td>
        </tr>
        <tr>
        <td>
        <label for="numberofworkstations">Number of Workstations</label>
        <br />
        <select id="numberofworkstations" name="numberofworkstations" style="width:150px;">
            <option value="">-</option>
""")

if numberofworkstations == "10":
    print("""<option selected value="10">< 10 workstations</option>""")
else:
    print("""<option value="10">< 10 workstations</option>""")

if numberofworkstations == "11~50":
    print("""<option selected value="11~50">11 ~ 50 workstations</option>""")
else:
    print("""<option value="11~50">11 ~ 50 workstations</option>""")

if numberofworkstations == "51~200":
    print("""<option selected value="51~200">51 ~ 200 workstations</option>""")
else:
    print("""<option value="51~200">51 ~ 200 workstations</option>""")

if numberofworkstations == "201":
    print("""<option selected value="201">> 201 workstations</option>""")
else:
    print("""<option value="201">> 201 workstations</option>""")

print("""
        </select>
        </td>
        <td>
        <label for="numberofservers">Number of Servers</label>
        <br />
        <select id="numberofservers" name="numberofservers" style="width:150px;">
            <option value="">-</option>
""")

if numberofservers == "0":
    print("""<option selected value="0">0 servers</option>""")
else:
    print("""<option value="0">0 servers</option>""")

if numberofservers == "1~5":
    print("""<option selected value="1~5">1 ~ 5 servers</option>""")
else:
    print("""<option value="1~5">1 ~ 5 servers</option>""")

if numberofservers == "6~15":
    print("""<option selected value="6~15">6 ~ 15 servers</option>""")
else:
    print("""<option value="6~15">6 ~ 15 servers</option>""")

if numberofservers == "15":
    print("""<option selected value="15">> 15 servers</option>""")
else:
    print("""<option value="15">> 15 servers</option>""")

print("""
        </select>
        </td>
        </tr>
        <tr>
        <td></td>
        </tr>
        <tr>
        <td>
        <label for="editor">Editor</label>
        <br />
""")

if editor != None:
    print(f"""
        <input type="text" id="editor" name="editor" style="width:150px;" value="{editor}" />
    """)
else:
    print("""
        <input type="text" id="editor" name="editor" style="width:150px;" />
    """)

print("""
        </td>
        </tr>
        <tr>
        <td colspan="2">
        <label for="typeofpolicy">Type of  policy to be generated: </label>
        <select id="typeofpolicy" name="typeofpolicy" style="width:150px;">
            <option value="">-</option>
""")

if typeofpolicy == "WiFi":
    print("""<option selected value="WiFi">WiFi Policy</option>""")
else:
    print("""<option value="WiFi">WiFi Policy</option>""")

if typeofpolicy == "Password":
    print("""<option selected value="Password">Password Policy</option>""")
else:
    print("""<option value="Password">Password Policy</option>""")

print("""
        </select>
        <input type="submit" id="gen" name="gen" value="Generate" />
        </td>
        </tr>
    </table>
    </fieldset>
    </form>
</div>
<div id="CompanyInformation">
    <form method="post">
    <fieldset>
    <legend>Policy Hash Code</legend>
        <table style="width:100%;">
""")

if hashcode != None:
    print(f"""
        <input type="text" id="hashcode" name="hashcode" style="width:700px;" value="{hashcode}" />
    """)
else:
    print(f"""
        <input type="text" id="hashcode" name="hashcode" style="width:700px;" />
    """)

print("""
        <input type="submit" id="find" name="find" value="Find" />
        </table>
    </fieldset>
    </form>
</div>
<div id="CompanyInformation">
    <fieldset>
    <legend>Policy</legend>
        <table style="width:100%;">
""")

if gen == "Generate" and filled == 1:
    print(f"""
        <tr>
        <td style="text-align: center; font-size: 50px">
        {typeofpolicy} Policy
        </td>
        </tr>
        <tr>
        <td>
        {result}
        </td>
        </tr>
    """)
else:
    print("""
        <tr>
        <td style="text-align: center; font-size: 50px">
        Waiting for generation
        </td>
        </tr>
    """)

print("""
        </table>
    </fieldset>
</div>
""")

#print(client.list_database_names())
#print("<br />")
#print(database.list_collection_names())
#print("<br />")

#for i in collection.find():
#    print(i)
#    print("<br />")

#collection.drop()


if gen == "Generate" and filled == 1:
    print(document.chain_size())
    print("<br />")
    
    for i in range(document.chain_size() + 1):
        print(document.blocks[i].index)
        print("<br />")
        print(document.blocks[i].data)
        print("<br />")
        print(document.blocks[i].timestamp)
        print("<br />")
        print(document.blocks[i].p_hash)
        print("<br />")

print("</body>")
print("</html>")

