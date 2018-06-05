import os
import numpy as np

from .utils import *

class CalculatePhaseDiagram:
    def __init__(self, free_energy, params):
        self.free_energy = free_energy
        self.params = params

    def calculate(self, slist, lamlist, onlyF=False):
        all_params = self.params
        all_params['onlyF'] = onlyF
        file_name = './data/phasediagram/phasediagram_{}.txt'.format(filename_from(all_params))
        if os.path.exists(file_name):
            print('----- load success {} -----'.format(file_name))
            phase_diagram = np.loadtxt(file_name)
        else:
            print('****** calculate {} *******'.format(file_name))
            phase_diagram = self.free_energy.get_phasediagram(slist, lamlist, onlyF)
            np.savetxt(file_name, phase_diagram)
        return phase_diagram


