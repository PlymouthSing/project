#!/usr/bin/python3

print("Content-type:text/html\r\n\r\n")

print("""
	<html>
	<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>Security Regulation Generator</title>
	<style type="text/css">
		#CompanyInformation { width: 350px; margin: 100px auto; }
	</style>
	</head>
	<body>
	<div id="CompanyInformation">
		<form id="infoForm" name="infoForm" method="post" action="">
		<fieldset>
			<legend>Enter company information</legend>
			<p>
			<label for="username">Username</label>
			<br />
			<input type="text" id="username" name="username" class="text" size="20" />
			</p>
			<p>
			<label for="password">Password</label>
			<br />
			<input type="password" id="password" name="password" class="text" size="20" />
			</p>
			<p>
			<button type="submit" class="button positive">Login</button>
			</p>
		</fieldset>
		</form>
	</div>
	</body>
	</html>
	""")

