from __future__ import absolute_import
from __future__ import print_function

import os
from shutil import copyfile
import matplotlib.pyplot as plt

from testing_simulation import Simulation
from model import TestModel
from visualization import Visualization
from utils import import_test_configuration, set_sumo, set_test_path


if __name__ == "__main__":

    config = import_test_configuration(config_file='testing_settings.ini')
    sumo_cmd = set_sumo(config['gui'], config['sumocfg_file_name'], config['max_steps'])
    model_path, plot_path = set_test_path(config['models_path_name'], config['model_to_test'])

    Model = TestModel(
        input_dim=config['num_states'],
        model_path=model_path
    )


    Visualization = Visualization(
        plot_path, 
        dpi=96
    )
        
    Simulation = Simulation(
        Model,
        sumo_cmd,
        config['max_steps'],
        config['green_duration'],
        config['yellow_duration'],
        config['red_duration'],
        config['num_states'],
        config['num_actions']
    )

    print('\n----- Test episode')
    simulation_time = Simulation.run()  # run the simulation
    print('Simulation time:', simulation_time, 's')

    print("----- Testing info saved at:", plot_path)

    copyfile(src='testing_settings.ini', dst=os.path.join(plot_path, 'testing_settings.ini'))

    # plot queue lenght of every lane and total queue in one graph
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

    with open(os.path.join(plot_path, 'plot_phase.txt'), "w") as file:
        for value in Simulation.phase:
            file.write("%s\n" % value)

    Visualization.save_data_and_plot(data=Simulation.reward_episode, filename='reward', xlabel='Action step', ylabel='Reward')
    #Visualization.save_data_and_plot(data=Simulation.queue_length_episode, filename='queue', xlabel='Step', ylabel='Queue lenght (vehicles)')
