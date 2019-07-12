import socket


def send_file(new_socket, ):
	# 接受客户端发送过来的要下载的文件名
	recv_data = new_socket.recv(1024).decode('utf-8')
	print("客户端要下载的文件是:{}".format(recv_data))
	# 发送文件给客户端
	file = None
	try:
		f = open(recv_data, 'r')
		file = f.read()
		f.close()
	except Exception as ret:
		print("没有要下载的文件!")
	if file:
		new_socket.send(file.encode('utf-8'))
		print("文件发送成功！")


def main():
	# 创建套接字
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 绑定端口
	tcp_socket.bind(('', 5522))
	# listen
	tcp_socket.listen(128)
	# accept
	new_socket, client_addr = tcp_socket.accept()
	print("客户端{}连接成功！".format(client_addr))
	send_file(new_socket)
	# 关闭套接字
	new_socket.close()
	tcp_socket.close()


if __name__ == '__main__':
	main()