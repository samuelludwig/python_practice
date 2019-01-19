import multiprocessing
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import process

if __name__ == "__main__":
    with multiprocessing.Pool(6) as p:
        print(p.starmap(process.count_down, [("p1", 30), ("p2", 30)]))
    