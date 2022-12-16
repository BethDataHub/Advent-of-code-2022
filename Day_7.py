from io import StringIO
import pandas as pd

lines = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

lines = StringIO(lines.replace("$ ",""))

df = pd.read_csv(lines, sep=" ", names = ["other","directory"])
df = df[df.other != "ls"].reset_index(drop=True)

df["type"] = df["other"].apply(lambda x: "file" if x.isnumeric() else "directory")

for i, row in df.iterrows():
    if row["other"] == "cd" and row["directory"] == "/":
        level = 0
        parent = row["directory"]
    
    elif row["other"] == "cd" and row["directory"] == "..":
        level +=-1

    elif row["other"] == "cd":
        level+=1
        parent = row["directory"]
    
    df.at[i,'level'] = level
    df.at[i,'parent'] = parent



directories = df[df.other == "dir"]

df[df.directory]

print(directories)

