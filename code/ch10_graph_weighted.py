from pathlib import Path

class WeightedGraphList:
    def __init__(self):
        self.n = 0  # number of vertices
        self.e = 0  # number of edges
        self.L = {} # adjacency list

    def read_file(self,file_name):
        with open(file_name, 'r') as f:
            self.n, self.e = map(int, f.readline().split())
            for n in range(self.n):
                self.L[n] = []
            for _ in range(self.e):
                i, j, k = map(int,f.readline().split())
                self.L[i].append((j, k))

    def print(self):	
        for i in range(self.n):
          print(f"{i}: {self.L[i]}")
        print()
  

if __name__ == '__main__':
  g = WeightedGraphList()
  file_path = Path.cwd() / 'asset' / 'txt' / 'weighted_graph_list.txt'
  g.read_file(file_path)
  g.print()