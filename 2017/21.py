
def checksum(spreadsheet):
    total = 0
    rows = spreadsheet.split('\n')
    rows.pop()
    for row in rows:
        split_row = row.split()
        split_row = list(map(int, split_row))
        total += max(split_row) - min(split_row)
      
    return total

test_one = """5\t1\t19\t5
7\t5\t3
2\t4\t6\t8\n"""

assert checksum(test_one) == 28


with open('day2.txt', 'r') as myfile:
    data=myfile.read()
    print(checksum(data))

