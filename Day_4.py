from utils.test import get_challenge_data, test_before_submit
import os

AOC_SESSION = os.getenv("AOC_SESSION") 
day=4

df = get_challenge_data(day=day, column_name=["First Elf","Second Elf"])

def get_answers(df):
    df["First Start"] = df["First Elf"].str.split("-").str[0].astype(int)
    df["First End"] = df["First Elf"].str.split("-").str[1].astype(int)
    df["Second Start"] = df["Second Elf"].str.split("-").str[0].astype(int)
    df["Second End"] = df["Second Elf"].str.split("-").str[1].astype(int)

    df["between"] = (df["Second Start"].between(df["First Start"],df["First End"]) & df["Second End"].between(df["First Start"],df["First End"])) | (df["First Start"].between(df["Second Start"],df["Second End"]) & df["First End"].between(df["Second Start"],df["Second End"]))

    df["overlap"] = df["Second Start"].between(df["First Start"],df["First End"]) | df["Second End"].between(df["First Start"],df["First End"]) | df["First Start"].between(df["Second Start"],df["Second End"]) | df["First End"].between(df["Second Start"],df["Second End"])

    df["test"] = df["Second Start","Second End"].between(df["First Start"],df["First End"])
    
    #part_one = df[df["between"]==True].count()["between"]
    #part_two = df[df["overlap"]==True].count()["between"]

    print(df)

    #return part_one, part_two

get_answers(df)

#def main():
#    test_part_one,test_part_two = get_answers(get_challenge_data(day=day, column_name=["First Elf","Second Elf"]))
#    part_one,part_two = get_answers(get_challenge_data(day=day, column_name=["First Elf","Second Elf"], run_type="actual"))
#
#    if part_two and part_one:
#        test_before_submit(day, part="b", test_answer=test_part_two, answer=part_two)
#    elif part_one:
#        test_before_submit(day, part="a", test_answer= test_part_one, answer=part_one)
#    else:
#        raise ValueError("Missing Answers")
#
#if __name__ == "__main__":
#    main()