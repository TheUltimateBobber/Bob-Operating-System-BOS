import os, time, random, subprocess
import pc

def wait(wt):
	time.sleep(float(wt))
def rebootNorm():
	pc.__bootmodeset__('norm')
	pc.__safemodeset_(True)
	pc.start()
def operation(operationtype=0o01001001):
	if(operationtype == 0):
		wait(1)
	elif(operationtype == 1):
		pc.start()
	elif(operationtype == 2):
		subprocess.call('clear')
	elif(operationtype == 3): pc.start()
	elif(operationtype == 0o01001001):
		print('No Operation')
	else:
		print('Invalid Operation?')