# -*- coding: utf-8 -*- 
'''
给定n种币值[x1,x2,...xn]和总钱数M
每种币值只能使用一次
设计算法求对于M的一种找零方式
'''
count = 0

def smallChange(X,M):
	global count
	count += 1
	print X,M
	if M==0:
		return True
	if M<0:
		return False
	if X==[] and M>0:
		return False
	current = X.pop()
	if smallChange(X[:],M-current):
		print "%d "%current,
		return True
	return smallChange(X[:],M)
	

def test_smallChange():
	X = [1,5,20,50,100,2,10]
	M = 58
	print "\n%s"%smallChange(X,M)
	print count

def smallChangeDp(X,M):
	success = set([])
	while X!=[]:
		t = X.pop()
		success |= set([x+t for x in success])
		success.add(t)
		print success
		if M in success:
			return True
	return False

def test_smallChangeDp():
	X = [1,5,20,50,100,2,10]
	M = 58
	print smallChangeDp(X,M)

def smallChangeDp2(X,M):
	table = [0 for i in xrange(M+1)]
	for x in X:
		if x<=M:
			temp = []
			for i in xrange(1,M-x+1):
				if table[i] == 1:
					temp.append(i+x)
			table[x] = 1
			for t in temp:
				table[t] = 1 
	return bool(table[M])

def test_smallChangeDp2():
	X = [1,5,20,50,100,2,10]
	M = 58
	print smallChangeDp2(X,M)

if __name__ == '__main__':
	test_smallChangeDp2()

