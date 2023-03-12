import numpy as np
import sys
import math

def main(marks):
    print(f"marks = {marks} ({len(marks)})")
    disp = np.var(marks)
    aver = sum(marks) / len(marks)
    disp2 = np.sqrt(disp) / np.sqrt(len(marks) - 1)
    print(f"average: {aver}\ndisper : {disp2}")

if __name__ == '__main__':
    marks = []
    for par in sys.argv:
        marks.append(par)
    marks.pop(0)
    main([int(mark) for mark in marks])