
from progressbar import *
total = 1000
def dosomework():
    time.sleep(0.01)
pbar = ProgressBar().start()
for i in range(1000):
    pbar.update(int((i / (total - 1)) * 100))
    dosomework()
