import socket


def main():
	# 创建套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	udp_socket.bind(('', 7788))
	while True:
		# 使用套接字收发数据
		recv = udp_socket.recvfrom(1024)
		print("接收到来自[{}]的信息[{}]".format(recv[1], recv[0].decode('utf-8')))
	# 关闭套接字
	udp_socket.close()

if __name__ == '__main__':
	main()