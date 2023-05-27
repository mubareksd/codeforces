#!/usr/bin/env python3

if __name__ == "__main__":
	num = int(input())
	val = []
	while num > 0:
		a, b, c = map(int, input().split())
		lists = [a, b, c]
		lists.sort()
		val.append(lists[1])
		num -= 1

	for i in val:
		print(i)
