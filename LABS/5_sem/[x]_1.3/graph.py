import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile # импорт модуля scipy.io.wavfile


def graph2_61():
    x = [2.639,
    3.162,
    3.566,
    4.111,
    4.502,
    5.299,
    4.737,
    6.325,
    6.802,
    7.095,
    7.503,
    8.232,
    9.488,
    10.625,
    11.006,
    11.588,
    11.528,
    12.197,
    12.193 ]
    y = [0.0295,
0.18,
0.216,
0.227,
0.2275,
0.2115,
0.2288,
0.1868,
0.1718,
0.162,
0.1472,
0.1255,
0.1025,
0.0987,
0.1009,
0.1056,
0.1052,
0.1104,
0.1106]

    plt.plot(x, y, '+', label="Ia (Vc) при V накала = 2,61 В")
    #plt.yticks(10)
    plt.grid()
    plt.xlabel("$V_c$, В")                                          # подпись оси X
    plt.ylabel("$I_a$, мА")             # подпись оси Y
    plt.legend(loc='best', bbox_to_anchor=(1, 1))
    plt.tight_layout() 
    plt.savefig("I_V_static_261")


def graph2_98():
    x = np.array([2.979, 3.261, 3.514, 3.858, 4.045, 4.435, 5.028, 5.254, 5.424, 6.032, 6.248,
6.557,
6.73,
7.047,
7.472,
7.856,
8.712,
9.515,
10.394,
10.701,
11.28,
10.713,
10.85])
    y = np.array([0.3834,
0.4771,
0.5368,
0.6001,
0.629,
0.6751,
0.7091,
0.7145,
0.7172,
0.7123,
0.7068,
0.6929,
0.6828,
0.6589,
0.6208,
0.5862,
0.5131,
0.4682,
0.4586,
0.4652,
0.4842,
0.4685,
0.4748])
    print(f"len x = {len(x)}, len y = {len(y)}")

    plt.plot(x, y, '+', label="Ia (Vc) при V накала = 2,98 В")
    #plt.yticks(10)
    plt.grid()
    plt.xlabel("$V_c$, В")                                          # подпись оси X
    plt.ylabel("$I_a$, мА")             # подпись оси Y
    plt.legend(loc='best', bbox_to_anchor=(1, 1))
    plt.tight_layout() 
    plt.savefig("I_V_static_298")

def graph3():
    x1 = np.array([2.639,
    3.162,
    3.566,
    4.111,
    4.502,
    5.299,
    4.737,
    6.325,
    6.802,
    7.095,
    7.503,
    8.232,
    9.488,
    10.625,
    11.006,
    11.588,
    11.528,
    12.197,
    12.193 ])
    y1 = np.array([0.0295,
0.18,
0.216,
0.227,
0.2275,
0.2115,
0.2288,
0.1868,
0.1718,
0.162,
0.1472,
0.1255,
0.1025,
0.0987,
0.1009,
0.1056,
0.1052,
0.1104,
0.1106])

    x2 = np.array([2.979, 3.261, 3.514, 3.858, 4.045, 4.435, 5.028, 5.254, 5.424, 6.032, 6.248,
6.557,
6.73,
7.047,
7.472,
7.856,
8.712,
9.515,
10.394,
10.701,
11.28,
10.713,
10.85])
    y2 = np.array([0.3834,
0.4771,
0.5368,
0.6001,
0.629,
0.6751,
0.7091,
0.7145,
0.7172,
0.7123,
0.7068,
0.6929,
0.6828,
0.6589,
0.6208,
0.5862,
0.5131,
0.4682,
0.4586,
0.4652,
0.4842,
0.4685,
0.4748])
    
    y1_new = -np.emath.log(y1) # add smth
    y2_new = -np.emath.log(y2) # add smth

    print (y2_new)

    plt.plot(x1, y1_new, '+', label="w(-lnV); V накала = 2,61 В")
    #plt.yticks(10)
    plt.grid()
    plt.xlabel("$-ln(V_c)$")                                          # подпись оси X
    plt.ylabel("$w$")             # подпись оси Y
    plt.legend(loc='best', bbox_to_anchor=(1, 1))
    plt.tight_layout() 

    plt.savefig("w_v_61")

    plt.close()

    plt.plot(x2, y2_new, '+', label=" w(-lnV); V накала = 2,98 В")
    plt.grid()
    plt.xlabel("$-ln(V_c)$")                                          # подпись оси X
    plt.ylabel("$w$")             # подпись оси Y
    plt.legend(loc='best', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.savefig("w_v_98")


def both():
    graph2_61()
    graph2_98()

def main():
    #graph2_61()
    #plt.close()
    #graph2_98()
    #both()
    graph3()


if __name__ == '__main__':
    main()