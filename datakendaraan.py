import csv

with open("C:\\Users\marth\Documents\Tugas Akhir\YOLO dan OpenCV\\vehicle-detection-classification-opencv\data_gab(12-15)-sort.csv") as f1:
    data = csv.reader(f1)

    with open("intersection/mapTA2new.rou.xml", "w") as routes:
        print('''<routes>
        <!-- VTypes -->
        <vType id="DEFAULT_VEHTYPE" emissionClass="HBEFA3/Bus" guiShape="bus" color="red"/>
        <vType id="bus" length="9.00" minGap="1.50" vClass="bus" emissionClass="HBEFA3/PC_G_EU4" guiShape="bus" width="2.10" height="1.50" color="blue"/>
        <vType id="car" length="4.20" minGap="1.50" emissionClass="HBEFA3/PC_G_EU4" guiShape="passenger" width="1.80" height="1.50" color="red" latAlignment="nice"/>
        <vType id="motorcycle" length="2.00" minGap="1.00" vClass="motorcycle" emissionClass="HBEFA3/PC_G_EU4" guiShape="motorcycle" width="0.80" height="1.50" color="green" latAlignment="nice"/>
        <vType id="truck" length="7.00" minGap="1.50" vClass="truck" emissionClass="HBEFA3/PC_G_EU4" guiShape="truck" width="2.00" height="1.50" color="yellow"/>
        <!-- Routes -->
        <route id="route_0" edges="W2TL TL2E" color="yellow"/>
        <route id="route_1" edges="W2TL TL2S" color="yellow"/>
        <route id="route_10" edges="N2TL TL2W" color="yellow"/>
        <route id="route_11" edges="N2TL TL2E" color="yellow"/>
        <route id="route_2" edges="W2TL TL2N" color="yellow"/>
        <route id="route_3" edges="S2TL TL2N" color="yellow"/>
        <route id="route_4" edges="S2TL TL2W" color="yellow"/>
        <route id="route_5" edges="S2TL TL2E" color="yellow"/>
        <route id="route_6" edges="E2TL TL2W" color="yellow"/>
        <route id="route_7" edges="E2TL TL2S" color="yellow"/>
        <route id="route_8" edges="E2TL TL2N" color="yellow"/>
        <route id="route_9" edges="N2TL TL2S" color="yellow"/>
        <!-- Vehicles, persons and containers (sorted by depart) -->''', file=routes)
        for row in data:
            if row:
                id = row[0]
                class_name = row[1]
                route = row[2]
                depart = row[3]
                print("    <vehicle id=\"" + id + "\" type=\"" + class_name + "\" depart=\"" + depart + "\" departLane=\"best\" departSpeed=\"10\" route=\"" + route + "\"/>", file=routes)

        print("</routes>", file=routes)