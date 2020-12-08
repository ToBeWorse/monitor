import socket
import requests
import re


def get_host_ip():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(('8.8.8.8', 80))
		ip = s.getsockname()[0]
	finally:
		s.close()
	return ip

def get_out_ip():
	html_text = requests.get("https://ip.cn/").text
	print(html_text)
	# （1）正则匹配方式1
	ip_text = re.search(u"<p>您现在的 IP：<code>(.*?)</code></p>", html_text)
	print
	ip_text.group(1)