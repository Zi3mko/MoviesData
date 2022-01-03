import json 
import csv

with open('./datasets/Movies.csv','r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    data = {"movies": []}
    for row in reader:
        data["movies"].append({"Title": row[0], "Director": row[1], "Cast": row[2], "ReleaseYear": row[3], "Duration": row[4], "Categories": row[5], "Description": row[6]})
with open("movies.json",'w') as f:
    json.dump(data,f, indent=4)