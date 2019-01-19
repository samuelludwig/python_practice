import multiprocessing

def square(x):
    return x*x

if __name__ == '__main__':
    with multiprocessing.Pool(5) as p:
        print(p.map(square, [1, 2, 3]))