n=input()
l=[0 for i in xrange(n+1)]

for i in xrange (2,n+1):
  if l[i]==0:
    for j in xrange (2*i,n+1,i):
      l[j]=1
      
g=input()
if l[g]==1:
  print "Not prime"
else:
  print "Prime"
