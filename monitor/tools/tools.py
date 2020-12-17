import socket
from json import load
from urllib.request import urlopen
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os


def get_host_ip():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(('8.8.8.8', 80))
		ip = s.getsockname()[0]
	finally:
		s.close()
	return ip


def get_out_ip():
	my_ip = load(urlopen('http://httpbin.org/ip'))['origin']
	return my_ip


def tick():
	print('Tick! The time is: %s' % datetime.now())
	with open("foo.txt", 'a+') as file_to_read:
		lines = file_to_read.read()
		print(lines)
		file_to_read.write(get_out_ip())
		file_to_read.close()






def jobs():
	scheduler = BlockingScheduler()
	scheduler.add_job(tick, 'interval', seconds=3)
	print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

	try:
		scheduler.start()
	except (KeyboardInterrupt, SystemExit):
		pass
