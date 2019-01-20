import multiprocessing as mp 

def f(n, a):
    n.value = 3.14
    for i in range(len(a)):
        a[i] = -a[i]
    
if __name__ == "__main__":
    num = mp.Value('d', 0.0) # 'd' indicates double
    arr = mp.Array('i', range(10)) # 'i' indicates signed int

    p = mp.Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])