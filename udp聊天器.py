import socket


def send_msg(udp_socket, dest_ip, dest_port):
	send_date = input("请输入要发送的数据:")
	udp_socket.sendto(send_date.encode('utf-8'), (dest_ip, dest_port))


def recv_msg(udp_socket):
	recv_date = udp_socket.recvfrom(1024)
	print("接收到来自{}的信息[{}]".format(recv_date[1], recv_date[0].decode('utf-8')))


def main():
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	my_port = int(input("请绑定自己的端口号:"))
	udp_socket.bind(('', my_port))
	dest_ip = input("请输入对方的ip地址:")
	dest_port = int(input("请输入对方的端口号:"))
	while True:
		print("-----udp聊天器-----")
		print("1.收发信息")
		print("0.退出系统")
		choice = input("请选择功能:")
		if choice == '1':
			send_msg(udp_socket, dest_ip, dest_port)
			recv_msg(udp_socket)
		elif choice == '0':
			break
		else:
			print("输入错误，清重新输入!")


if __name__ == '__main__':
	main()