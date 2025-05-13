import requests
import json
import csv

response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = json.loads(response.text)

with open('dz1205.csv', 'w') as f:
    writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=todos[0].keys())
    writer.writeheader()
    for d in todos:
        writer.writerow(d)

print(todos[0].keys())