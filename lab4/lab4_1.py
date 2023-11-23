import json

FILENAME = "input.json"


def task() -> float:
    reader = json.load(open(FILENAME, 'r'))
    total_sum = sum(item.get("score", 0.0) * item.get("weight", 1) for item in reader)
    return round(total_sum, 3)


if __name__ == '__main__':
    print(task())
