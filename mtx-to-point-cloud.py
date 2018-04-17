import csv
from igraph import Graph
from sys import argv
from os import path
from scipy.io import mmread

file_name = None

try:
    file_name, file_extension = path.splitext(argv[1])
except IndexError:
    print('Invalid filename. Usage:\npython mtx-to-point-cloud.py filename')
    exit(1)

matrix = mmread(file_name)
graph = Graph.Adjacency(list(matrix.toarray()))
layout = graph.layout_kamada_kawai_3d()

with open('%s.txt' % file_name, 'w') as f:
    csv.writer(f, delimiter=' ').writerows(layout.coords)
