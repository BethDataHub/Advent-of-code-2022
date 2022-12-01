import utils.Examples as exm
from aocd import submit

day=2
year=2022
part = "a"

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