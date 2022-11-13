import matplotlib.pyplot as plt
import numpy as np
import pandas

colors = ["red", "green", "blue"]

def build_graph(x, y, label, fig_name, i):
    plt.plot(x, y, '+', label=label, color = colors[i])
    plt.grid()
    plt.legend()
    plt.xlabel("$V_a$, В")                                          # подпись оси X
    plt.ylabel("$I_k$, мА")             # подпись оси Y
    #plt.tight_layout() 
    plt.savefig(fig_name)

def main():
    result = pandas.read_csv('1_2.ods')
    #print(result)
    #print(f"x1 = {result['x1']}\n y1 = {result['y1']}")
    #print(f"x2 = {result['x2'].dropna()}\n y2 = {result['y2'].dropna()}")

    x1 = result['x1'].dropna()
    y1 = result['y1'].dropna()

    x2 = result['x2'].dropna()
    y2 = result['y2'].dropna()

    x3 = result['x3'].dropna()
    y3 = result['y3'].dropna()

    x2_0 = list(x2[[6,15,22,35,40]])
    y2_0 = list(y2[[6,15,22,35,40]])


    y2_new = y2 - 1.3254*x2 - 58.8740
    print(f"x = {list(x2)}")
    print(f"y = {list(y2_new)}")

    #build_graph(x = x1, y = y1, label = "$I_k$ ($V_a$) при $V_{\text{задер.}}$ = 4 В", fig_name = "graph4", i = 0)    
    #build_graph(x = x2, y = y2, label = "$I_k$ ($V_a$) при $V_{\text{задер.}}$ = 6 В", fig_name = "graph5", i = 1)
    #build_graph(x = x3, y = y3, label = "$I_k$ ($V_a$) при $V_{\text{задер.}}$ = 8 В", fig_name = "graph6", i = 2)
    build_graph(x = x2_0, y = y2_0, label = "$I_0$ ($V_a$) при $V_{задер.}$ = 6 В", fig_name = "for10", i = 2)
    plt.close()
    build_graph(x = x2, y = y2_new, label = "$I_{\sim}$ ($V_a$) при $V_{задер.}$ = 6 В", fig_name = "for10_full", i = 2)

if __name__ == '__main__':
    main()