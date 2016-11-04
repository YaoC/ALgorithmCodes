#coding:utf-8
'''
0-1背包问题
输入：
  物品价值向量 v
  物品重量向量 w
  背包最大重量限制 b
输出：
  在sum(w_i)<=b的条件下
  使得sum(v_i)最大的物品选择向量knapsack
  例：knapsack=[1,0,0,1,1],
    1：放入背包
    0：不放入背包
'''
def knapsack_r(v,w,b,knapsack):
  '''
  递归实现：
    穷举所有可能的装包情况取最大值
    递归考虑每一个物品装还是不装的情况
    递推关系：
    F[i,j] = max(F[i-1,j],F[i-1,j-w[j]]+v[i])
    F[i,j]: 背包重量限制为j时，只考虑前i个物品时可装包的最大价值
    显然有F[0,j]=0
  '''
  if v==[]:
    return 0
  idx = len(v)-1
  #默认不装入第idx个背包
  #第idx个背包可能因为之前的某次递归被置为了1
  #需要将其置为0
  knapsack[idx] = 0
  if b<w[-1]:
    return knapsack_r(v[:-1],w[:-1],b,knapsack)
  t1 = knapsack_r(v[:-1],w[:-1],b,knapsack)
  t2 = knapsack_r(v[:-1],w[:-1],b-w[-1],knapsack)+v[-1]
  if t2<t1:
    return t1
  #装入第idx个背包
  knapsack[idx] = 1
  return t2

def test_knapsack_r():
  v = [1,3,5,9]
  w = [2,3,4,7]
  b = 10
  knapsack = [0]*len(v)
  maxValue = knapsack_r(v,w,b,knapsack)
  print "knapsack_r:\nknapsack=%s\nmax value=%d"%(knapsack,maxValue)

import numpy as np 
def knapsack_dp(v,w,b):
  '''
  动态规划实现：
    递归中存在一些状态被重复计算
    将这些状态对应的最大价值保存起来
    利用递推关系：
      F[i,j] = max(F[i-1,j],F[i-1,j-w[j]]+v[i])
    从F[0,0] 递推计算至F[n][b]
    标记矩阵I中I[i,j]记录只考虑前i个物品，当背包重量限制为j+1时
    装入的物品的下标+1
  '''
  n = len(v)
  F = np.zeros([n+1,b])
  I = np.zeros([n+1,b])
  #只使用第1个物品
  for j in xrange(b):
    F[1,j] = (j+1)/w[0]*v[0]
    I[1,j] = bool((j+1)/w[0])
  #递推计算F[i,j]
  for i in xrange(2,n+1):     
    for j in xrange(b):
      if w[i-1] > j+1 or F[i,j-w[i-1]]+v[i-1]<F[i-i,j]:
        F[i,j] = F[i-1,j] 
        I[i,j] = I[i-1,j]
      else:
        F[i,j] = F[i,j-w[i-1]]+v[i-1]
        I[i,j] = i
  maxValue = F[n,b-1]
  knapsack = [0]*n
  minWeight = min(w)
  nowWeight = b
  k = n
  #回溯标记矩阵得到物品选择向量
  while(minWeight<nowWeight):
    idx = int(I[k,nowWeight-1]-1)
    knapsack[idx] = 1
    nowWeight -= w[idx]
    del w[idx]
    minWeight = min(w)
  return knapsack,maxValue

def test_knapsack_dp():
  v = [1,3,5,9]
  w = [2,3,4,7]
  b = 10
  ans = knapsack_dp(v,w,b)
  print "knapsack_dp:\nknapsack=%s\nmax value=%d"%ans

'''
背包问题扩展：
  增加物品的体积向量c
  体积约束 V
'''
def knapsack1_dp(v,w,b,c,V):
  '''
  递推关系：
  F[i,j,k] = max(F[i-1,j,k],F[i-1,j-w[j],k-c[j]]+v[i])
  '''
  n = len(v)
  F = np.zeros([n+1,b,V])
  I = np.zeros([n+1,b,V])
  #只使用第1个物品
  for j in xrange(b):
    for k in xrange(V):
      F[1,j,k] = min((j+1)/w[0],(k+1)/c[0])*v[0]
      I[1,j,k] = bool(F[1,j,k])
  #递推计算F[i,j,k]
  for i in xrange(2,n+1):     
    for j in xrange(b):
      for k in xrange(V):
        if w[i-1] > j+1 or c[i-1] > k+1 or F[i,j-w[i-1],k-c[i-1]]+v[i-1]<F[i-i,j,k]:
          F[i,j,k] = F[i-1,j,k] 
          I[i,j,k] = I[i-1,j,k]
        else:
          F[i,j,k] = F[i,j-w[i-1],k-c[i-1]]+v[i-1]
          I[i,j,k] = i
  maxValue = F[n,b-1,V-1]
  knapsack = [0]*n
  minWeight = min(w)
  minVolume = min(c)
  nowWeight = b
  nowVolume = V
  k = n   
  #回溯标记矩阵得到物品选择向量
  while(minWeight<nowWeight and minVolume<nowVolume):
    idx = int(I[k,nowWeight-1,nowVolume-1]-1)
    knapsack[idx] = 1
    nowWeight -= w[idx]
    nowVolume -= c[idx]
    del w[idx]
    del c[idx]
    minWeight = min(w)
    minVolume = min(c)
  return knapsack,maxValue

def test_knapsack1_dp():
  v = [1,3,5,9]
  w = [2,3,4,7]
  c = [1,3,1,3]
  b = 10
  V = 5
  ans = knapsack1_dp(v,w,b,c,V)
  print "knapsack1_dp:\nknapsack=%s\nmax value=%d"%ans

if __name__ == '__main__':
  test_knapsack_r()
  test_knapsack_dp()
  test_knapsack1_dp()