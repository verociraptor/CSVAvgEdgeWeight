import sys
import csv

class CSVAvgEdgeWeightPlugin:
	def input(self, filename):
		self.myfile = filename


	def run(self):
		f = open(self.myfile, 'r')
		csv_f = csv.reader(f)
		next(csv_f)
		self.edge_weight = []
		
		for row in csv_f:
			self.edge_weight.append(row[1:])
		
	
	def output(self, filename):
		total_weights = 0
		total_edges = 0
		for row in self.edge_weight:
			for i in range(0, len(row)):
				if(float(row[i]) > 0):
					total_weights += float(row[i])
					total_edges += 1
		
		average = (total_weights / total_edges)

		print("Average edge weight: ", average)
