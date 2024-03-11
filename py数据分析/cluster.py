import sklearn
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def pre_check(data):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(data["FACTOR1"],data["FACTOR2"],data["FACTOR3"],cmap="rainbow")
    ax.view_init(45,45)
    plt.show()

