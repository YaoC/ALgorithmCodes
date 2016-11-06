#coding:utf-8
"""
问题：
	用多边形顶点的逆时针序列表示凸多边形，
	即P={v0,v1,…,vn-1}表示具有n条边的凸多边形。
	给定凸多边形P，以及定义在由多边形的边和弦组成的三角形上的权函数w。
	要求确定该凸多边形的三角剖分，
	使得即该三角剖分中诸三角形上权之和为最小。
"""
import sys
import numpy as np

def minWeight(G,n):
	M = np.zeros([n,n])
	S = np.zeros([n,n])
	for r in xrange(2,n):
		for i in xrange(1,n-r+1):
			j = i+r-1
			minW = sys.maxint
			for k in xrange(i,j):
				M[i,j] = M[i,k] + M[k+1,j] + G[i-1,k]+G[k,j]+G[j,i-1]
				if M[i,j]<minW:
					minW = M[i,j]
					S[i,j] = k
			M[i,j] = minW
	back_trace(S,1,n-1)
	print "最小权值：%d"%M[1,-1]

def back_trace(S,a,b):
	if a!=b:
		back_trace(S,a,S[a,b])
		back_trace(S,S[a,b]+1,b)
		print "最优三角划分： V%d V%d V%d"%(a-1,S[a,b],b)

def test_minWeight():
	n = 6
	G = np.array([
		[0,2,2,3,1,4],
		[2,0,1,5,2,3],
		[2,1,0,2,1,4],
		[3,5,2,0,6,2],
		[1,2,1,6,0,1],
		[4,3,4,2,1,0]])
	minWeight(G,n)

if __name__ == '__main__':
	test_minWeight()

