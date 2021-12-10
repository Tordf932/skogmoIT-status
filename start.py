from pygame import register_quit
import itscreen, webserver
import multiprocessing
import time

def itpygame():
	itscreen.run()

def itwebserver():
	webserver.webstart()

if __name__ == '__main__':
	p1 = multiprocessing.Process(name='p1', target=itpygame)
	p = multiprocessing.Process(name='p', target=itwebserver)
	started = True
	if started:
		p1.start()
		p.start()
		started = False
	else:
		print("Already started")
