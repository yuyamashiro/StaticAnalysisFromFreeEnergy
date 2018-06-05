import os
import numpy as np

from .utils import *

class CalculatePhaseDiagram:
    def __init__(self, free_energy, params):
        self.free_energy = free_energy
        self.params = params

    def calculate(self, slist, lamlist, onlyF=False):
        # スクリプトのあるディレクトリの絶対パスを取得
        name = os.path.dirname(os.path.abspath(__name__))
        joined_path = os.path.join(name, '../data/phasediagram/')
        data_path = os.path.normpath(joined_path)
        all_params = self.params
        all_params['onlyF'] = onlyF
        file_name = data_path + '/phasediagram_{}.txt'.format(filename_from(all_params))
        if os.path.exists(file_name):
            print('----- load success {} -----'.format(file_name))
            phase_diagram = np.loadtxt(file_name)
        else:
            print('****** calculate {} *******'.format(file_name))
            phase_diagram = self.free_energy.get_phasediagram(slist, lamlist, onlyF)
            np.savetxt(file_name, phase_diagram)
        return phase_diagram

    def calc_mag(self, s, lam, onlyF=True):
        mags = []
        if hasattr(s, "__iter__"):
            for _s in s:
                mags.append(self.free_energy.minimum_m(_s,lam, onlyF))
        else:
            for _l in lam:
                mags.append(self.free_energy.minimum_m(s, _l, onlyF))
        return mags


