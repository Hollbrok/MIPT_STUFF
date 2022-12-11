import matplotlib.pyplot as plt
import numpy as np
import pandas

from scipy.interpolate import interp1d


colors = ["red", "green", "blue"]

def build_graph(x: list, y: list, label, fig_name, i):
    print(f" {len(x)}, {len(y)}")
    plt.xlabel("$l, см$")
    plt.ylabel("$ln(\\frac{N}{N_0})$") 
    plt.plot(x, y, '+', label=label, color = colors[i])
    
    plt.plot([x[0], x[4]], [y[0], y[4]])
    
    plt.grid()
    plt.legend()
    plt.savefig(fig_name)

def main():
    result = pandas.read_csv('for-python.csv',encoding='utf-8')
    print(result)

    n_0 = 139843
    n_phon = 170
    N_0 = n_0 - n_phon

    X = []
    Y = []

    for i in range(3):
        Y.append(result[f"n{i+1}"].dropna())
        X.append(result[f"l{i+1}"].dropna())
        #print(f"x = {X[-1]}")
        #print(f"y = {Y[-1]}")

    labels = ["Свинец", "Железо", "Алюминий"]

    print(f"X = {X}")

    for i in range(3):
        y = list(np.array(np.log(N_0/Y[i])))
        build_graph(x = list(X[i]), y = y, label = labels[i], fig_name = f"graph{i+1}", i = 2)
        plt.close()

    for i in range(3):
        y = np.array(np.log(N_0/Y[i]))
        build_graph(x = X[i], y = y, label = labels[i], fig_name = f"all", i = i)
    plt.close()


if __name__ == '__main__':
    main()