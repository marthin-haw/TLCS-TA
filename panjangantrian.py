from __future__ import absolute_import
from __future__ import print_function

import os
import traci
import timeit
import matplotlib.pyplot as plt

from utils import import_test_configuration, set_sumo

class Simulation:
    def __init__(self, sumo_cmd, max_steps):
        self._step = 0
        self._sumo_cmd = sumo_cmd
        self._max_steps = max_steps
        self._queue_length_episode = []
        self._halt_N = []
        self._halt_S = []
        self._halt_E = []
        self._halt_W = []

    def run(self):
        """
        Runs the testing simulation
        """
        start_time = timeit.default_timer()

        # first, generate the route file for this simulation and set up sumo
        traci.start(self._sumo_cmd)
        print("Simulating...")

        # inits
        self._step = 0
        self._waiting_times = {}

        while self._step < self._max_steps:
            traci.simulationStep()  # simulate 1 step in sumo
            self._step += 1  # update the step counter
            queue_length, halt_N, halt_S, halt_E, halt_W = self._get_queue_length()
            self._queue_length_episode.append(queue_length)
            self._halt_N.append(halt_N)
            self._halt_S.append(halt_S)
            self._halt_E.append(halt_E)
            self._halt_W.append(halt_W)

        traci.close()
        simulation_time = round(timeit.default_timer() - start_time, 1)
        return simulation_time

    def _get_queue_length(self):
        """
        Retrieve the number of cars with speed = 0 in every incoming lane
        """
        halt_N = traci.edge.getLastStepHaltingNumber("N2TL")
        halt_S = traci.edge.getLastStepHaltingNumber("S2TL")
        halt_E = traci.edge.getLastStepHaltingNumber("E2TL")
        halt_W = traci.edge.getLastStepHaltingNumber("W2TL")
        queue_length = halt_N + halt_S + halt_E + halt_W
        return queue_length, halt_N, halt_S, halt_E, halt_W

    @property
    def queue_length_episode(self):
        return self._queue_length_episode

    @property
    def halt_N(self):
        return self._halt_N

    @property
    def halt_S(self):
        return self._halt_S

    @property
    def halt_E(self):
        return self._halt_E

    @property
    def halt_W(self):
        return self._halt_W

if __name__ == "__main__":

    config = import_test_configuration(config_file='testing_settings.ini')
    sumo_cmd = set_sumo(config['gui'], config['sumocfg_file_name'], config['max_steps'])
    plot_path = os.path.join('intersection', '')

    Simulation = Simulation(
        sumo_cmd,
        config['max_steps']
    )

    print('\n----- Simulation without model')
    simulation_time = Simulation.run()  # run the simulation
    print('Simulation time:', simulation_time, 's')

    print("----- Simulation info saved at:", plot_path)

    #plot queue lenght of every lane and total queue in one graph
    min_val = min(Simulation.queue_length_episode)
    max_val = max(Simulation.queue_length_episode)
    plt.rcParams.update({'font.size': 24})  # set bigger font size
    plt.stairs(Simulation.queue_length_episode, label='total_queue')
    plt.stairs(Simulation.halt_N, label='queue_N')
    plt.stairs(Simulation.halt_S, label='queue_S')
    plt.stairs(Simulation.halt_E, label='queue_E')
    plt.stairs(Simulation.halt_W, label='queue_W')
    plt.ylabel('Queue lenght (vehicles)')
    plt.xlabel('Step')
    plt.margins(0)
    plt.legend()
    plt.ylim(-5, max_val + 0.05 * abs(max_val))
    fig = plt.gcf()
    fig.set_size_inches(20, 11.25)
    fig.savefig(os.path.join(plot_path, 'plot_queue.png'))
    plt.close("all")

    with open(os.path.join(plot_path, 'plot_total_queue_data.txt'), "w") as file:
        for value in Simulation.queue_length_episode:
            file.write("%s\n" % value)

    with open(os.path.join(plot_path, 'plot_queue_N_data.txt'), "w") as file:
        for value in Simulation.halt_N:
            file.write("%s\n" % value)

    with open(os.path.join(plot_path, 'plot_queue_S_data.txt'), "w") as file:
        for value in Simulation.halt_S:
            file.write("%s\n" % value)

    with open(os.path.join(plot_path, 'plot_queue_E_data.txt'), "w") as file:
        for value in Simulation.halt_E:
            file.write("%s\n" % value)

    with open(os.path.join(plot_path, 'plot_queue_W_data.txt'), "w") as file:
        for value in Simulation.halt_W:
            file.write("%s\n" % value)

    #plot total queue lenght
    #Visualization.save_data_and_plot(data=Simulation.queue_length_episode, filename='total_queue', xlabel='Step', ylabel='Queue lenght (vehicles)')