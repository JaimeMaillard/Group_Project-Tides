import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("ASTR19_F24_group_project_data.txt",
                     dtype=[('day', 'i8'), ('time', 'U6'), ('height', 'f8')])

day, time, height = data['day'].tolist(), data['time'].tolist(), data['height'].tolist()

def condense_list(lst, n=5):
    return f"{lst[:n]} ... {lst[-n:]}" if len(lst) > 2 * n else str(lst)

print("Day:", condense_list(day))
print("Time:", condense_list(time))
print("Height:", condense_list(height))