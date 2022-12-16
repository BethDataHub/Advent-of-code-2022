from io import StringIO
import pandas as pd
from aocd import get_data, submit
import math

noop = 1
addx = 2

data = """addx 1
addx 4
noop
noop
noop
noop
addx 6
addx -1
noop
addx 5
noop
addx 5
noop
noop
noop
addx 1
addx 3
addx 1
addx 6
addx -1
noop
noop
noop
addx 7
noop
addx -39
noop
noop
noop
addx 7
addx 3
addx -2
addx 2
noop
addx 3
addx 2
addx 5
addx 2
addx -8
addx 13
noop
addx 3
addx -2
addx 2
addx 5
addx -31
addx 36
addx -2
addx -36
noop
noop
noop
addx 3
addx 5
addx 2
addx -7
addx 15
addx -5
addx 5
addx 2
addx 1
addx 4
noop
addx 3
noop
addx 2
addx -13
addx -16
addx 2
addx 35
addx -40
noop
noop
addx 7
noop
noop
noop
addx 5
noop
addx 5
addx 10
addx -10
noop
noop
noop
addx 3
noop
addx 16
addx -9
noop
noop
noop
addx 3
noop
addx 7
addx -32
addx 35
addx -38
addx 22
addx 10
addx -29
addx 2
noop
addx 3
addx 5
addx 2
addx 2
addx -12
addx 13
noop
noop
addx 7
addx 5
noop
noop
noop
addx 7
addx -6
addx 2
addx 5
addx -38
addx 1
noop
noop
addx 2
noop
addx 3
addx 5
noop
addx 4
addx -2
addx 5
addx 2
addx 1
noop
addx 4
addx 4
addx -14
addx 16
noop
addx -13
addx 18
addx -1
noop
noop
noop"""

example = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


lines = StringIO(example)
df = pd.read_csv(lines, sep = " ", names = ['instruction','number'])

x=1
a=1

for i, row in df.iterrows():
    if row["instruction"] == "addx":
        x+=row["number"]
    
    df.at[i,"X"] = x    
    
    a+= eval(row["instruction"])

    df.at[i,"cycle"] = a
    df.at[a,"use_this_number"] = x

df["index"]=df.index

pd.set_option('display.max_rows',None)

#df = df[df["use_this_number"].notnull()]

requested_cycles=[20,60,100,140,180,220]


output=[]

for i, row in df.iterrows():
    if row["index"] == 0:
        df.at[i, "use_this_number"] = 1
    
    elif math.isnan(row["use_this_number"]):
        df.at[i,"use_this_number"] = df["use_this_number"][i-1]


#for cycle in requested_cycles:
#    if cycle in df["index"]:
#        output.append(int(float(df.iloc[(df['index']-cycle).abs().argsort()[:1]]["use_this_number"].to_string(index=False)))*cycle)
#    else:    
#        output.append(int(float(df.iloc[(df['index']-cycle).abs().argsort()[1:2]]["use_this_number"].to_string(index=False)))*cycle)
#
#print(sum(output))

lines = StringIO(data)
df = pd.read_csv(lines, sep = " ", names = ['instruction','number'])

x=1
a=0

for i, row in df.iterrows():
    if row["instruction"] == "addx":
        x+=row["number"]
    
    df.at[i,"X"] = x    
    
    a+= eval(row["instruction"])

    df.at[i,"cycle"] = a
    df.at[a,"use_this_number"] = x

df["index"]=df.index

for i, row in df.iterrows():
    if row["index"] == 0:
        df.at[i, "use_this_number"] = 1
    
    elif math.isnan(row["use_this_number"]):
        df.at[i,"use_this_number"] = df["use_this_number"][i-1]

    if row["index"] != 0:
        try:
            df["index"][i-1]
        except:
            df.loc[i-1] = "","","","",df["use_this_number"][i-2],i-1

df = df.sort_index().reset_index(drop=True)

def get_sprite(df,start,end):
    new_sprite = []
    df = df.iloc[start:end]

    for cycle, row in df.iterrows():
        x = int(row["use_this_number"])
        sprite = list('........................................')
        sprite[x-1:x+2]="###"

        new_sprite.append(sprite[cycle%40])
    print("".join(new_sprite))



get_sprite(df,0,40)
get_sprite(df,40,80)
get_sprite(df,80,120)
get_sprite(df,120,160)
get_sprite(df,160,200)
get_sprite(df,200,240)