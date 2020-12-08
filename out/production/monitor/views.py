from django.http import HttpResponse
from django.shortcuts import render
import socket
import time
def hello(request):
	return HttpResponse("Hello world ! Index")

def helloWorld(request):
	"""context = {}
	context['hello'] = 'Hello World! 干饭人'
	localtime = time.asctime( time.localtime(time.time()) )
	context['dateStr'] = localtime
	context['views_list'] = ["菜鸟教程1","菜鸟教程2","菜鸟教程3"]
	return render(request, 'HelloWorld.html', context)"""

	"""views_dict = {"name":"菜鸟教程"}
	return render(request, 'HelloWorld.html', {'views_dict':views_dict})"""

	views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
	return render(request, "HelloWorld.html", {"views_str": views_str})

def ipMonitor(request):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	s.getsockname()[0]

	ip_adress = {"ip":ip,"myaddr":myaddr}

	return render(request, "IpMonitor.html.html", {"ip_adress": ip_adress})


