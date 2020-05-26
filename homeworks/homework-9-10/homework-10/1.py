import argparse
import re


parser = argparse.ArgumentParser(description="getter count pages in .pdf")

parser.add_argument("-f", "--filename", type=str, help="filename")
args = parser.parse_args()


def get_count_pages_pdf(filename):
    count = 0
    re_pattern = re.compile("Page\W")
    with open(filename, "rb") as f:
        for line in f:
            if re_pattern.search(str(line)) and "Pages" not in str(line):
                # print(line)
                count += 1
    return count


if __name__ == "__main__":
    filename = args.filename
    count_pages = get_count_pages_pdf(filename)
    print(count_pages)
