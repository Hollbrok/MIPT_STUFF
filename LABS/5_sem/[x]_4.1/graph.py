import matplotlib.pyplot as plt
import numpy as np
import pandas

colors = ["red", "green", "blue"]

def build_graph(x, y, label, fig_name, i):
    lin_x = x[[9, -1]]
    lin_y = y[[9, -1]]
    plt.plot(x, y, '+', label=label, color = colors[i])
    plt.plot(lin_x, lin_y, '-', color = colors[1], label = "Аппроксимация прямой линейного участка")
    plt.grid()
    plt.legend()
    plt.xlabel("$P$, торр")                                          # подпись оси X
    plt.ylabel("$N$, кол-во")             # подпись оси Y
    #plt.tight_layout() 
    plt.savefig(fig_name)

def main():
    result = pandas.read_csv('Data.csv')
    print(result)

    P = np.array(result['P'].dropna())
    N = np.array(result['N'].dropna() / 10, dtype=int)

    print(f"P = {P}\nN = {N}\n")
    build_graph(x = P, y = N, label = "Данные $N$ ($P$) (сцинтилляционный счетчик)", fig_name = "graph_2", i = 2)    
    #build_graph(x = x2, y = y2, label = "$I_k$ ($V_a$) при $V_{\text{задер.}}$ = 6 В", fig_name = "graph5", i = 1)
    #build_graph(x = x3, y = y3, label = "$I_k$ ($V_a$) при $V_{\text{задер.}}$ = 8 В", fig_name = "graph6", i = 2)
    #build_graph(x = x2_0, y = y2_0, label = "$I_0$ ($V_a$) при $V_{задер.}$ = 6 В", fig_name = "for10", i = 2)
    #plt.close()
    #build_graph(x = x2, y = y2_new, label = "$I_{\sim}$ ($V_a$) при $V_{задер.}$ = 6 В", fig_name = "for10_full", i = 2)

if __name__ == '__main__':
    main()