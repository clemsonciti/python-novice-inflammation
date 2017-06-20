import numpy as np

def count_zero_rows(filename):
    """
    Counts the number of rows
    containing all zeros
    in the file "filename"

    Parameters
    ----------

    filename : str
        Name of csv file containing the data

    Returns
    -------

    num_zero_rows : int
        Number of zero rows
        
    Examples
    --------
    >>> count_zero_rows('small-01.csv')
    2

    >>> count_zero_rows('small-02.csv')
    0

    """

    # read the file
    data = np.loadtxt(filename, delimiter=',')

    # get number of columns and rows:
    cols, rows = np.shape(data)

    # loop over rows; increase num_zero_rows if any row is all zeros
    num_zero_rows = 0
    for i in range(rows):
        if np.all(data[i, :]==0):
            num_zero_rows = num_zero_rows + 1

    return num_zero_rows

print(count_zero_rows(filename))
