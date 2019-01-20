import multiprocessing as mp

def f(x, y):
    x.acquire()
    try:
        print('hello world', y)
    finally:
        x.release()

if __name__ == "__main__":
    lock = mp.Lock()

    for num in range(10):
        mp.Process(target=f, args=(lock, num)).start()
    