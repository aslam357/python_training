import csv
def parse_csv(file, delimiter=',', comment='#'):
    with open(file, mode="r") as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        p=[row for row in reader]
    return p
file = 'E:\\a.csv'
parse = parse_csv(file, delimiter=',', comment='#')
print(parse)
