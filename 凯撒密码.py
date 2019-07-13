s = input("请输入原文:")
c = ''
for i in s:
	if 'a' <= i <= 'z':
		c += chr((ord(i) - ord('a') + 3) % 26 + ord('a'))
	elif 'A' <= i <= 'Z':
		c += chr((ord(i) - ord('A') + 3) % 26 + ord('A'))
	else:
		c += i
print("密文为:" + c)