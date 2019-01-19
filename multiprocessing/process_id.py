import multiprocessing
import os

def info(title):
    print(title)
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())

def hello_name(name):
    info("function hello_name")
    print("hello", name)
    

if __name__ == "__main__":
    info("main_line")
    p = multiprocessing.Process(target=hello_name, args=("country roads",))
    p.start()
    p.join()