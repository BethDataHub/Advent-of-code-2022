from aocd import get_data, submit

def get_marker(characters):
    for i in range(len(data)):
        if len(set(data[i:i+characters])) == characters:
            return i+characters
        
data = get_data(day=6, year=2022)

submit(get_marker(4), part="a")
submit(get_marker(14), part="b")