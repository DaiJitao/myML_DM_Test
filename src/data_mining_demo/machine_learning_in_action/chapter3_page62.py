import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="22")
arrow_args = dict(arrowstyle="<-")


def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    """

    :param nodeTxt: 注释
    :param centerPt: 箭头终止位置
    :param parentPt: 箭头起始位置
    :param nodeType: 节点类型
    :return:
    """
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',
                            xytext=centerPt, textcoords='axes fraction',
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)


def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf() # clear figure
    axprops = dict(xticks=[], yticks=[])
    # createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)    #no ticks
    createPlot.ax1 = plt.subplot(111, frameon=True)  # ticks for demo puropses
    plotNode("dd", (.5, .1), (.1, .5), decisionNode)
    plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()

createPlot()
