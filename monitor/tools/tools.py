import socket
from json import load
from urllib.request import urlopen


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
