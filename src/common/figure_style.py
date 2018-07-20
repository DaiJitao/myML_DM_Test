import matplotlib.pyplot as plt

class Figure_Style():
    """
    设置图像风格
    """
    def __init__(self, type=None):
        if type == None or type == 0:
            plt.style.use('classic')
        elif type == 1:
            plt.style.use('seaborn-whitegrid')