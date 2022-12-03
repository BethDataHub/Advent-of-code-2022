import pandas as pd
from aocd import get_data
import utils.Examples as exm
from utils.test import test_before_submit
from io import StringIO
import os

AOC_SESSION = 
day=3
year=2022

lower = 96
upper = 38



def get_challenge_data(run_type):
    example_data = exm.examples[f"Day_{day}"]["example"]
    challenge_data = get_data(day=day, year=year)

    if run_type == "test":
        data = example_data
    else:
        data = challenge_data

    df = pd.read_csv(StringIO(data),names=["Backpack Contents"])

    return df

data = get_challenge_data("test")

data["first"] = data["Backpack Contents"].apply(lambda x: x[:int(len(x)/2)])
data["second"] = data["Backpack Contents"].apply(lambda x: x[int(len(x)/2):])
data["return"] = data.apply(lambda x: set(x["first"]).intersection(x["second"]), axis=1).str.join('')
data["priority"] = data["return"].apply(lambda x: ord(x)-upper if x.isupper() else ord(x)-lower)

print(data["priority"].sum())
