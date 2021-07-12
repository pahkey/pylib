import csv

result = []
with open('score.csv', 'r', encoding='euc-kr') as f:
    reader = csv.reader(f)
    for line in reader:
        average = sum(map(int, line[1].split(','))) / 2
        line.append(average)
        result.append(line)

with open('score_result.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)
