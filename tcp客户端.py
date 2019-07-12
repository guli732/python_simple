import socket


def main():
	tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	desk_ip = input("请输入服务器的ip地址:")
	desk_port = int(input("请输入服务器的端口号:"))
	tcp_client_socket.connect((desk_ip, desk_port))
	while True:
		send_data = input("请输入你的请求(输入q退出):")
		if send_data == 'q':
			break
		else:
			tcp_client_socket.send(send_data.encode('utf-8'))
			recv_data = tcp_client_socket.recv(1024)
			print("来自客户端的回应:{}".format(recv_data.decode('utf-8')))
	tcp_client_socket.close()


if __name__ == '__main__':
	main()