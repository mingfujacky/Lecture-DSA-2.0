from pathlib import Path

class GraphMatrix:
  
  def read_file(self,file_name):
    with open(file_name, 'r') as f:
      self.n = int(f.readline())
      self.A = [[] for _ in range(self.n)]
      for i in range(self.n):
        self.A[i] = list(map(int,f.readline().split()))
  
  def print(self):	
    for i in range(self.n):
      for j in range(self.n):
        print(self.A[i][j], end = ' ')
      print()
    print()
  
if __name__ == '__main__':
  g = GraphMatrix()
  file_path = Path.cwd() / 'asset' / 'txt' / 'graph_matrix.txt'
  g.read_file(file_path)
  g.print()