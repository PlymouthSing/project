#!/usr/bin/python3

print("Content-type:text/html\r\n\r\n")

print("""

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Security Regulation Generator</title>
<style type="text/css">
    #CompanyInformation {
        width: 800px;
        margin: 100px auto;
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
<body>
<div id="CompanyInformation">
    <form id="infoForm" name="infoForm" method="post">
    <fieldset>
    <legend>Enter company information</legend>
        <table style="width:100%;">
        <tr>
        <td colspan="2">
        <label for="companyname">Name of Company</label>
        <br />
        <input type="text" id="companyname" name="companyname" style="width:100%;" />
        </td>
        </tr>
        <tr>
        <td style="width:50%;">
        <label for="businesstype">Type of Business</label>
        <br />
        <select id="businesstype" name="businesstype" style="width:150px;">
            <option value="No Information">No Information</option>
            <option value="Education">Education</option>
            <option value="Retail">Retail</option>
            <option value="Financial Services">Financial Services</option>
            <option value="IT Services">IT Services</option>
            <option value="Legal Services">Legal Services</option>
            <option value="Other">Other</option>
        </select>
        </td>
        <td style="width:50%;">
        <label for="organizationsize">Size of Organization</label>
        <br />
        <select id="organizationsize" name="organizationsize" style="width:150px;">
            <option value="No Information">No Information</option>
            <option value="10">< 10 employees</option>
            <option value="1150">11 ~ 50 employees</option>
            <option value="51200">51 ~ 200 employees</option>
            <option value="201">> 201 employees</option>
        </select>
        </td>
        </tr>
        <tr>
        <td>
        <label for="numberofworkstations">Number of Workstations</label>
        <br />
        <select id="numberofworkstations" name="numberofworkstations" style="width:150px;">
            <option value="No Information">No Information</option>
            <option value="10">< 10 workstations</option>
            <option value="1150">11 ~ 50 workstations</option>
            <option value="51200">51 ~ 200 workstations</option>
            <option value="201">> 201 workstations</option>
        </select>
        </td>
        <td>
        <label for="numberofservers">Number of Servers</label>
        <br />
        <select id="organizationsize" name="organizationsize" style="width:150px;">
            <option value="No Information">No Information</option>
            <option value="0">0 servers</option>
            <option value="15">1 ~ 5 servers</option>
            <option value="615">6 ~ 15 servers</option>
            <option value="15">> 15 servers</option>
        </select>
        </td>
        </tr>
        <tr>
        <td></td>
        </tr>
        <tr>
        <td colspan="2">
        <label for="typeofpolicy">Type of  policy to be generated: </label>
        <select id="typeofpolicy" name="typeofpolicy" style="width:150px;">
            <option value="No Information">No Information</option>
            <option value="WiFi">WiFi Policy</option>
        </select>
        <input type="submit" value="Generate" />
        </td>
        </tr>
    </table>
    </fieldset>
    </form>
</div>
</body>
</html>

""")

