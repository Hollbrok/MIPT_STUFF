import matplotlib.pyplot as plt
import numpy as np
import pandas

from scipy.interpolate import interp1d


colors = ["red", "green", "blue"]


def build_graph(x, y, label, fig_name, i):
    plt.plot(x, y, '+', label=label, color = colors[i])
    # 300 represents number of points to make between T.min and T.max
    f_cubic = interp1d(x, y, kind='cubic')
    xnew = np.linspace(min(x), max(x), num=41, endpoint=True)
    plt.plot(xnew, f_cubic(xnew), '--')


    plt.grid()
    plt.legend()
    plt.xlabel("$\\frac{1}{n^2} - \\frac{1}{m^2}$")                                          # подпись оси X
    plt.ylabel("$\\frac{1}{\lambda}$, $10^{-4}\ \mathring{A}^{-1}$")             # подпись оси Y
    #plt.tight_layout() 
    plt.savefig(fig_name)

def main():
    print("ffff")
    result = pandas.read_csv('Data.csv',encoding='utf-8')
    print(result)
    
    #print(f"x1 = {result['x1']}\n y1 = {result['y1']}")
    #print(f"x2 = {result['x2'].dropna()}\n y2 = {result['y2'].dropna()}")

    y1 = result['wave_length'].dropna()
    x1 = result['degree'].dropna()

    y2 = result['wave_length2'].dropna()
    x2 = result['degree2'].dropna()


    #build_graph(x = x1, y = y1, label = "Неон", fig_name = "1", i = 1)
    #plt.close()
    #build_graph(x = x2, y = y2, label = "Ртуть", fig_name = "2", i = 2)
    #plt.close()

    x3 = [0.139, 0.188, 0.21, 0.222]
    y3 = [1.528, 2.059, 2.3, 2.436]
    build_graph(x = x3, y = y3, label = "", fig_name = "3", i = 0)

if __name__ == '__main__':
    main()