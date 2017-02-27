def is_harshad(x):
	if not isinstance(x, (int,long)):
		return False 
	if x < 0:
		return False
	sum = 0
	num = x
	while num > 0:
		sum += num % 10
		num /= 10
	if x % sum == 0:
		return True 
	else:
		return False		

def is_div_by_product(x):
	prod = 1
	num = x
	while num > 0:
		prod *= num % 10
		num /= 10
	if prod == 0:
		return False
	if x % prod == 0:
		return True 
	else:
		return False
	
def main():
	for num in range(1,1000):
		if is_harshad(num):
			print num, "is Harshad. ",
			if is_div_by_product(num):
				print num, "is also divisable by the product of its digits."
			else:
				print
if __name__ == "__main__":
	main()
