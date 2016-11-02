
def minWeight(value,weight,totalValue):
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

if __name__ == '__main__':
	test_minWeight()