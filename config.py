input('press enter to boot BOS')
import pc
def StartSystem():
	pc.__bootmodeset__('norm')
	pc.testbootmode()
	pc.__safemodeset__(True)
	pc.testsafemode()
	pc.start()
StartSystem()