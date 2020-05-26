import argparse


parser = argparse.ArgumentParser(description="Free or not places")

parser.add_argument("--get_count", action="store_true", help="Get count free places")
parser.add_argument("--free_or_not", help="Free or not place. Params examples: 1,3")
parser.add_argument("-f", "--filename", type=str, help="filename")
args = parser.parse_args()


def get_list_places(filename):
    lst = []
    with open(filename, "r") as f:
        for line in f:
            lst.append(list(map(int, list(line.rstrip()))))
    return lst


def get_count_free_places(list_places):
    count = sum([line.count(0) for line in list_places])
    return count


def free_or_not(list_places, i, j):
    return list_places[i-1][j-1] == 0


if __name__ == "__main__":
    filename = args.filename
    list_places = get_list_places(filename)
    if args.get_count:
        print(get_count_free_places(list_places))
    if args.free_or_not:
        params = args.free_or_not.split(',')
        print(free_or_not(list_places, int(params[0]), int(params[1])))
