import math
import re

def mean(X):
	if X is None or len(X) == 0:
		return 0
	sum = 0.0
	for x in X:
		sum += x 
	return sum / len(X)

def std(X):
	if X is None or len(X) <= 1:
		return 0
	sub = 0
	m = mean(X)
	for x in X:
		sub = (x-m)**2
	div = sub / (len(X)-1)
	return math.sqrt(div)

def argmax(X):
	max_value = X[0]
	max_index = 0
	for i in range(1, len(X)):
		if X[i] > max_value:
			max_value = X[i]
			max_index = i
	return max_index

def argmin(X):
	min_value = X[0]
	min_index = 0
	for i in range(1, len(X)):
		if X[i] < min_value:
			min_value = X[i]
			min_index = i
	return min_index

def str_to_num(X):
	floats = []
	for x in X:
		try:
			floats.append(float(x))
		except ValueError:
			print x, "not a number!"
			exit()
	return floats


def main():
	input_nums = raw_input("Give me some comma separated numbers, bro.\n")
	X = re.split(',', input_nums.replace(" ", ""))
	X = str_to_num(X)

	for i in range(2):
		max_i = argmax(X)
		del(X[max_i])
		min_i = argmin(X)
		del(X[min_i])
	print std(X)

if __name__ == "__main__":
	main()