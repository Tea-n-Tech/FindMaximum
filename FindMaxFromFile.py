import csv
import math

with open('values.csv') as csvFile:

    csv_reader = csv.reader(csvFile, delimiter=";")
    line_count = 0

    id_max = 0
    value_max = -math.inf

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'Our id is {row[0]} and our value is {row[1]}')
            line_count += 1
            if float(row[1]) > value_max:
                id_max, value_max = row[0], float(row[1])

    print(f'Processed lines: {line_count}')
    print(f'Max_id: {id_max} and max Value: {value_max}')
