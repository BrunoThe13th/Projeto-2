import sys
import generate_data
import insert
import csv
import json

size = int(sys.argsqlv[1])
type = sys.argv[2]

people = generate_data.generator(size)
insert_sql = insert.format_insert(people)
json = json.format_json(people)
csv = csv.format_csv(people)

if type == "-insert":
    print(insert_sql)
elif type == "-json":
    print(json)
elif type == "-csv":
    print(csv)
else:
    print("error")
