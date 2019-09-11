import numpy as np
import pandas as pd

# define function


def make_assignments(students):
    '''takes a file, and produces a set of assignments'''

    if students % 2 == 0:
        n_groups = students / 2
        groups = np.tile(np.arange(n_groups), 2)
        groups = np.random.permutation(groups)
    elif students % 2 == 1:
        n_groups = (students / 2) - 0.5
        groups = np.tile(np.arange(n_groups), 2)
        groups = np.append(groups, n_groups-1)
        groups = np.random.permutation(groups)

    return(groups)

# do work


d = pd.read_csv('~/Desktop/info-290-2019-D_rosters.csv')

np.random.seed(1)
d['group_assignment'] = make_assignments(d.shape[0])

d.to_csv('~/info290-005/assignments/essays/partners.csv')



