
def valid(x,y,path,mat):
  return (0 <= x < len(mat)) and (0 <= y < len(mat[0])) and (x, y) not in path

def searchMatrix(mat, word):
  if not mat or not word:
    return res
  
  def dfs(i,j,mat,path,index,word):
    r=[-1,0,1,-1, 0,1,1,1]
    c=[-1,1,0, 0,-1,0,0,1]

    if index==len(word):
      res.add(tuple(path))
      return 
    if mat[i][j] !=word[index]:
      return 
    
    path.append((i,j))
    for k in range(len(r)):
      if valid(i+r[k],j+c[k],path,mat):
        dfs(i+r[k],j+c[k],mat,path,index+1,word)
    path.pop()

  m,n=len(mat),len(mat[0])
  path=[]
  res=set()
  for i in range(m):
    for j in range(n):
      dfs(i,j,mat,path,0,word)
  
  return res
if __name__=='__main__':
  mat = [
        ['D', 'E', 'M', 'X', 'B'],
        ['A', 'O', 'E', 'P', 'E'],
        ['D', 'D', 'C', 'O', 'D'],
        ['E', 'B', 'E', 'D', 'S'],
        ['C', 'P', 'Y', 'E', 'N']
    ]
  word = 'CODE'
 ret =searchMatrix(mat, word)
