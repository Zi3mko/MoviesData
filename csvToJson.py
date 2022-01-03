import json
import csv

data ={}

with open("Movies.csv",encoding='utf-8') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        key = rows['movie_id']
        data[key] = rows

with open("movies.json",'w',encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data,indent=4))