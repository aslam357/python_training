import csv
def parse_csv(file):    
    print(open(file).read())
    with open(file,mode="r") as csvfile:        
        reader=csv.reader(csvfile)
        p=[row for row in reader]
    return p
file='E:\\aslam.csv'
parsed=parse_csv(file)
print(parsed)
