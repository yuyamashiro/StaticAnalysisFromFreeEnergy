import numpy as np

from NumericalCalculation.StaticsApproximationF import FreeEnergy
from NumericalCalculation.DrawFigure import DrawFigure


class PbodyInhomogeneous(FreeEnergy):
    def __init__(self, mlist, params):
        super().__init__(mlist)

        self.p = params['p']

    def f(self, s, lam):
        tau = lam
        p1smp = (self.p - 1.0) * s * self.m ** self.p
        spmp1 = s * self.p * self.m ** (self.p - 1.0)
        return (1.0 - tau) * (p1smp - np.sqrt(spmp1 ** 2 + 1.0)) + tau * (p1smp - spmp1)

    def selfconsistent_m(self, s, lam):
        spmp1 = s * self.p * self.m ** (self.p - 1.0)
        return (1.0 - lam) * spmp1 / np.sqrt(spmp1 ** 2 + 1.0) + lam

def main():

    plist = [3, 4, 5]

    slist = np.arange(0, 1.001, 0.001)
    lamlist = np.arange(0, 1.01, 0.01)
    mlist = np.arange(0, 1.01, 0.01)
    draw_figure = DrawFigure(PbodyInhomogeneous, mlist, slist, lamlist, onlyF=True)

    for p in plist:
        draw_figure.calculation(params={'p':p}, label='p={}'.format(p))

    file_name = 'figures/phasediagram_p{}.pdf'.format(p)
    draw_figure.draw_figure(file_name)


if __name__ == "__main__":
    main()