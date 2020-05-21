from threading import Thread
from main import main


def main_threads():
    t1 = Thread(target=main)
    t2 = Thread(target=main)
    t3 = Thread(target=main)
    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':
    main_threads()
