from pathlib import Path

class GraphList:
    def __init__(self):
        self.n = 0  # number of vertices
        self.e = 0  # number of edges
        self.L = {} # adjacency list

    def read_file(self,file_name):
        with open(file_name, 'r') as f:
            self.n, self.e = map(int, f.readline().split())
            for k in range(self.n):
                self.L[k] = []
            for _ in range(self.e):
                i, j = map(int,f.readline().split())
                self.L[i].append(j)

    def print(self):	
        for i in range(self.n):
          print(f"{i}: {self.L[i]}")
        print()
  

if __name__ == '__main__':
  g = GraphList()
  file_path = Path.cwd() / 'asset' / 'txt' / 'graph_list.txt'
  g.read_file(file_path)
  g.print()