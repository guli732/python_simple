import time


def main():
	count = 50
	start = time.perf_counter()
	for i in range(count + 1):
		a = '#' * i
		b = ' ' * (count - i)
		c = (i/count) * 100
		dur = time.perf_counter() - start
		print("\r{:.1f}%[{}{}]{:.2f}s".format(c, a, b, dur), end='')
		time.sleep(0.4)


if __name__ == '__main__':
	main()