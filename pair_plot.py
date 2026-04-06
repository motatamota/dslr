import matplotlib.pyplot as plt
import pandas as pd
import sys

def main():
	if len(sys.argv) < 2:
		print("Argument error")
		return
	df = pd.read_csv(sys.argv[1])

	houses = {
		"Gryffindor": "red",
		"Slytherin": "green",
		"Ravenclaw": "blue",
		"Hufflepuff": "yellow",
	}

	courses = df.select_dtypes(exclude='object').columns.tolist()
	courses.remove("Index")
	n = len(courses)

	fig, axes = plt.subplots(n, n, figsize=(14, 10))

	for i, c1 in enumerate(courses):
		for j, c2 in enumerate(courses):
			ax = axes[i][j]
			if i == j:
				for house, color in houses.items():
					data = df[df["Hogwarts House"] == house][c1].dropna()
					ax.hist(data, alpha=0.5, color=color, label=house)
			else:
				for house, color in houses.items():
					data = df[df["Hogwarts House"] == house][[c1, c2]].dropna()
					ax.scatter(data[c2], data[c1], alpha=0.3, color=color, s=2, label=house)
			if i == n - 1:
				ax.set_xlabel(c2, fontsize=5)
			else:
				ax.set_xticks([])
			if j == 0:
				ax.set_ylabel(c1, fontsize=5)
			else:
				ax.set_yticks([])

	handles, labels = axes[0][0].get_legend_handles_labels()
	fig.legend(handles, labels, loc='upper right', fontsize=8)
	plt.tight_layout()
	plt.show()

if __name__ == '__main__':
	main()
