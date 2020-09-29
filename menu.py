#!/usr/bin/python3

print("Content-type: text/html\n\n")
print()

menu_css='''<style>
body
{
	margin: 0;
	padding: 0;
	display: flex;
	justify-content: center;
	align-items: center;
	min-height: 40vh;
	background: #031230;
	font-family: consolas;
}
h
{
	position: relative;
	display: inline-block;
	padding: 15px 30px;
	color: #2196f3;
	text-transform: uppercase;
	letter-spacing: 4px;
	text-decoration: none;
	font-size: 40px;
	overflow: hidden;
	transition: 0.2s;
}

h span
{
	position :absolute;
	display: block;
}
h span:nth-child(1)
{
	top: 0;
	Left: -100%;
	width: 100%;
	height: 2px;
	background: linear-gradient(90deg,transparent,#2196f3);
}
h:hover span:nth-child(1)
{
	Left:100%;
	transition: 1s;
}
h span:nth-child(2)
{
	top: -100%;
	right: 0;
	width: 2px;
	height: 100%;
	background: linear-gradient(180deg,transparent,#2196f3);
}
h:hover span:nth-child(2)
{
	top:100%;
	transition: 1s;
	transition-delay: 0.25s;
}
h span:nth-child(3)
{
	bottom: 0;
	right: -100%;
	width: 100%;
	height: 2px;
	background: linear-gradient(270deg,transparent,#2196f3);
}
h:hover span:nth-child(3)
{
	right:100%;
	transition: 1s;
	transition-delay: 0.5s;
}
h span:nth-child(4)
{
	bottom: -100%;
	left: 0;
	width: 2px;
	height: 100%;
	background: linear-gradient(360deg,transparent,#2196f3);
}
h:hover span:nth-child(4)
{
	bottom:100%;
	transition: 1s;
	transition-delay: 0.75s;
}
p
{
	color: #2196f3;
	text-transform: uppercase;
	letter-spacing: 4px;
	font-size: 15px;
} </style>'''


import subprocess,cgi

cmd_list=['1.DATE ',' 2.TIME', '3.CALENDER', '4.DAY' , '5.CALCULATE {operand} {operator} {operand}']
days={'Mon':'monday','Tue':'Tuesday','Wed':'wednesday','Thur':'thursday','Fri':'friday','Sat':'saturday','Sun':'sunday'}

def run_cmd(c):
	y=subprocess.getstatusoutput(c)
	if y[0] == 0:
		return y[1]
	else:
		return 99

def get_cmd():
	form = cgi.FieldStorage() 
	x=form.getvalue("x")
	if x==None:
		return "You didn't enter any querry!."
	else:
		d=list(x.split())
	if 'date' in d:
		out=run_cmd('date')
		if out ==99:
			return 'Some error occured.'
		ret = list(out.split())
		return f"Today's date is {ret[2]}th {ret[1]} {ret[5]}."
	elif 'calender' in d:
		out=run_cmd('cal')
		if out ==99:
			return 'Some error occured.'
		return f"<input type=Submit value='{out}' />"
	elif ('editor' in d) and ('text' in d):
		return "Sorry! That is outside our scope.<br><br>Can't open any graphical interface."
	elif ('list' in d) and ('commands' in d):
		cmdlist='All commands that this site supports : <br>'
		for i in cmd_list:
			cmdlist+=i
			cmdlist+='<br>'
		return cmdlist
	elif 'time' in d:
		out=run_cmd('date')
		if out ==99:
			return 'Some error occured.'
		ret= list(out.split())
		return f'Now it is {ret[3]} {ret[4]}'
	elif ('today' in d) or ('day' in d):
		out=run_cmd('date')
		if out ==99:
			return 'Some error occured.'
		ret=list(out.split())
		day=days[ret[0]]
		return f'Today is {day} <br>have a nice day!'
	elif 'browser' in d:
		out=run_cmd('firefox')
		if out ==99:
			return 'Some error occured.'
		return f'Now it is {out}'
	elif 'calculate' in d:
		if len(d)<4:
			return 'Enter all operands along with operators and spaces in between them to get the correct value.'
		else:
			out=run_cmd(f'expr {d[1]} {d[2]} {d[3]}')
		if out ==99:
			return 'Some error occured.'
		return f'The result is {out}'
	else:
		return "Sorry! Couldn't understand your querry."

result = get_cmd()
menu_html_out=f'''<!doctype html>
<html>
	<head>
		<title>MENU</title>
		{menu_css}
	</head>
	<body>
		<center><p><h>
			<span></span>
			<span></span>
			<span></span>
			<span></span>
			<u>my linux terminal</u>
		</h></p>
		<form action ='http://192.168.43.99/webpages/menu.html'>
			<p>
				<br><br>LINUX TERMINAL 
				<br><br>{result}
				<br><br><input type=Submit value='RETURN' />
			</p>
		</form>
		</center>
	</body>
</html>'''
print(menu_html_out)
