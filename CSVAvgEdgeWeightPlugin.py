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
		total = 0
		elements = 0
		for row in self.edge_weight:
			for i in range(0, len(row)):
				total += float(row[i])
				elements += 1
		
		average = (total / elements)

		print "Average edge weight: ", average
