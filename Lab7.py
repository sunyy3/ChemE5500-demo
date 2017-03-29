from graph import Graph
import math

f1 = lambda x: x**2
f2 = lambda x: math.sin(x)

g1 = Graph(f1)
g1.plot('demo1')

g2 = Graph(f2)
g2.plot('demo2')