import matplotlib.pyplot as plt
import pandas as pd
import sys

def main():
	args = sys.argv
	if len(args) != 2:
		print("Argument error")
		return
	df = pd.read_csv(args[1])

	plt.scatter(df["Astronomy"], df["Defense Against the Dark Arts"], alpha=0.5)
	plt.xlabel("Astronomy")
	plt.ylabel("Defense Against the Dark Arts")
	plt.show()

if __name__ == '__main__':
	main()
