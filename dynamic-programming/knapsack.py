
loop = 0
num = 6
v = (1,3,5,9,3,5)
w = (11,3,4,7,3,3)
size = 10

def nowValue(id,now):
    global loop
    loop += 1
    print "calculate S[%d][%d]" %(id,now)
    if(id>=num):
        return 0
    if(now>size):
        return 0
    value = 0
    b = nowValue(id+1,now)
    if(now+w[id]>size):
        value = b
    else:
        a = nowValue(id+1,now+w[id])+v[id]
        if(a>b):
            value =  a
            print "put %d into bag" %id
        else:
            value = b
    print "value is %d" %value
    return value

if __name__ == '__main__':
    print nowValue(0,0)
    print "loop: %d" %loop