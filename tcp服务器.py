import socket


def main():
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp_server_socket.bind(('', 5252))
	tcp_server_socket.listen(128)
	print("等待客户端的连接...")
	while True:
		new_socket, client_addr = tcp_server_socket.accept()
		print("客户端{}连接成功！".format(client_addr))
		while True:
			recv_data = new_socket.recv(1024)
			if recv_data:
				print("接收到请求:", recv_data.decode('utf-8'))
				new_socket.send("收到了!".encode('utf-8'))
			else:
				print("客户端{}已断开连接!".format(client_addr))
				break
		new_socket.close()
	tcp_server_socket.close()


if __name__ == '__main__':
	main()