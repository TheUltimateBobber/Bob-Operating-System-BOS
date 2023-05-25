import os, time, random, subprocess, boot
def __bootmodeset__(bootmode):
	global BOOTMODE
	BOOTMODE = bootmode
def testbootmode():
	try:
		print('BootMode>'+BOOTMODE)
	except:
		print("no BOOTMODE variable?")
def __safemodeset__(safemode):
	global SAFEMODE
	SAFEMODE = safemode
def testsafemode():
	try:
		print('SafeMode>'+str(SAFEMODE))
	except:
		print("no SAFEMODE variable?")
def start():
	boot.start(BOOTMODE, SAFEMODE)