import utils.Examples as exm
from aocd import get_data, submit
import pandas as pd
from io import StringIO

year=2022

def get_challenge_data(day, column_name, run_type="test", seperator=","):
    example_data = exm.examples[f"Day_{day}"]["example"]
    challenge_data = get_data(day=day, year=year)

    if run_type == "test":
        data = example_data
    else:
        data = challenge_data

    df = pd.read_csv(StringIO(data), names=[column_name], sep=seperator)

    return df

def test_before_submit(day,year,part,test_answer,answer):
    expected = exm.examples[f"Day_{day}"][part]
    if test_answer == expected:
        print("🎉 Submitting!")
        submit(answer, part=part, day=day, year=year)
    else:
        print(f"""Something isn't right here! 
        Expected: {expected}
        Receive: {test_answer}
        Difference {test_answer} - {expected}""")