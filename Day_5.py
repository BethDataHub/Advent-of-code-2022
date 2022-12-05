from utils.test import get_challenge_data
import pandas as pd

def parse_data():
    df = get_challenge_data(day=5, column_name=["moves"], run_type="actual")

    row_split  = df.loc[df["moves"].str.startswith('move', na=False)].index[0]
    moves  = df.loc[df["moves"].str.startswith('move', na=False)].reset_index().iloc[: , 1:]

    moves["quantity"] = moves["moves"].str.split(" ").str[1]
    moves["from"] = moves["moves"].str.split(" ").str[3]
    moves["to"] = moves["moves"].str.split(" ").str[5]

    stacks = df[0:row_split-1]

    split_stacks = pd.DataFrame(list(stacks["moves"][i]) for i in range(8))

    stacks_df = split_stacks[[1,5,9,13,17,21,25,29,33]].rename(columns={5:2,9:3,13:4,17:5,21:6,25:7,29:8,33:9})
    stacks_df = stacks_df.iloc[::-1]

    return moves, stacks_df
    

def create_lists(stacks_df):

    for columns in stacks_df:
        globals()[f"list_{columns}"] = eval(f'stacks_df[{columns}].loc[stacks_df[{columns}] != " "].tolist()')

    return list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9


def part_one(moves):
    for index, move in moves.iterrows():
        quantity=int(move["quantity"])
        to_list=move["to"]
        from_list=move["from"]

        eval(f"list_{to_list}.extend(list_{from_list}[-{quantity}:][::-1])")
        globals()[f"list_{from_list}"] = eval(f'list_{from_list}[:-{quantity}]')

    print(f"{list_1.pop()}{list_2.pop()}{list_3.pop()}{list_4.pop()}{list_5.pop()}{list_6.pop()}{list_7.pop()}{list_8.pop()}{list_9.pop()}")

list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9 = create_lists(parse_data()[1])
part_one(parse_data()[0])


def part_two(moves):
    for index, move in moves.iterrows():
        quantity=move["quantity"]
        to_list=move["to"]
        from_list=move["from"]

        eval(f"list_{to_list}.extend(list_{from_list}[-{quantity}:])")
        globals()[f"list_{from_list}"] = eval(f'list_{from_list}[:-{quantity}]')

    print(f"{list_1.pop()}{list_2.pop()}{list_3.pop()}{list_4.pop()}{list_5.pop()}{list_6.pop()}{list_7.pop()}{list_8.pop()}{list_9.pop()}")

list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9 = create_lists(parse_data()[1])
part_two(parse_data()[0])