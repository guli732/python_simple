import socket


def main():
	# 创建一个udp套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	udp_socket.bind(('', 7890))
	while True:
		# 使用套接字收发数据
		send_date = input("请输入要发送的数据(输入‘exit’退出程序):")
		if send_date == 'exit':
			break
		else:
			udp_socket.sendto(send_date.encode('utf-8'), ('192.168.2.126', 2233))
	# 关闭套接字
	udp_socket.close()

if __name__ == '__main__':
	main()