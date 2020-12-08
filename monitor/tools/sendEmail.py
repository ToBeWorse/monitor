import smtplib


def sendEmail(ip_address):
	# 网易163邮箱
	HOST = 'smtp.163.com'
	# 2> 配置服务的端口，默认的邮件端口是25.
	PORT = '25'
	# 3> 指定发件人和收件人。
	FROM = 'worsehost@163.com'
	TO = '1170569551@qq.com'
	# 4> 邮件标题
	SUBJECT = 'IP地址'
	# 5> 邮件内容
	CONTENT = '当前服务器地址' + ip_address
	# 创建邮件发送对象
	# 普通的邮件发送形式
	smtp_obj = smtplib.SMTP()
	# 数据在传输过程中会被加密。
	# smtp_obj = smtplib.SMTP_SSL()
	# 需要进行发件人的认证，授权。
	# smtp_obj就是一个第三方客户端对象
	smtp_obj.connect(host=HOST, port=PORT)
	# 如果使用第三方客户端登录，要求使用授权码，不能使用真实密码，防止密码泄露。
	res = smtp_obj.login(user=FROM, password='XQHGTZSIHPSHWHTD')
	print('登录结果：', res)
	# 发送邮件
	msg = '\n'.join(['From: {}'.format(FROM), 'To: {}'.format(TO), 'Subject: {}'.format(SUBJECT), '', CONTENT])
	smtp_obj.sendmail(from_addr=FROM, to_addrs=TO, msg=msg.encode('utf-8'))
