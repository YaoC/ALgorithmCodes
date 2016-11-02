#-*-coding:utf-8-*- #
import numpy as np

# maxSubStrLength: str中满足最大值小于last的最大单调递增子串的长度
def maxSubStrLength(str,last):
	if(str==[]):
		return 0 
	if(str[-1]>=last):
		return maxSubStrLength(str[:-1],last)
	return max(1+maxSubStrLength(str[:-1],str[-1]),
		maxSubStrLength(str[:-1],last))



def maxSubString(str):
	length = len(str)
	maxSubStr = np.zeros([length,length])
	for i in xrange(1,length):
		for j in xrange(i,length):
			if(str[j]<=str[i-1]):
				maxSubStr[i][j] = maxSubStr[i-1][j]
			else:
				maxSubStr[i][j] = max(maxSubStr[i-1][i-1]+1,maxSubStr[i-1][j])
	print maxSubStr
	i=length-1
	j=i
	ans = []
	while (i!=0):
		if(maxSubStr[i][j] == maxSubStr[i-1][i-1]+1):
			ans.append(j)
			i -= 1
			j = i
		else:
			i -= 1
	ans.append(j)
	ans.reverse()
	return ans


if __name__ == '__main__':
	s = [2,8,4,-4,5,9,11]
	index = maxSubString(s)
	print [s[i] for i in index]