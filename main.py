import sys

import generate_data
import csv
import json
import sql
import html

size = int(sys.argv[1])
type = sys.argv[2]

people = generate_data.generator(size)
json = json.format_json(people)
csv = csv.format_csv(people)
sql = sql.format_insert(people)
html = html.format_html(people)

if type == "-json":
    print(json, end='')
elif type == "-csv":
    print(csv, end='')
elif type == "-sql":
    print(sql, end='')
elif type == "-html":
    print(html, end='')
else:
    print("error")
