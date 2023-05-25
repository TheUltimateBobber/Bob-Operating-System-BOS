import os, time, random, subprocess
from operations import *
def CMDinterp(interpret):
	if(interpret == '.help'):
		print('.help - help')
		print('bos.clear - clears screen')
		print('bos - mini info screen')
		print('print <input> - prints what is inputted by the user')
		print('pyexec <input> - executes python code in input')
	elif(interpret == 'bos.clear'):
		operation(2)
	elif(interpret == 'bos.UseLineEmptyMethod'):
		LineEmpty()
	elif(interpret == 'bos' or interpret == 'BOS'):
		print('Bob Operating System (BOS)')
		print('created in 2022')
		print('version 1.1')
		print('can be used as a template for another OS.')
		print('use .help for help')
	elif(interpret[0:5] == 'print' or interpret[0:5] == 'PRINT'):
		print(interpret[6:len(interpret)])
	elif(interpret[0:6] == 'pyexec' or interpret[0:6] == 'PYEXEC'):
		try:
			exec(interpret[7:len(interpret)])
		except:
			print('Error in python code')
			print('Type: ' + str(Exception))
	else: print('unknown command')
def LineEmpty():
	print('                                            ' * 2000)
def run():
	print("")
	wait(1.65)
	operation(2)
	print('Bob Operating System (BOS)')
	print('ALL COMMANDS ARE CASE SENSITIVE UNLESS STATED NOT.')
	print('use lowercase')
	print('.help for help')
	while True:
		CMDinterp(input('bos > '))