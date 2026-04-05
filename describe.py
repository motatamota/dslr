import pandas as pd
import math
import numpy
import sys

def main() :
	csv_data = pd.read_csv("datasets/dataset_train.csv")
	data_base = {}
	for col in csv_data:
		if csv_data[col].dtype == object:
			continue
		sum_data = 0
		values = []
		for value in csv_data[col]:
			if value != value:
				continue
			values.append(value)
			sum_data += value
		values.sort()

		# 25%
		index = (len(values) - 1) * 0.25
		low = int(index)
		fraction = index - low
		high = low + 1
		ql_data = values[low] * (1 - fraction) + values[high] * fraction

		# 50%
		index = (len(values) - 1) * 0.50
		low = int(index)
		fraction = index - low
		high = low + 1
		h_data = values[low] * (1 - fraction) + values[high] * fraction

		# 75%
		index = (len(values) - 1) * 0.75
		low = int(index)
		fraction = index - low
		high = low + 1
		qh_data = values[low] * (1 - fraction) + values[high] * fraction

		# Std
		mean = sum_data / len(values)
		std_sum = 0
		for x in values:
			std_sum += (x - mean) * (x - mean)
		std = math.sqrt(std_sum / (len(values) - 1))

		data_base[col] = {
			"Count" : len(values),
			"Mean" : mean,
			"Std" : std,
			"Min" : values[0],
			"25%" : ql_data,
			"50%" : h_data,
			"75%" : qh_data,
			"Max" : values[len(values) - 1]
		}

	option_name_size = 5
	col_sizes = {}
	for col in csv_data:
		if csv_data[col].dtype == object:
			continue
		col_sizes[col] = max(14, len(col) + 2)

	print(f"{'':<{option_name_size}}", end="")
	for col in csv_data:
		if csv_data[col].dtype == object:
			continue
		print(f"{col:>{col_sizes[col]}}", end="")
	print()

	for value in ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]:
		print(f"{value:<{option_name_size}}", end="")

		for col in csv_data:
			if csv_data[col].dtype == object:
				continue
			print(f"{data_base[col][value]:>{col_sizes[col]}.6f}", end="")
		print()



if __name__ == '__main__':
	main()
