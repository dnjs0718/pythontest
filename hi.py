'''
import sys
for i in range(1,int(sys.stdin.readline())+1):
    print('*' * i)
'''
import sys
total = 0
hi=[]
for i in range(int(sys.stdin.readline())):
    hi.append(int(sys.stdin.readline()))
for i in range(len(hi)-1):
    total+= hi[i]-1
total += hi[-1]
print(total)
