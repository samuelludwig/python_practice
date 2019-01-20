import multiprocessing as mp

def f(c, d):
    c[1] = '1'
    c['2'] = 2
    c[0.25] = None
    d.reverse()

if __name__ == "__main__":
    with mp.Manager() as man:
        arg1 = man.dict()
        arg2 = man.list(range(10))

        p = mp.Process(target=f, args=(arg1, arg2))
        p.start()
        p.join()

        print(arg1)
        print(arg2)