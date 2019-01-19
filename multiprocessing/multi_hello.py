import multiprocessing

def hello(place):
    print('hello', place)

if __name__ == '__main__':
    p = multiprocessing.Process(target=hello, args=('world',))
    j = multiprocessing.Process(target=hello, args=('west virginia',))
    j.start()
    p.start()
    j.join()
    p.join()