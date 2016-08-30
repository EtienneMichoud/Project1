'''
6 digits
mult. by 2, 3, 4, 5, 6
'''

def areNumbersDigitsEquals(num1, num2):
	s1 = str(num1)
	s2 = str(num2)
	l1 = list(s1)
	l2 = list(s2)
	l1 = [int(i) for i in l1]
	l2 = [int(i) for i in l2]
	#l1.sort()
	#l2.sort()
	x = set(l1) & set(l2)
	#print(l1)
	#print(l2)
	#print(x)
	if(len(x)==len(l1) and len(x)==len(l2)):
		return True
	else:
		return False

if __name__ == "__main__":
	for x in range(100000,166666):
		x2 = 2*x
		x3 = 3*x
		x4 = 4*x
		x5 = 5*x
		x6 = 6*x
		b2 = areNumbersDigitsEquals(x, x2)
		b3 = areNumbersDigitsEquals(x, x3)
		b4 = areNumbersDigitsEquals(x, x4)
		b5 = areNumbersDigitsEquals(x, x5)
		b6 = areNumbersDigitsEquals(x, x6)
		if(b2 and b3 and b4 and b5 and b6):
			print(x)
			break
		else:
			continue

			
	'''
	x1 = areNumbersDigitsEquals(123456, 789456)
	print(x1)
	x2 = areNumbersDigitsEquals(123, 123)
	print(x2)
	x3 = areNumbersDigitsEquals(123, 124)
	print(x3)
	'''