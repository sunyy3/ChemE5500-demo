import matplotlib.pyplot as plt 

class Graph:

   def __init__(self,function=lambda x: x):
      self.function = function

   def plot(self, fptr):
      x = [i for i in range(0,100,1)]
      y = [self.function(x_i) for x_i in x]
      #print(x)
      #print(y)
      plt.clf()
      plt.plot(x,y)
      plt.savefig(fptr)
      plt.show()