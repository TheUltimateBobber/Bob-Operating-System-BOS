response = input('It is highly recommended that you use the fix-main branch or the latest release! (type "n" to abort')
if(reponse == 'n' or response == 'N'):
  import time
  print('please download the fix-main branch version, or use one of the releases.')
  time.sleep(99999999)
import pc
def StartSystem():
	pc.__bootmodeset__('norm')
	pc.testbootmode()
	pc.__safemodeset__(True)
	pc.testsafemode()
	pc.start()
StartSystem()
