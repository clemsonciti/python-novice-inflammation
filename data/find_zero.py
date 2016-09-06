import numpy as np

def find_zero_rows(filename):
    data = np.loadtxt(filename, delimiter=',')
    num_zero_rows = 0
    cols, rows = np.shape(data)
    for i in range(rows):
        if np.all(data[i, :]==0):
            num_zero_rows = num_zero_rows + 1
    return num_zero_rows

