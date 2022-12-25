filename = "prac_05/wimbledon.csv"


def main():
    record = get_record(filename)


def get_record(filename):
    record = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readlines()
        for line in in_file:
            part = line.strip().split(",")
            record.append(part)
        return record

main()