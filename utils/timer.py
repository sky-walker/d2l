import sys

sys.path.append('..')

import time
import numpy as np


class Timer:

    def __init__(self):
        self.times = []
        self.start()

    '''启动计时器'''

    def start(self):
        self.tik = time.time()

    '''停止计时器'''

    def stop(self):
        self.times.append(time.time() - self.tik)
        return self.times[-1]

    '''返回平均用时'''

    def avg(self):
        return sum(self.times) / len(self.times)

    '''返回总用时'''

    def sum(self):
        return sum(self.times)

    '''返回累计用时'''

    def cumsum(self):
        return np.array(self.times).cumsum.tolist()


if __name__ == '__main__':
    timer = Timer()
    timer.start()
    print(f'{timer.stop():.5f} sec')
