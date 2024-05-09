import numpy as np




def running_average(average_window_size, measures_in_hops):
    average_y = []
    for i in range(len(measures_in_hops[0]) - average_window_size + 1):
        average_y.append(np.mean(measures_in_hops[0][i:i + average_window_size]))
    for i in range(average_window_size - 1):
        average_y.insert(0, np.nan)
    return average_y
