##problem is to find all occurences word in mat
def isValid(i,j,path,mat):
  return 0<=i<len(mat) and 0<=j<len(mat[0]) and mat[i][j] not in path

def dfs(mat,word,i,j,res,index=0,path=[]):
  if mat[i][j]!=word[index]: #skip
    return 
  path.append((i,j))
  ##get complete word 
  if index==len(word)-1:
    res.append(path.copy())
  else:
    for nr,nc in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
      if isValid(nr,nc,path,mat):
        dfs(mat,word,nr,nc,res,index+1,path)

if __name__ == '__main__':
 
    mat = [
        ['D', 'E', 'M', 'X', 'B'],
        ['A', 'O', 'E', 'P', 'E'],
        ['D', 'D', 'C', 'O', 'D'],
        ['E', 'B', 'E', 'D', 'S'],
        ['C', 'P', 'Y', 'E', 'N']
    ]
    m,n =len(mat),len(mat[0])
    word = 'CODE'
  
    res=[]
    for i in range(m):
      for j in range(n):
        dfs(mat, word, i,j, res)
    print(res)
    
 
