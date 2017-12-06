
def checksum(spreadsheet):
    total = 0
    rows = spreadsheet.split('\n')
    rows.pop()
    for row in rows:
        split_row = row.split()
        split_row = list(map(int, split_row))

        # Find pair that is evenly divisible
        found = False
        for i in range(len(split_row)):
            first = split_row[i]

            for j in range(i + 1, len(split_row)):
                second = split_row[j];

                if not first % second:
                    total += first / second
                    found = True
                    break

                elif not second % first:
                    total += second / first
                    found = True
                    break
            if found:
                break
      
    return total

test_one = """5\t9\t2\t8
9\t4\t7\t3
3\t8\t6\t5\n"""

assert checksum(test_one) == 9


with open('day2.txt', 'r') as myfile:
    data=myfile.read()
    print(checksum(data))

