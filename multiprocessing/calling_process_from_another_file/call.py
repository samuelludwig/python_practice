import multiprocessing
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import process

if __name__ == "__main__":
    p1 = multiprocessing.Process(
        target=process.count_down, args=("p1", 20))
    p2 = multiprocessing.Process(
        target=process.count_down, args=("p2", 20))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()