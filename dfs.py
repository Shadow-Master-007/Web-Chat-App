n,m=map(int,raw_input().split())
global g,vis

g=[[] for i in xrange(n+1)]
vis=[0 for i in xrange(n+1)]

def dfs(s):
  print s
  vis[s]=1
  for i in xrange (len(g[s])):
    if vis[g[s][i]]==0:
      dfs(g[s][i])

for i in xrange (m):
  x,y=map(int,raw_input().split())
  g[x].append(y)
  g[y].append(x)

print "DFS pattern:"
for i in xrange (1,n+1):
  if vis[i]==0:
    dfs(i)
