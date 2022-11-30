# This scrpit takes all of the flight data and returns data in correct form ready for training the GNN 
import pandas as pd
import os

def load_flights():

    for flight_file in os.walk("../data/pigeonflocks_trajectories/ff2/"):
        path_list = flight_file[2]
        
    flights_list = []    
    for flight in path_list:    
        full_path = "../data/pigeonflocks_trajectories/ff2/" + flight
        data_out = pd.read_csv(full_path, delimiter="\t",skiprows=18)
        start_time = 2300000
        end_time = 2400000

        # start at a given row so all birds begin at the same timestep.
        data_out = data_out[data_out['#t(centisec)'].between(start_time, end_time)]
        if len(data_out) == 5001:
            flights_list.append(data_out)

    return flights_list


# Expected form of data 

# are timereadings evently spaced?

# decide on features to use?... should the hireracty effect the potential?.


# are timesteps equaly spaced?...  



# Nodes 
# torch.Size([10000 sims of, 500 frames, num_birds, 6 + num featues])

# Acelleration (Y)
# torch.Size([10000, 500, num_birds, 3])