import multiprocessing as mp

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = mp.Pipe()
    p = mp.Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()