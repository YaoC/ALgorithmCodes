import numpy as np
def bandWidth(T,k,S):
	if T == [] :
		return 0
	idx = len(T)-1
	S[idx] = 0
	if T[-1]>k:
		return bandWidth(T[:-1],k,S)
	a = bandWidth(T[:-1],k,S)
	b = bandWidth(T[:-1],k-T[-1],S)+T[-1]
	if a>b:
		return a
	S[idx] = 1
	return b

def test_bandWidth():
	T = [5,11,8,9]
	k = 15
	S = np.zeros(len(T))
	print bandWidth(T,k,S)
	print S

if __name__ == '__main__':
	test_bandWidth()