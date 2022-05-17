
import csv

with open('data_kendaraan.csv') as f1:
    data = csv.reader(f1)
    for row in data:
        id = row[0]
        route = row[1]
        depart = row[2]
        departSpeed = row[3]
        print("    <vehicle id=\"vehicle_" + id + "\" depart=\"" + depart + "\" departLane=\"random\" departSpeed=\"" + departSpeed + "\" route=\"route_" + route +"\"/>")