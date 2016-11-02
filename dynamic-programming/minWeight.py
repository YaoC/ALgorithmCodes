import sys
count = 0

def minWeight(value,weight,totalValue):
	global count 
	count += 1
	if totalValue == 0:
		return 0
	n = len(value)
	weights = []
	for i in xrange(n):
		if value[i] <= totalValue:
			weights.append(weight[i]+minWeight(value,weight,totalValue-value[i]))
	return min(weights)	
	
def test_minWeight():
	v = (1,4,6,8)
	w = (1,2,4,6)
	y = 12
	print minWeight(v,w,y)
	print count

def minWeightDp(value,weight,totalValue):
	coins = zip(value,weight)
	minWeight = [0]
	n = len(coins)
	plan = [[]]
	for t in xrange(1,totalValue+1):
		weights = []
		for coin in coins:
			if coin[0] <= t:
				weights.append(minWeight[t-coin[0]]+coin[1])
			else:
				weights.append(sys.maxint)
		minW = min(weights)
		idx = weights.index(minW)
		plan.append(plan[t-coins[idx][0]]+[coins[idx][0]])
		minWeight.append(minW)

		
	return plan[totalValue],minWeight[totalValue]

def test_minWeightDp():
	v = (1,4,6,8)
	w = (1,2,4,6)
	y = 12
	print minWeightDp(v,w,y)


if __name__ == '__main__':
	test_minWeightDp()