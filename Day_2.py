from aocd import get_data
import pandas as pd
import os
import utils.Examples as exm
from tests.test import test_before_submit
from io import StringIO
from tests.test import test_before_submit

AOC_SESSION = os.getenv("AOC_SESSION") 
day=2
year=2022

shapes = {
    "A":{
        "points":1, 
        "loses_against":"B",
        "wins_against":"C"
        },
    "B":{
        "points":2, 
        "loses_against":"C",
        "wins_against":"A"
        },
    "C":{
        "points":3, 
        "loses_against":"A",
        "wins_against":"B"
        }
}

my_move={
    "X":{"part_one":"A","part_two":"loss"},
    "Y":{"part_one":"B","part_two":"draw"},
    "Z":{"part_one":"C","part_two":"win"}
}

loss=0
draw=3
win=6


def get_challenge_data(run_type):
    example_data = exm.examples[f"Day_{day}"]['example']
    actual_data = get_data(day=day, year=year)

    if run_type == "example":
        data = example_data
    else:
        data = actual_data

    df = pd.read_csv(StringIO(data),names=["Opponent","Moves"],sep=" ")

    return df

def get_score(df):

    for i, row in df.iterrows():
        p1_points = shapes.get(my_move.get(row["Moves"])["part_one"])["points"]
        loses_against = shapes.get(my_move.get(row["Moves"])["part_one"])["loses_against"]

        if row["Opponent"] == loses_against:
            p1_outcome = loss
        elif row["Opponent"] == my_move.get(row["Moves"])["part_one"]:
            p1_outcome = draw
        else:
            p1_outcome = win

        if my_move.get(row["Moves"])["part_two"] == "win":
            challenge_move = shapes.get(row["Opponent"])["loses_against"]
            p2_outcome = win
        elif my_move.get(row["Moves"])["part_two"] == "loss":
            challenge_move = shapes.get(row["Opponent"])["wins_against"]
            p2_outcome = loss
        else:
            challenge_move = row["Opponent"]
            p2_outcome = draw

        p2_points = shapes.get(challenge_move)["points"]

        df.at[i,"p1"] = p1_outcome+p1_points
        df.at[i,"p2"] = p2_outcome+p2_points

    p1 = df["p1"].astype(int).sum()
    p2 = df["p2"].astype(int).sum()

    return p1, p2

def main():
    test_p1,test_p2 = get_score(get_challenge_data("example"))
    p1,p2 = get_score(get_challenge_data("actual"))

    test_part_one = test_p1
    test_part_two = test_p2

    part_one = p1
    part_two = p2

    if part_two and part_one:
        test_before_submit(day, year, part="b", test_answer=test_part_two, answer=part_two)
    elif part_one:
        test_before_submit(day, year, part="a", test_answer= test_part_one, answer=part_one)
    else:
        raise ValueError("Missing Answers")

if __name__ == "__main__":
    main()