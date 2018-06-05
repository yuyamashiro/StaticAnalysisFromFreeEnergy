import matplotlib.pyplot as plt

from .CalculatePhasediagram import *

def plot_setting(font_size=8):
    plt.rcParams['font.family'] = 'sans-serif'  # 使用するフォント
    plt.rcParams['xtick.direction'] = 'in'  # x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['ytick.direction'] = 'in'  # y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['xtick.major.width'] = 1.0  # x軸主目盛り線の線幅
    plt.rcParams['ytick.major.width'] = 1.0  # y軸主目盛り線の線幅
    plt.rcParams['font.size'] = font_size  # フォントの大きさ
    plt.rcParams['axes.linewidth'] = 1.0  # 軸の線幅edge linewidth。囲みの太さ

class DrawFigure:
    def __init__(self, free_energy, mlist, slist, lamlist, onlyF):
        self.slist = slist
        self.lamlist = lamlist
        self.onlyF = onlyF
        self.free_energy = free_energy
        self.phasediagrams = []
        self.label_list = []
        self.mlist = mlist

    def calculation(self, params, label):
        fe = self.free_energy(self.mlist, params)
        calc_phasediagram = CalculatePhaseDiagram(fe, params)
        self.phasediagrams.append(
            calc_phasediagram.calculate(slist=self.slist, lamlist=self.lamlist, onlyF=self.onlyF)
        )
        all_params = params
        all_params['onlyF'] = self.onlyF
        self.label_list.append(label)

    def draw_figure(self, file_name):
        plot_setting(font_size=10)
        plt.xlim(0,1)
        plt.ylim(0,1)
        for pd, label in zip(self.phasediagrams, self.label_list):
            plt.plot(pd[1], pd[0], '.', label=label)
        plt.legend()
        plt.savefig(file_name)

