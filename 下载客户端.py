import socket


def main():
	# 创建套接字
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 获取服务器ip、port
	desk_ip = input("服务器ip:")
	desk_port = int(input("服务器端口号:"))
	# 连接服务器
	tcp_socket.connect((desk_ip, desk_port))
	# 获取下载的文件的名字
	file_name = input("想要下载的文件名字:")
	# 将名字发送到服务器
	tcp_socket.send(file_name.encode('utf-8'))
	# 接收文件中的数据
	recv_data = tcp_socket.recv(1024)
	if recv_data:
		# 保存接收到的数据到一个文件中
		with open ("new_" + file_name, 'w') as f:
			f.write(recv_data.decode('utf-8'))
			print("文件下载成功!")
	else:
		print("文件下载失败！")
	# 关闭套接字
	tcp_socket.close()


if __name__ == '__main__':
	main()