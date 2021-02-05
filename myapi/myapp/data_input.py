import csv
import json

def convert_csv_to_json():
    csvfile = open('src/data.csv', 'r')
    jsonfile = open('src/file.json', 'w')

    fieldnames = ("id","name","price","size","style","type","color","brand","post_date","status")
    reader = csv.DictReader(csvfile, fieldnames)
    out = json.dumps( [ row for row in reader ] )

    return jsonfile.write(out)
