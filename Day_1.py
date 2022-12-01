from aocd import get_data
import pandas as pd
import os
from io import StringIO
import utils.Examples as exm
from tests.test import test_before_submit

AOC_SESSION = os.getenv("AOC_SESSION") 
day=1
year=2022

def get_challenge_data(run_type):
    example_data = exm.examples[f"Day_{day}"]["example"].replace("\n\n","\n;\n")
    challenge_data = get_data(day=day, year=year).replace("\n\n","\n;\n")

    if run_type == "test":
        data = example_data
    else:
        data = challenge_data

    df = pd.read_csv(StringIO(data),names=["Calories"])

    return df

def get_calories_by_elf(df):
    elves = df.index[df["Calories"] == ";"].tolist()
    elves.append(len(df))

    total_calories=[]
    i = 0
    for elf in elves:
        elf_calories = pd.DataFrame(df[i:elf]).astype(int).sum()
        i=elf+1
        total_calories.append(elf_calories[0])

    return total_calories

def main():
   

    test_total_calories = sorted(get_calories_by_elf(get_challenge_data("test")), reverse=True)
    test_part_one = test_total_calories[0]
    test_part_two = sum(test_total_calories[0:3])

    total_calories = sorted(get_calories_by_elf(get_challenge_data("")), reverse=True)
    part_one = total_calories[0]
    part_two = sum(total_calories[0:3])

    if part_two and part_one:
        test_before_submit(day, year, part="b", test_answer=test_part_two, answer=part_two)
    elif part_one:
        test_before_submit(day, year, part="a", test_answer= test_part_one, answer=part_one)
    else:
        raise ValueError("Missing Answers")


if __name__ == "__main__":
    main()