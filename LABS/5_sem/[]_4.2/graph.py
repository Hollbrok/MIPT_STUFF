import matplotlib.pyplot as plt
import numpy as np
import pandas

from scipy.interpolate import interp1d


colors = ["red", "green", "blue"]


def build_graph(x, y, label, fig_name, i):
    plt.xlabel("$I, A$") 
    plt.ylabel("$N-N_ф$") 
    plt.plot(x, y, '+', label=label, color = colors[i])
    plt.grid()
    plt.legend()
    plt.savefig(fig_name)

def main():
    result = pandas.read_csv('data.csv',encoding='utf-8')
    print(result)
    
    #print(f"x1 = {result['x1']}\n y1 = {result['y1']}")
    #print(f"x2 = {result['x2'].dropna()}\n y2 = {result['y2'].dropna()}")

    y1 = result['N-N_phon'].dropna()
    x1 = result['I'].dropna()
    y2 = result["mkFermi"].dropna()
    x2 = result["T"].dropna()

    build_graph(x = x1, y = y1, label = "N-Nф (I)", fig_name = "1", i = 2)
    plt.close()
    build_graph(x = x2, y = y2, label = "mkFermi(T)", fig_name = "2", i = 2)
    plt.close()
    #build_graph(x = x2, y = y2, label = "Ртуть", fig_name = "2", i = 2)
    #plt.close()


if __name__ == '__main__':
    main()