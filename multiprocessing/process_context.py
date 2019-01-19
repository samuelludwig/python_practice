import multiprocessing as mp

def hello(q):
    q.put("hello")

if __name__ == "__main__":
    context = mp.get_context("spawn")
    queue = context.Queue()
    p = context.Process(target=hello, args=(queue,))
    p.start()
    print(queue.get())
    p.join()