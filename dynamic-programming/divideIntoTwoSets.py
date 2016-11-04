def devideIntoTwoSets(A):
	S = sum(A)
	if S % 2 == 1:
		return False
	s1 = S/2
	s2 = S/2
	A.sort()
	while(A):
		t = A.pop()
		if t>max(s1,s2):
			return False
		if(s1>s2):
			s1 -= t
		else:
			s2 -= t
	if(s1==s2):
		return True
	return False

def test_devideIntoTwoSets():
	A = [7,23,26,27,29]
	print devideIntoTwoSets(A)

import smallChange as sc 
def devideIntoTwoSetsDp(A):
	S = sum(A)
	if S % 2 == 1:
		return False
	return sc.smallChangeDp2(A,S/2)

def test_devideIntoTwoSetsDp():
	A = [7,23,26,27,29]
	print devideIntoTwoSetsDp(A)

if __name__ == '__main__':
	test_devideIntoTwoSetsDp()
