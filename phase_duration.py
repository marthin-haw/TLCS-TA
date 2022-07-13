import csv

all_phase = []
duration = []
green_duration = 10
yellow_duration = 2
all_red_duration = 2
list_queue_east = []
list_queue_north = []
list_queue_west = []
list_queue_south = []
queue_east = []
queue_north = []
queue_west = []
queue_south = []

with open("C:\\Users\marth\Documents\Tugas Akhir\RL Sumo\TLCS TA\models\model_4\\test\phase_duration.csv", 'w') as f:
    cwriter = csv.writer(f)

    with open("C:\\Users\marth\Documents\Tugas Akhir\RL Sumo\TLCS TA\models\model_4\\test\plot_phase.txt") as f1:
        phase = f1.readlines()
        for i in phase:
            all_phase.append(i.replace('\n', ''))
        for i in all_phase:
            if i.endswith('GREEN'):
                duration.append(green_duration)
            if i.endswith('YELLOW'):
                duration.append(yellow_duration)
            if i.endswith('RED'):
                duration.append(all_red_duration)

    with open("C:\\Users\marth\Documents\Tugas Akhir\RL Sumo\TLCS TA\models\model_4\\test\plot_queue_E_data.txt") as f2:
        data_queue_east = f2.readlines()
        n = 0
        for i in data_queue_east:
            list_queue_east.append(int(i.replace('\n', '')))
        for j in duration:
            n = n + j
            queue_east.append(list_queue_east[n-1])

    with open("C:\\Users\marth\Documents\Tugas Akhir\RL Sumo\TLCS TA\models\model_4\\test\plot_queue_N_data.txt") as f3:
        data_queue_north = f3.readlines()
        n = 0
        for i in data_queue_north:
            list_queue_north.append(int(i.replace('\n', '')))
        for j in duration:
            n = n + j
            queue_north.append(list_queue_north[n-1])

    with open("C:\\Users\marth\Documents\Tugas Akhir\RL Sumo\TLCS TA\models\model_4\\test\plot_queue_W_data.txt") as f4:
        data_queue_west = f4.readlines()
        n = 0
        for i in data_queue_west:
            list_queue_west.append(int(i.replace('\n', '')))
        for j in duration:
            n = n + j
            queue_west.append(list_queue_west[n - 1])

    with open("C:\\Users\marth\Documents\Tugas Akhir\RL Sumo\TLCS TA\models\model_4\\test\plot_queue_S_data.txt") as f5:
        data_queue_south = f5.readlines()
        n = 0
        for i in data_queue_south:
            list_queue_south.append(int(i.replace('\n', '')))
        for j in duration:
            n = n + j
            queue_south.append(list_queue_south[n - 1])

    all_phase.insert(0, 'phase')
    duration.insert(0, 'duration')
    queue_east.insert(0, 'queue east')
    queue_north.insert(0, 'queue north')
    queue_west.insert(0, 'queue west')
    queue_south.insert(0, 'queue south')
    for i in range(len(all_phase)):
        cwriter.writerow([all_phase[i], duration[i], queue_east[i], queue_north[i], queue_west[i], queue_south[i]])

f.close()
print("Data saved at 'phase_duration.csv'")