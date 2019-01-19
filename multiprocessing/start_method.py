import multiprocessing as mp
import os

def hey_there(q):
    q.put("hello")
    print(os.getpid())

if __name__ == "__main__":
    mp.set_start_method('spawn')
    my_queue = mp.Queue()
    p = mp.Process(target=hey_there, args=(my_queue,))
    p.start()
    print(my_queue.get())
    p.join()