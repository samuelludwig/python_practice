import multiprocessing as mp

def f(q):
    q.put([42, None, 'hello'])

if __name__ == "__main__":
    my_q = mp.Queue()
    p = mp.Process(target=f, args=(my_q,))
    p.start()
    print(my_q.get())
    p.join()