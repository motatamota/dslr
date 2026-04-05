import matplotlib.pyplot  as maplot
import pandas as pd
import sys

args = sys.argv
if len(args) != 2:
	print("Argument error")
	exit()

df = pd.read_csv(args[1])

gryffindor = df[df["Hogwarts House"] == "Gryffindor"]
slytherin  = df[df["Hogwarts House"] == "Slytherin"]
ravenclaw  = df[df["Hogwarts House"] == "Ravenclaw"]
hufflepuff = df[df["Hogwarts House"] == "Hufflepuff"]

courses = df.select_dtypes(exclude='object').columns.tolist()

fig, axes = maplot.subplots(4, 4, figsize=(16, 12))
axes = axes.flatten()

for i, course in enumerate(courses):
	if i == 0:
		continue
	axes[i - 1].hist(gryffindor[course].dropna(), alpha=0.5, label="Gryffindor")
	axes[i - 1].hist(slytherin[course].dropna(),  alpha=0.5, label="Slytherin")
	axes[i - 1].hist(ravenclaw[course].dropna(),  alpha=0.5, label="Ravenclaw")
	axes[i - 1].hist(hufflepuff[course].dropna(), alpha=0.5, label="Hufflepuff")
	axes[i - 1].set_title(course, fontsize=8)
	axes[i - 1].legend(fontsize=5)

for j in range(len(courses) - 1, len(axes)):
	axes[j].set_visible(False)

maplot.tight_layout()
maplot.show()
