import numpy as np


class FreeEnergy:
    def __init__(self, mlist):
        self.mlist = mlist.copy()
        self.m = mlist

    def f(self, s, lam):
        raise NotImplementedError('You should implement f(s, lam) which is free energy.')

    def selfconsistent_m(self, s, lam):
        raise NotImplementedError('You should implement selfconsistent_m(s) which is self consistent equation')

    def get_m_each(self, slist, lam):
        mvss = []
        for s in slist:
            self.m = self.mlist
            for _ in range(10):
                  self.m = self.selfconsistent_m(s, lam) # 逐次代入でself-consitent方程式を解く
            mvss.append(self.m[np.argmin(self.f(s, lam))])  # 得た解から f を最小にする m を選んでくる.
        self.m = self.mlist.copy()
        return mvss

    def get_phasediagram(self, slist, lamlist, onlyF=False):
        self.m = self.mlist.copy()
        dm_threshold = (self.mlist[1] - self.mlist[0]) * 5

        # 逐次代入 か 自由エネルギーだけをみて磁場を測るか. onlyF フラグで判定
        if onlyF:
            self.m = np.arange(0, 1.01, 0.01)
            getm = lambda _slist, lam: [self.m[np.argmin(self.f(s, lam))] for s in _slist]
        else:
            getm = lambda _slist, lam: self.get_m_each(_slist, lam)

        trans_s = []
        for lam in lamlist:
            m = getm(slist, lam)
            dm = [m[i + 1] - m[i] for i in range(len(m) - 1)]
            trans_dm = [tdm for tdm in dm if tdm > dm_threshold]
            for tdm in trans_dm:
                trans_s.append([lam, slist[dm.index(tdm)]])  # 転移する直前が記録される

        # [lambda, s]
        return np.array(trans_s).T




