from utils.test import get_challenge_data, test_before_submit
import os

AOC_SESSION = os.getenv("AOC_SESSION") 
day=3

lower = 96
upper = 38

def get_incorrect_item(data):
    data["first"] = data["Backpack Contents"].apply(lambda x: x[:int(len(x)/2)])
    data["second"] = data["Backpack Contents"].apply(lambda x: x[int(len(x)/2):])
    data["return"] = data.apply(lambda x: set(x["first"]).intersection(x["second"]), axis=1).str.join('')
    data["priority"] = data["return"].apply(lambda x: ord(x)-upper if x.isupper() else ord(x)-lower)

    part_one = data["priority"].sum()

    i=0
    part_two=0
    while i < len(data):
        df = data["Backpack Contents"][i:i+3].tolist()
        common = list(set.intersection(*map(set,df)))
        part_two+=(ord(common[0])-upper if common[0].isupper() else ord(common[0])-lower)
        i+=3

    return part_one, part_two

def main():
    test_part_one,test_part_two = get_incorrect_item(get_challenge_data(day=day, column_name=["Backpack Contents"]))
    part_one,part_two = get_incorrect_item(get_challenge_data(day=day, column_name=["Backpack Contents"], run_type="actual"))

    if part_two and part_one:
        test_before_submit(day, part="b", test_answer=test_part_two, answer=part_two)
    elif part_one:
        test_before_submit(day, part="a", test_answer= test_part_one, answer=part_one)
    else:
        raise ValueError("Missing Answers")

if __name__ == "__main__":
    main()
